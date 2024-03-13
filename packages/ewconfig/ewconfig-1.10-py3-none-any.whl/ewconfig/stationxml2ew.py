from argparse import ArgumentParser
from logging import getLogger
from os import getcwd, mkdir, unlink
from os.path import sep, join, exists

from obspy import read_inventory
from obspy.io.stationxml.core import validate_stationxml

from .lib.args import ParagraphHelpFormatter, add_version_args
from .lib.date import parse_date, between
from .lib.file import assert_dir
from .lib.filter import Filter
from .lib.log import add_log_args, make_log_from_args
from .lib.markdown import add_md_help_argument
from .lib.write import write_all, add_write_args, DEFAULT_PICK_FP_STA
from .pz.xml import XmlPolesZeros, Response, UnsupportedResponseException

'''
The equivalent of sacpz2ew, but takes input from station.xml files. 
'''

log = getLogger(__name__)


def _validate(file):
    ok, errors = validate_stationxml(file)
    if not ok:
        log.info('The following warnings are from XML validation:')
        for error in errors:
            log.warning(error)
        # paul's Ince_v1 file triggers warnings
        log.info('End of XML validation warnings')
        log.info('Will continue despite warnings above')


def _nscl(network, station, channel):
    return f'{network.code}.{station.code}.{channel.code}.' \
           f'{channel.location_code if channel.location_code else "--"}'


def _filter(metadata, sta_filter, chan_filter, date=None):
    # warning - this actually mutates the metadata
    for network in metadata:
        for station in list(network):
            sta_used = False
            if sta_filter.test(station, key=lambda sta: sta.code):
                for channel in list(station):
                    chan_used = False
                    nscl = _nscl(network, station, channel)
                    if chan_filter.test(channel, key=lambda chan: chan.code):
                        if between(channel.start_date, date, channel.end_date):
                            log.debug(f'Keeping {nscl} ({date if date else "now"} included)')
                            chan_used = True
                            sta_used = True
                    if not chan_used:
                        log.warning(f'Deleting {nscl}: {date} not in {channel.start_date} - {channel.end_date}')
                        station.channels.remove(channel)
            if not sta_used:
                log.info(f'Deleting station {station} because it was either filtered by command line args, '
                         f'or it has no channels')
                network.stations.remove(station)
    return metadata


def _parse(metadata, lo_precision=False, default_response=None):
    for network in metadata.networks:
        for station in network.stations:
            for channel in station.channels:
                nscl = _nscl(network, station, channel)
                try:
                    log.debug(f'Processing {nscl}')
                    yield XmlPolesZeros(network, station, channel,
                                        lo_precision=lo_precision, default_response=default_response)
                except UnsupportedResponseException as e:
                    log.warning(f'Skipping {nscl}: {e}')


def main_multiple(files, dirs=None, xml_outs=None, drop_comment=False, m_to_nm=1, geophone=False,
                  lo_precision=False, default_response=None, date=None, pick_fp_sta=DEFAULT_PICK_FP_STA,
                  sta_filter=Filter('Station'), chan_filter=Filter('Channel')):
    if len(files) == 1 and not dirs:
        dirs = [None]
    if len(dirs) != len(files):
        raise Exception('The number of output directories must match the number of XML files.')
    if not xml_outs:
        # None is set to a value later (based on filtered stations)
        xml_outs = [None] * len(files)
    if len(xml_outs) != len(files):
        raise Exception('If output files are given (--xml-out) the number of files must match the number of '
                        'input XML files.')
    if any(sep in xml_out for xml_out in xml_outs if xml_out):
        raise Exception('Output XML (--xml-out) files must not contain slashes (they go in the stationxml dir)')
    for file, dir, xml_out in zip(files, dirs, xml_outs):
        log.info(f'Expanding {file} into {dir}')
        main_single(file, dir=dir, xml_out=xml_out, drop_comment=drop_comment, m_to_nm=m_to_nm, geophone=geophone,
                    lo_precision=lo_precision, default_response=default_response, date=date, pick_fp_sta=pick_fp_sta,
                    sta_filter=sta_filter, chan_filter=chan_filter)


def _first_sta(net):
    stas = sorted((sta for sta in net), key=lambda sta: sta.code)
    return net.code + '-' + stas[0].code


def _default_xml_name(metadata):
    nets = sorted((net for net in metadata), key=lambda net: net.code)
    name = _first_sta(nets[0])
    if len(nets) > 1:
        name += '-' + _first_sta(nets[-1])
    return name + '.xml'


def __fix_output_dir(dir, subdir):
    dir = join(dir, subdir)
    if not exists(dir):
        mkdir(dir)
    return dir


def _copy_xml_monolith(metadata, dir, xml_out, subdir='stationxml'):
    if not xml_out: xml_out = _default_xml_name(metadata)
    dir = __fix_output_dir(dir, subdir)
    xml_out = join(dir, xml_out)
    log.info(f'Writing filtered XML to {xml_out}')
    metadata.write(xml_out, format='STATIONXML')


def _copy_xml_by_net_sta(metadata, dir, subdir='stationxml'):
    dir = __fix_output_dir(dir, subdir)
    for net in metadata:
        net_dir = __fix_output_dir(dir, net.code)
        if not exists(net_dir):
            mkdir(net_dir)
        net_metadata = metadata
        for nm_net in list(net_metadata):
            if nm_net.code != net.code:
                net_metadata = net_metadata.remove(network=nm_net.code)
        for sta in net:
            sta_path = join(net_dir, sta.code + '.xml')
            if exists(sta_path):
                log.warning(f'Overwriting {sta_path}')
                unlink(sta_path)
            sta_metadata = net_metadata
            for sm_sta in list(sta_metadata[0]):
                if sm_sta.code != sta.code:
                    sta_metadata = sta_metadata.remove(network=net.code, station=sm_sta.code)
            log.info(f'Writing XML to {sta_path}')
            sta_metadata.write(sta_path, format='STATIONXML')


def main_single(file, dir=None, xml_out=None, drop_comment=False, m_to_nm=1, geophone=False,
                lo_precision=False, default_response=None, date=None, pick_fp_sta=DEFAULT_PICK_FP_STA,
                sta_filter=Filter('Station'), chan_filter=Filter('Channel')):
    log.debug(f'Calling stationxml2ew single for file={file} dir={dir} drop_comment={drop_comment} '
              f'm_to_nm={m_to_nm} geophone={geophone} lo_precision={lo_precision} '
              f'default_response={default_response}sta_filter={sta_filter} chan_filter={chan_filter} '
              f'date={date}')
    _validate(file)
    dir = assert_dir(dir or getcwd(), 'Output dir (--dir)', create=True)
    metadata = read_inventory(file)
    metadata = _filter(metadata, sta_filter, chan_filter, date=date)
    nscls = list(_parse(metadata, lo_precision=lo_precision, default_response=default_response))
    write_all(dir, nscls, drop_comment=drop_comment, m_to_nm=m_to_nm, geophone=geophone, pick_fp_sta=pick_fp_sta)
    if xml_out:
        _copy_xml_monolith(metadata, dir, xml_out)
    else:
        _copy_xml_by_net_sta(metadata, dir)

    
def add_stationxml2ew_args(parser):
    # separated here so that it can also be used by ewmerge
    parser.add_argument('--include-chan', metavar='PATTERN', nargs='*',
                        help='Pattern to match included channel names (default all).')
    parser.add_argument('--exclude-chan', metavar='PATTERN', nargs='*',
                        help='Pattern to match excluded channel names.')
    parser.add_argument('--include-sta', metavar='PATTERN', nargs='*',
                        help='Pattern to match included station names (default all).')
    parser.add_argument('--exclude-sta', metavar='PATTERN', nargs='*',
                        help='Pattern to match excluded station names.')
    parser.add_argument('--date', type=parse_date, help='Use channels valid on this date (default now).')
    parser.add_argument('--pick-fp-sta', metavar='STRING',
                        default=DEFAULT_PICK_FP_STA,
                        help=f'Extra values for pick_FP_sta.d (default "{DEFAULT_PICK_FP_STA}").')
    defaults = parser.add_mutually_exclusive_group()
    defaults.add_argument('--displacement', dest='default_response', action='store_const',
                          const=Response.DISPLACEMENT, help='Assume unrecognized responses are displacement.')
    defaults.add_argument('--velocity', dest='default_response', action='store_const',
                          const=Response.VELOCITY, help='Assume unrecognized responses are velocity.')
    defaults.add_argument('--acceleration', dest='default_response', action='store_const',
                          const=Response.ACCELERATION, help='Assume unrecognized responses are acceleration.')
    parser.set_defaults(default_response=None)
    add_write_args(parser, with_drop_comment=False)


def main_args():
    args = None  # used in cleanup
    try:
        parser = ArgumentParser(prog='stationxml2ew',
                                formatter_class=ParagraphHelpFormatter,
                                description='''A scanner program to 
convert a station.xml file to configurations suitable for use with localmag, hypoinverse, 
pick_ew, pick_FP, slink2ew, carlstatrig and wave_serverV station lists. It is presumed 
that the input file is complete, with lat/long/elevation for the SCNL.  Output sac files 
will be in meters unless the --nano parameter is set to convert to nanometers. 

Stations and channels can be selected using --include-chan (-sta) and --exclude-chan (-sta).
These take patterns that can match any string (*), any character (?), and any character from 
a sequence ([abc]).  If --include-chan (-sta) is not given it is assumed to be "*".  Channels,
for example, are included if they match --include-chan and do not match --exclude-chan.

Specifying --date selects channels active at that time.  By default this is the current time.

Responses types are recognised via the response units.  Unrecognised units can be given a default
using --displacement|--velocity|--acceleration.  If no default is given they are skipped.  Pressure
sensitive stations (units Pa) are always skipped.    

Examples

To generate a config in the current directory from an XML file:

stationxml2ew station.xml

To generate a config in a different directory:

stationxml2ew station.xml --dir output/dir

To process multiple XML files, each with a different output directory:

stationxml2ew station1.xml station2.xml --dir station1 station2

To convert multiple XML files into a single directory see ewmerge (which can
call this program and then do the merge to a single directory).
''')
        parser.add_argument('file', nargs='+', default=[], metavar='FILE',
                            help='Station XML file(s)')
        parser.add_argument('--dir', nargs='*', default=[], metavar='DIR',
                            help='Output directory(s) (default CWD for a single input file)')
        parser.add_argument('--xml-out', nargs='+', metavar='FILE', help='Filtered station.xml output')
        add_stationxml2ew_args(parser)
        add_version_args(parser)
        add_md_help_argument(parser)
        add_log_args(parser)
        args = parser.parse_args()
        make_log_from_args(parser.prog, args)
        main_multiple(args.file, dirs=args.dir, xml_outs=args.xml_out,
                      drop_comment=args.drop_comment, m_to_nm=args.nano, geophone=args.geophone,
                      default_response=args.default_response, date=args.date, pick_fp_sta=args.pick_fp_sta,
                      sta_filter=Filter('Station', includes=args.include_sta, excludes=args.exclude_sta),
                      chan_filter=Filter('Channel', includes=args.include_chan, excludes=args.exclude_chan))
    except Exception as e:
        log.critical(e)
        if args and args.verbosity == 5:
            log.exception(e)
        exit(1)


if __name__ == '__main__':
    main_args()

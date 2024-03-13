from argparse import ArgumentParser
from logging import getLogger
from os.path import isfile, exists
from shutil import move, rmtree

from ewconfig.lib.write import DEFAULT_PICK_FP_STA
from ewconfig.merge.xml import merge_xml
from .lib.args import ParagraphHelpFormatter, add_version_args
from .lib.file import assert_dir, tmp_dir, assert_empty_dir
from .lib.filter import Filter
from .lib.log import add_log_args, make_log_from_args
from .lib.markdown import add_md_help_argument
from .merge.binder import compute_binder_grid
from .merge.chan import merge_filtered_chan, sncl_sort
from .merge.prefer import Prefer
from .merge.rest import copy_rest
from .merge.sac import merge_sac
from .stationxml2ew import add_stationxml2ew_args, main_single

log = getLogger(__name__)


def expand_xml(file, drop_comment=False, m_to_nm=1, geophone=False,
               lo_precision=False, default_response=None,
               sta_filter=Filter('Station'), chan_filter=Filter('Channel'), date=None,
               pick_fp_sta=DEFAULT_PICK_FP_STA):
    if isfile(file):
        if not file.endswith('.xml'):
            log.warning(f'Treating {file} as a station.xml file and calling stationxml2ew')
        dir = tmp_dir()
        main_single(file, dir=dir, drop_comment=drop_comment, m_to_nm=m_to_nm, geophone=geophone,
                    lo_precision=lo_precision, default_response=default_response,
                    sta_filter=sta_filter, chan_filter=chan_filter, date=date, pick_fp_sta=pick_fp_sta)
        log.debug(f'Expanded {file} into {dir}')
        return dir, file
    else:
        return file, False


def _prepare_dirs(news, old=None, merged=None, backup=None):
    if old: old = assert_dir(old, 'Old directory (--old)')
    news = [(assert_dir(new, 'New directory (--new)'), delete) for new, delete in news]
    if not merged:
        merged = tmp_dir()
        log.info(f'Merging to temporary directory {merged}')
    merged = assert_empty_dir(merged, 'Merge directory (--merged)', extra=' (aborting with no changes made)')
    mergeds = [merged]
    while len(mergeds) < len(news):
        mergeds = [tmp_dir()] + mergeds  # pad to front so final merged at end
    if backup == 'NONE':
        log.warning('No backup (--backup NONE)')
        backup = None
    if backup and exists(backup):
        raise Exception(f'--backup {backup} already exists')
    return old, news, mergeds, backup


def main(news, old=None, merged=None, backup=None, prefer=Prefer.CHECK, sort=None,
         drop_comment=False, m_to_nm=1, geophone=False, lo_precision=False, default_response=None,
         sta_filter=Filter('Station'), chan_filter=Filter('Channel'),
         date=None, comment=None, all_chan=False, pick_fp_sta=DEFAULT_PICK_FP_STA):
    accumulate = None
    try:
        if backup and not old:
            raise Exception('--backup can only be used with --old')
        if not backup and not merged:
            raise Exception('Provide --merged or --backup (the latter only with --old)')
        news = [expand_xml(new, drop_comment=drop_comment, m_to_nm=m_to_nm, geophone=geophone,
                           lo_precision=lo_precision, default_response=default_response,
                           sta_filter=sta_filter, chan_filter=chan_filter, date=date, pick_fp_sta=pick_fp_sta)
                for new in news]
        old, news, mergeds, backup = _prepare_dirs(news, old=old, merged=merged, backup=backup)
        current_old = old  # where we have currently accumulated to
        for index, ((new, xml_file), accumulate) in enumerate(zip(news, mergeds)):
            if xml_file:
                log.debug(f'Processing {new}/{xml_file}')
                source = xml_file
            else:
                log.debug(f'Processing directory {new}')
                source = new
            merge_sac(current_old, new, accumulate, prefer, source)
            merge_filtered_chan(current_old, new, accumulate, prefer, sort, source,
                                comment if index == 1 else None, all=all_chan)
            merge_xml(current_old, new, accumulate, prefer)
            if xml_file:
                log.debug(f'Deleting temporary {new} (where {xml_file} was expanded)')
                rmtree(new)
            if current_old != old:  # so a temporary intermediate
                log.debug(f'Deleting temporary {current_old} (intermediate merge)')
                rmtree(current_old)
            current_old = accumulate
        copy_rest(old, current_old)

        # Processing for which the complete inventory is needed.
        compute_binder_grid(current_old)
        
        if merged:
            return accumulate
        else:
            if backup:
                log.info(f'Moving {old} to {backup} (creating backup)')
                move(old, backup)
            else:
                log.warning(f'Deleting {old} (--backup NONE)')
                rmtree(old)
            log.info(f'Moving {accumulate} to {old} (overwriting old)')
            move(accumulate, old)
            return backup
    except:
        if accumulate:
            if exists(accumulate):
                log.warning(f'You may need to delete intermediate data in {accumulate} '
                            f'(initial data should be unchanged)')
            elif not backup:
                log.warning(f'Check {old} for corrupt data (--backup NONE)')
        raise


def main_args():
    try:
        parser = ArgumentParser(prog='ewmerge', add_help=False,
                                formatter_class=ParagraphHelpFormatter,
                                description='''A program to merge EW configurations 
(at --old and --new) selecting entries based on NSCLs.

The --new sources can be Station XML format files or EW config directories.

In the final output, files in the eqk/response and chan sub-directories are merged / filtered 
from all directories and files.  All other configuration data are taken from --old (if given).

If --merged is given, the new, merged config is placed in that directory.

If --merged is not given, but --old is used, the merged config replaces the current contents
of the --old directory.  In this case --backup (which will contain the original contents of
--old) must be given.  If you really don't want a backup use "--backup NONE".

Examples

To merge data from all the station xml files in the "input" directory, placing the EW config
in the "output" directory:

    ewmerge --new input/*.xml --merged output
    
To merge data from all the station xml files in the "input" directory into an existing "config"
directory:

    ewmerge --new input/*.xml --old config --backup old-config
    
To merge data from all the station xml files in the "input" directory with an existing "config"
directory, placing the results in a new "output" directory:

    ewmerge --new input/*.xml --old config --merged output
''')
        group = parser.add_argument_group(title='Merge parameters')
        group.add_argument('--old', help='Directory for old (full) config.')
        group.add_argument('--new', required=True, nargs='+',
                           help='Directory(s) or XML file(s) for new (chan and response) config.  '
                                'XML files are expanded by stationxml2ew (see parameters below).')
        prefer = group.add_mutually_exclusive_group()
        prefer.add_argument('--prefer-old', action='store_const', dest='prefer', const=Prefer.OLD,
                            help='If a NSCL is present in old and new, use the old entries '
                                 '(default is to require identical entries).')
        prefer.add_argument('--prefer-new', action='store_const', dest='prefer', const=Prefer.NEW,
                            help='If a NSCL is present in old and new, use the new entries.')
        group.set_defaults(prefer=Prefer.CHECK)
        group.add_argument('--merged', help='Destination directory for merged config.')
        group.add_argument('--backup', help='Backup directory for old config (if --old and no --merged; can be NONE).')
        group.add_argument('--sort', type=sncl_sort, help='Sorting order for output (eg SNCL, NS).')
        group.add_argument('--comment', nargs='?', default=None, const='',
                           help='Comment before second file (no argument for timestamp only)')
        group.add_argument('--all-chan', action='store_true',
                           help='Fail if a file in the chan directory is an unknown type (default is to ignore).')
        group.add_argument('-h', action='help', help='Show this help message and exit.')
        add_version_args(group)
        add_md_help_argument(group)
        add_log_args(group)
        group = parser.add_argument_group(title='XML expansion parameters (passed to stationxml2ew)')
        add_stationxml2ew_args(group)
        args = parser.parse_args()
        make_log_from_args(parser.prog, args)
        output = main(news=args.new, old=args.old, merged=args.merged, backup=args.backup,
                      prefer=args.prefer, sort=args.sort,
                      drop_comment=args.drop_comment, m_to_nm=args.nano, geophone=args.geophone,
                      default_response=args.default_response, date=args.date, comment=args.comment,
                      pick_fp_sta=args.pick_fp_sta, all_chan=args.all_chan,
                      sta_filter=Filter('Station', includes=args.include_sta, excludes=args.exclude_sta),
                      chan_filter=Filter('Channel', includes=args.include_chan, excludes=args.exclude_chan))
    except Exception as e:
        log.critical(e)
        exit(1)


if __name__ == '__main__':
    main_args()

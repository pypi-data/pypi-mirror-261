from collections import defaultdict
from logging import getLogger
from os.path import join
from re import match

from ewconfig.lib.file import assert_empty_dir
import ewconfig.merge.binder as binder

log = getLogger(__name__)

DEFAULT_PICK_FP_STA = '-1 -1 10.0 10.0 -1'

INST = 'INST_WILDCARD'
MOD = 'MOD_WILDCARD'
INDEX_SIZE = 10000
TANKSIZE_VAR = '${WSV_TANK_MEGS}'
TANKDIR_VAR = '${WSV_TANK_DIR}'
EWDATA_VAR = '${EW_DATA_DIR}'

NM_IN_M = 1e9


def write_pz_ew(dir, sncl, drop_comment=False, m_to_nm=1):
    with open(join(dir, "%s.%s.%s.%s.sac" % (sncl.net, sncl.sta, sncl.chan, sncl.loc)), "w") as f:
        if not drop_comment:
            f.write(sncl.keep_comment)
        f.write("ZEROS   %d\n" % len(sncl.zeros_lines))
        for line in sncl.zeros_lines:
            f.write(line)
        f.write("POLES   %d\n" % len(sncl.poles_lines))
        for line in sncl.poles_lines:
            f.write(line)
        sncl.constant = sncl.constant / m_to_nm
        if m_to_nm == 1:
            comment = 'UNITS IN M'
        elif m_to_nm == NM_IN_M:
            comment = 'UNITS IN NM'
        else:
            comment = f'UNITS UNKNOWN (FACTOR {m_to_nm:g})'
        f.write(f"* {comment}\nCONSTANT        {sncl.constant:e}\n")


def write_wsv(dir, sncls):
    with open(join(dir, 'wsv_chan_list.d'), 'w') as f:
        f.write(
            "#          names       size  (TYPE_TRACEBUF2 only)         (megabytes) (max breaks)     (full path)      Tank\n")
        for sncl in sncls:
            f.write("Tank %s %s %s %s 4096 %s %s %s %d %s/%s/%s.%s.%s.%s.wsv_tnk\n" % \
                    (sncl.sta, sncl.chan, sncl.net, sncl.loc, INST, MOD, TANKSIZE_VAR, INDEX_SIZE, EWDATA_VAR, TANKDIR_VAR, \
                     sncl.sta, sncl.chan, sncl.net, sncl.loc))


def write_pick_sta(dir, sncls, geophone=False):
    # example from Raton
    #    1     1  T25A  BHZ TA -- 3  40  3 162  500  3  .939  3.  .4  .015 5.  .9961  1200. 132.7   .8  1.5 135000. 8388608
    #    1     1  T25A  BHE TA -- 3  40  3 162  500  3  .939  3.  .4  .015 5.  .9961  1200. 132.7   .8  1.5 135000. 8388608
    #    1     1  T25A  BHN TA -- 3  40  3 162  500  3  .939  3.  .4  .015 5.  .9961  1200. 132.7   .8  1.5 135000. 8388608
    with open(join(dir, 'pick_sta.d'), 'w') as f:
        f.write(
            '#\n #                              MinBigZC       RawDataFilt    LtaFilt         DeadSta          PreEvent\n')
        f.write('# Pick  Pin    Station/   MinSmallZC   MaxMint           StaFilt       RmavFilt           AltCoda\n')
        f.write(
            '# Flag  Numb   Comp/Net   Itr1   MinPeakSize  i9  CharFuncFilt  EventThresh          CodaTerm         Erefs\n')
        f.write(
            '# ----  ----   --------   ----------------------------------------------------------------------------------\n')
        for sncl in sncls:
            if geophone or sncl.chan.startswith('E'):
                f.write("1 1 %s %s %s %s 3 40 3 300 500 0 .985 0. .0198 .002 3. .9961 1200. 100.0 .8 1.5 50000. 8388608\n" % \
                        (sncl.sta, sncl.chan, sncl.net, sncl.loc))
            else:
                f.write(
                    "1  1 %s %s %s %s 3  40  3 162  500  3  .939  3.  .4  .015 5.  .9961  1200. 132.7   .8  1.5 135000. 8388608\n" % \
                    (sncl.sta, sncl.chan, sncl.net, sncl.loc))


def expand_angle(angle, pos, neg):
    if angle < 0:
        char = neg
        angle = abs(angle)
    else:
        char = pos
    degrees = int(angle)
    minutes = (angle - degrees) * 60.
    return degrees, minutes, char


def write_hinv_sta(dir, sncls):
    # P02   XR  EHZ  37 05.0890 104 51.1720 17830.0     0.02  0.00  0.00  0.00    0.0000
    with open(join(dir, 'hinv_sta.d'), 'w') as f:
        for sncl in sncls:
            lat_deg, lat_min, lat_char = expand_angle(sncl.lat, ' ', 'S')
            lon_deg, lon_min, lon_char = expand_angle(sncl.lon, 'E', ' ')
            f.write("%-5s %2s  %3s  %2d %7.4f%1s%3d %7.4f%1s%4d0.0     0.00  0.00  0.00  0.00    0.00%2s\n" % \
                    (sncl.sta, sncl.net, sncl.chan, lat_deg, lat_min, lat_char, lon_deg, lon_min, lon_char, int(sncl.elev), sncl.loc))


def write_binder_grid(dir, sncls):
    ''' Write grid configuration for binder_ew.

    '''
    with open(join(dir, 'binder_grid.d'), 'w') as f:
        # Compute the grid boundaries.
        lat = [x.lat for x in sncls]
        lon = [x.lon for x in sncls]

        round_dec = 2
        grid_limits = binder.compute_grid_limits(lon = lon,
                                                 lat = lat,
                                                 round_dec = round_dec)

        grid_params = binder.compute_grid_parameters(lon = lon,
                                                     lat = lat)

        float_string = '{{:.{:d}f}}'.format(round_dec)
        template_lat = 'grdlat    {}    {}\n'.format(float_string,
                                                     float_string)
        template_lon = 'grdlon    {}    {}\n'.format(float_string,
                                                     float_string)
        f.write(template_lon.format(grid_limits[0],
                                    grid_limits[1]))
        f.write(template_lat.format(grid_limits[2],
                                    grid_limits[3]))
        f.write('dspace    {:f}\n'.format(grid_params['dspace']))
        f.write('rstack    {:f}\n'.format(grid_params['rstack']))
        f.write('tstack    {:f}\n'.format(grid_params['tstack']))


def write_seed_link_stas2(dir, sncls):
    ns_to_chan02 = defaultdict(set)
    for sncl in sncls:
        ns = f'{sncl.net}_{sncl.sta}'
        ns_to_chan02[ns].add(sncl.chan[0:2])
    with open(join(dir, 'slink_imports.d'), 'w') as f:
        for ns in sorted(ns_to_chan02.keys()):
            chans = " ".join(f'{chan02}?.D' for chan02 in sorted(ns_to_chan02[ns]))
            f.write(f'Stream   {ns} "{chans}"\n')


def write_pick_fp(dir, sncls, pick_fp_sta):
    #                                      threshold1
    # Pick  Pin     Sta/Comp           longTermWindow  tUpEvent
    # Flag  Numb    Net/Loc       filterWindow  threshold2
    # ----  ----    --------      -----------------------------
    #    1    00  AVG 2.4 6.0 10.0 8.0 0.2
    #
    # ----  ----   --------   ----------------------------------------------------------------------------------
    # 1  1 ACSO BH1 US 00  2.4 6.0 10.0 8.0 0.2
    with open(join(dir, 'pick_FP_sta.d'), 'w') as f:
        f.write('#                                      threshold1\n')
        f.write('# Pick  Pin     Sta/Comp           longTermWindow  tUpEvent\n')
        f.write('# Flag  Numb    Net/Loc       filterWindow  threshold2\n')
        f.write('# ----  ----    --------      -----------------------------\n')
        for sncl in sncls:
            f.write("1    1 %s %s %s %s %s\n" % \
                    (sncl.sta, sncl.chan, sncl.net, sncl.loc, pick_fp_sta))


def write_trigsta(dir, sncls):
    with open(join(dir, 'trigsta.scnl'), 'w') as f:
        for sncl in sncls:
            f.write("TrigStation %s %s %s %s\n" % (sncl.sta, sncl.chan, sncl.net, sncl.loc))


def write_tbuf2mseed(dir, sncls):
    with open(join(dir, 'tbuf2mseed.d'), 'w') as f:
        for sncl in sncls:
            f.write("Send_scnl %s %s %s %s 10\n" % (sncl.sta, sncl.chan, sncl.net, sncl.loc))


def write_carlsta(dir, sncls):
    with open(join(dir, 'carlsta.scnl'), 'w') as f:
        for sncl in sncls:
            # the 10 is a TTL.  see discussion in issue #6 - if the user wants a different
            # value they can edit the file.
            f.write("station %s %s %s %s 10\n" % (sncl.sta, sncl.chan, sncl.net, sncl.loc))


def write_fir(dir, sncls):
    # sncls are already sorted so stations are grouped together
    with open(join(dir, 'fir.scnl'), 'w') as f:
        for sncl in sncls:
            f.write("GetSCNL %s %s %s %s %s %s %s %s\n" %
                    (sncl.sta, sncl.chan, sncl.net, sncl.loc, sncl.sta, sncl.chan, sncl.net, sncl.loc))


ITYPES = {'.N': 1, '[BH]H': 2, '[SE]H': 3}


def write_stalist(dir, sncls):
    with open(join(dir, 'stalist.txt'), 'w') as f:
        for sncl in sncls:
            itype = None
            for (prefix, value) in ITYPES.items():
                if match(prefix, sncl.chan.upper()):
                    itype = value
            if itype:
                f.write("%s %s %s %s %f %f %f %f %s\n" %
                        (sncl.sta, sncl.chan, sncl.net, sncl.loc,
                         sncl.lat, sncl.lon, sncl.rate, sncl.gain, itype))
            else:
                log.warning(f'No match for {sncl} when writing stalist.txt')


def log_pz(sncl):
    log.info("%s lat=%f lon=%f elev=%f const=%e np=%d nz=%d" %
             (sncl, sncl.lat, sncl.lon,
              sncl.elev, sncl.constant, len(sncl.poles_lines), len(sncl.zeros_lines)))


def write_all(dir, sncls, drop_comment=False, m_to_nm=1, geophone=False,
              pick_fp_sta=DEFAULT_PICK_FP_STA):
    # we sort so that the output is constant even if different sources generate sncls in different orders
    sncls = sorted(sncls, key=str)
    chan = assert_empty_dir(join(dir, 'chan'), extra=' (aborting with some changes already made to the system)')
    eqk = assert_empty_dir(join(dir, 'eqk'), extra=' (aborting with some changes already made to the system)')
    write_wsv(chan, sncls)
    write_pick_sta(chan, sncls, geophone=geophone)
    write_pick_fp(chan, sncls, pick_fp_sta)
    write_hinv_sta(chan, sncls)
    write_trigsta(chan, sncls)
    write_tbuf2mseed(chan, sncls)
    write_stalist(chan, sncls)
    z_sncls = [sncl for sncl in sncls if sncl.chan.endswith('Z')]
    write_carlsta(chan, z_sncls)
    write_fir(chan, z_sncls)
    eqk_response = assert_empty_dir(join(dir, 'eqk', 'response'),
                                    extra=' (aborting with some changes already made to the system)')
    for sncl in sncls:
        write_pz_ew(eqk_response, sncl, drop_comment=drop_comment, m_to_nm=m_to_nm)
    write_seed_link_stas2(chan, sncls)

    write_binder_grid(eqk, sncls)


def add_write_args(parser, with_drop_comment=True):
    if with_drop_comment:
        parser.add_argument('-d', '--drop-comment', action="store_true",
                            help='Delete the comments from the sac output.')
    else:
        parser.set_defaults(drop_comment=False)
    parser.add_argument('-n', '--nano', action='store_const',
                        const=NM_IN_M, default=1,
                        help='Convert Constant meters into nanometers. '
                             'You must use this option if you are using the default Localmag or GMEW settings. '
                             'If you have enabled the ResponseInMeters option in localmag.d and/or gmew.d, '
                             'then you don\'t need this option.')
    parser.add_argument('-g', '--geophone', action="store_true",
                        help='Treat ALL instruments as Geophones in pick_ew output. '
                             'Otherwise broadband settings are used unless channel starts with E.')

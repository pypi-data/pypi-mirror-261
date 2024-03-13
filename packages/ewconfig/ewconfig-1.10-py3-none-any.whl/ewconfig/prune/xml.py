from glob import glob
from logging import getLogger
from os import unlink
from os.path import join

from obspy import read_inventory

log = getLogger(__name__)


def _delete_file(file, filter, force=False):
    deleted = False

    def warn(code):
        nonlocal deleted
        if not deleted:
            print(f'DELETIONS in {file}')
            deleted = True
        print('  ' + code)

    metadata = read_inventory(file)
    for net in list(metadata):
        for sta in list(net):
            for chan in list(sta):
                nscl = f'{net.code}.{sta.code}.{chan.code}.{chan.location_code}'
                if filter.test(nscl):
                    warn(nscl)
                    if force:
                        metadata.remove(network=net.code, station=sta.code, channel=chan.code)
            ns = f'{net.code}.{sta.code}'
            if filter.test(ns):
                warn(ns)
                if force:
                    metadata.remove(network=net.code, station=sta.code)
        if force and len(net) == 0:
            log.debug(f'Deleting {net.code} as no stations remaining')
            metadata.remove(network=net.code)
    if force:
        unlink(file)
        log.info(f'Writing filtered XML to {file}')
        metadata.write(file, format='STATIONXML')


def delete_xml(dir, filter, force=False):
    for file in glob(join(dir, 'stationxml', '*', '*.xml')):
        _delete_file(file, filter, force=force)


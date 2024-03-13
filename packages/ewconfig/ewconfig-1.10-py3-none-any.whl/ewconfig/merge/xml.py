from glob import glob
from logging import getLogger
from os import mkdir, scandir
from os.path import join, exists, basename, splitext
from shutil import copyfile

from obspy import read_inventory

from ewconfig.merge.prefer import Prefer

log = getLogger(__name__)


def merge_xml(old, new, merged, prefer, subdir='stationxml'):
    src_old = join(old, subdir) if old else None
    src_new = join(new, subdir) if new else None
    dest = join(merged, subdir)
    if prefer == Prefer.OLD:
        _merge_xml_recursive(src_old, src_new, dest, False)
    elif prefer == Prefer.NEW:
        _merge_xml_recursive(src_new, src_old, dest, False)
    else:
        _merge_xml_recursive(src_new, src_old, dest, True)


def _merge_xml_recursive(over, base, dest, unique):

    def make_dest_on_demand():
        if not exists(dest):
            mkdir(dest)

    def xml_files_in(dir):
        yield from (basename(file) for file in glob(join(dir, '*.xml')))

    def subdirs_in(dir):
        yield from (basename(dir.path) for dir in scandir(dir) if dir.is_dir())

    known = set()
    if base and exists(base):
        make_dest_on_demand()
        for file in xml_files_in(base):
            known.add(file)
            log.debug(f'Copying {file} from {base} to {dest}')
            copyfile(join(base, file), join(dest, file))
    if over and exists(over):
        make_dest_on_demand()
        for file in xml_files_in(over):
            if unique and file in known:
                if read_inventory(join(base, file)) == read_inventory(join(over, file)):
                    log.debug(f'{file} in both {over} and {base} but identical')
                else:
                    raise Exception(f'{file} in {over} and {base} differ (use --prefer-new or --prefer-old)')
            else:
                log.debug(f'Copying {file} from {over} to {dest}')
                copyfile(join(over, file), join(dest, file))
    known = set()
    if base and exists(base):
        make_dest_on_demand()
        for dir in subdirs_in(base):
            known.add(dir)
            _merge_xml_recursive(join(over, dir) if over else None, join(base, dir), join(dest, dir), unique)
    if over and exists(over):
        make_dest_on_demand()
        for dir in subdirs_in(over):
            if dir not in known:
                _merge_xml_recursive(join(over, dir), join(base, dir) if base else None, join(dest, dir), unique)

from logging import getLogger
from os.path import exists, basename
from shutil import copytree, copy2

log = getLogger(__name__)


def copy_rest(old, merged):
    if old:
        log.info(f'Copying rest of {old} to {merged}')
        copytree(old, merged, ignore=_copy_filter(old), dirs_exist_ok=True, copy_function=_error_on_overwrite)
    else:
        log.warning('No additional config (specify --old)')


def _error_on_overwrite(src, dst):
    """
    This is to highlight any failure in assumptions made.  Issue 28 occurred because we were
    over-writing files.  The bug was elsewhere (in _copy_filter below), but we would have
    detected it here.
    """
    if exists(dst):
        raise Exception(f'Refusing to copy {src} to {dst} because file already exists')
    else:
        copy2(src, dst)


def _copy_filter(old):

    def select(files, *exclude):
        return [file for file in files if file in exclude]

    def filter(dir, files):
        if dir == old:
            return select(files, 'chan', 'stationxml')
        elif basename(dir) == 'eqk':
            return select(files, 'response')
        else:
            return []

    return filter

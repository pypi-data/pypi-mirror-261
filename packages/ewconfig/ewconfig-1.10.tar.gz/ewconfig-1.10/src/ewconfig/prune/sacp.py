import re
from glob import glob
from os.path import join

from ewconfig.prune.file import delete_file

FILE = re.compile(r'.*/(SAC_PZs_.*)')
NSCL = re.compile(r'SAC_PZs_([A-Z0-9]+_[A-Z0-9]+_[A-Z0-9]+_[A-Z0-9]*)_\d+\.')


def parse_path(path):
    file = FILE.match(path).group(1)
    nscl = NSCL.match(file).group(1).replace('_', '.')
    return nscl, file


def delete_sacp(dir, pattern, force=False):
    delete_file(glob(join(dir, 'SAC_PZs_*')), pattern, parse_path, 'SACP', force=force)

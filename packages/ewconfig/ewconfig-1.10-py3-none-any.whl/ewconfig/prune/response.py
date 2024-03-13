import re
from glob import glob
from os.path import join, basename

from ewconfig.prune.file import delete_file

NSCL = re.compile(r'([A-Z0-9]+\.[A-Z0-9]+\.[A-Z0-9]+\.[A-Z0-9]+)\.sac')


def parse_path(path):
    file = basename(path)
    nscl = NSCL.match(file).group(1)
    return nscl, file


def delete_response(dir, pattern, force=False):
    delete_file(glob(join(dir, 'eqk', 'response', '*.sac')), pattern, parse_path, 'response', force=force)

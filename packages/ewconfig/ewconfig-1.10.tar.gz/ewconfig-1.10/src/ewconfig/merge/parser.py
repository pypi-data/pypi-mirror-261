from abc import ABC
from logging import getLogger
from os import makedirs
from os.path import join, exists

log = getLogger(__name__)


class BaseParser(ABC):

    def __init__(self, file, source):
        self._file = file
        self._source = source
        self.__deletion = False

    def read(self, dir, comment=None):
        path = join(dir, 'chan', self._file)
        if exists(path):
            log.debug(f'Reading {path}')
            with open(path, 'r') as src:
                self._read(src, comment=comment)
        else:
            log.warning(f'Could not find {path}')

    def _read(self, file, comment=None):
        raise NotImplementedError('_read')

    def add(self, new):
        raise NotImplementedError('add')

    def write(self, merged):
        dir = join(merged, 'chan')
        if not exists(dir):
            makedirs(dir)
        path = join(dir, self._file)
        log.info(f'Writing {path}')
        with open(path, 'w') as file:
            self._write(file)

    def _write(self, file):
        raise NotImplementedError('_write')

    def _print_deletion(self, lines):
        # presumably there was a reason this prints rather than logs
        # i guess so that it uses stdout rather than stderr?
        if not self.__deletion:
            print(f'DELETIONS in {self._source}:')
            self.__deletion = True
        for line in lines:
            print('  ', line, end='' if line.endswith('\n') else '\n')

    def _end_deletions(self):
        if not self.__deletion:
            print(f'UNCHANGED {self._source}')

from logging import getLogger
from os import listdir
from os.path import join, exists
from re import compile
import datetime as dt
from textwrap import wrap

from .parser import BaseParser
from .prefer import Prefer
from ewconfig.lib.file import fix_newline

log = getLogger(__name__)

PARSERS = {}


def merge_filtered_chan(old, new, merged, prefer, sort, source, comment, all=False):
    # by the time we get here we've used the filters to select NSCLs from the two directories
    all_files = set(ls_chan(old)).union(ls_chan(new))
    for file in sorted(all_files):
        if file in PARSERS:
            Parser = PARSERS[file]
            log.debug(f'Parsing {file} with {Parser}')
            new_parser = Parser(file, prefer, sort, source)
            new_parser.read(new, comment)
            if old:
                old_parser = Parser(file, prefer, sort, join(old, file))
                old_parser.read(old)
                old_parser.add(new_parser)
                old_parser.write(merged)
            else:
                new_parser.write(merged)
        else:
            if all:
                raise Exception(f'No support for {file} (see --all-chan)')
            else:
                log.warning(f'No support for {file} (ignoring; use --all-chan to fail in this case)')


def ls_chan(dir):
    if dir:
        chan = join(dir, 'chan')
        if exists(chan):
            return listdir(chan)
    return []


def sncl_sort(template):
    """
    The type used for search templates.
    """
    template = template.toupper()
    if len(set(template)) != len(template):
        raise Exception(f'Repetitions in {template}')
    for letter in template:
        if letter not in 'NSCL':
            raise Exception(f'Bad character {letter} in {template} (not S, N, C, or L)')
    return template


COMMENT = compile(r'^\s*(?:\s*|#.*)$')
END = None


class RegexParser(BaseParser):
    '''
    Files with an optional header where each line contains NSCL related data.
    Each line is matched against a pattern and compared with the pre-selected NSCLs.
    '''

    def __init__(self, line_regex, file, prefer, sort, source):
        self.__line_regex = line_regex
        self.__prefer = prefer
        self.__sort = sort
        self.__comments = {}
        self.__lines = {}
        super().__init__(file, source)

    def _match_to_key(self, match):
        raise NotImplementedError('_match_to_key')

    def _initial_comments(self, comment):
        if comment is None:
            return []
        else:
            date = dt.date.today().isoformat()
            if comment:
                comment = f'{date} {comment} Added by ewmerge, part of ewconfig.'
            else:
                comment = f'{date} Added by ewmerge, part of ewconfig.'
            return [fix_newline(line)
                    for line in wrap(comment, width=78, initial_indent='# ', subsequent_indent='# ')]

    def _read(self, file, comment=None):
        comments = self._initial_comments(comment)
        for line in file:
            line = fix_newline(line)
            if COMMENT.match(line):
                comments.append(line)
            else:
                match = self.__line_regex.match(line)
                if match:
                    key = self._match_to_key(match)
                    if key in self.__lines:
                        log.warning(f'Duplicate data in {file.name} '
                                    f'replacing [{self.__lines[key].strip()}] with [{line.strip()}]')
                    self.__lines[key] = line
                    self.__comments[key] = comments
                    comments = []
                else:
                    raise Exception(f'Could not parse "{line.strip()}" in {file.name}')
        if comments:
            self.__comments[END] = comments

    def add(self, new):
        if self._source == new._source:
            log.error('Calling twice?')
        for key, line in new.__lines.items():
            if key in self.__lines:
                if line != self.__lines[key]:
                    if self.__prefer == Prefer.OLD:
                        log.warning(f'Taking {key} from {self._source} (preferring old data over {new._source})')
                        pass  # already have the old line
                    elif self.__prefer == Prefer.NEW:
                        log.warning(f'Taking {key} from {new._source} (preferring new data over {self._source})')
                        self.__lines[key] = line
                        self.__comments[key] = new.__comments[key]
                    else:
                        raise Exception(f'Entries differ for {key} in {self._source}')
                else:
                    log.debug(f'Entries consistent for {key} in {self._source}')
            else:
                self.__lines[key] = line
                self.__comments[key] = new.__comments[key]

    def _sorted_items(self):
        # this returns (key, lines) where lines includes preceding comments
        # list() avoids errors on deletion (mutation)
        if not self.__sort:
            prev_comments = []
            for key in list(self.__lines.keys()):
                if key in self.__comments:
                    lines = list(self.__comments[key])  # copy so we don't mutate when appending line!
                    if lines == prev_comments:
                        log.debug(f'Skipping duplicate comments in {self._file}')
                        lines = []
                    elif lines:
                        prev_comments = list(lines)
                else:
                    lines = []
                lines.append(self.__lines[key])
                yield key, lines
        else:
            if self.__comments:
                log.warning(f'Dropping comments since entries are sorted ({self._source})')
            for key in list(self.__sorted_keys()):
                yield key, [self.__lines[key]]

    def __sorted_keys(self):
        for mapped, raw in sorted([(self.__map_key(key), key) for key in self.__lines.keys()],
                                  key=lambda pair: pair[0]):
            yield raw

    def __map_key(self, key):
        mapped_key = []
        components = key.split('.')
        for letter in self.__sort:
            try:
                index = self.KEY.index(letter)
                mapped_key.append(components[index])
            except ValueError:
                pass  # not in KEY
        return mapped_key

    def _write(self, file):
        for key, lines in self._sorted_items():
            for line in lines:
                file.write(line)

    def delete(self, pattern, force=False):
        for key, lines in self._sorted_items():
            if pattern.test(key, quiet=True):
                self._print_deletion(lines)
                if force:
                    del self.__lines[key]
                    del self.__comments[key]
        self._end_deletions()


class NSCL(RegexParser):
    '''
    Selection uses net, sta, chan and loc.
    '''

    KEY = 'NSCL'

    def _match_to_key(self, match):
        return f'{match.group("net")}.{match.group("sta")}.{match.group("chan")}.{match.group("loc")}'


class NSC(RegexParser):
    '''
    Selection uses net, sta and chan.
    '''

    KEY = 'NSC'

    def _match_to_key(self, match):
        return f'{match.group("net")}.{match.group("sta")}.{match.group("chan")}'


class NS(RegexParser):
    '''
    Selection uses net and sta.
    '''

    KEY = 'NS'

    def _match_to_key(self, match):
        return f'{match.group("net")}.{match.group("sta")}'


class BINDER(RegexParser):
    '''
    Select grdlat or grdlon.
    '''

    KEY = 'BINDER'

    def _match_to_key(self, match):
        coord_type = match.group("coord_type")
        return (self._source, coord_type)


SNC_prefix_trailing_L = compile(r'^\s*(?P<sta>[A-Z0-9]+)\s+(?P<net>[A-Z0-9]+)\s+(?P<chan>[A-Z0-9]+)\s+.*(?P<loc>(?:[A-Z0-9]{2}|--))$')
SCNL_after_2 = compile(r'^\s*\d+\s+\d+\s+(?P<sta>[A-Z0-9]+)\s+(?P<chan>[A-Z0-9]+)\s+(?P<net>[A-Z0-9]+)\s+(?P<loc>(?:[A-Z0-9]+|--))\s+')
NS_after_Stream =  compile(r'^\s*Stream\s*(?P<net>[A-Z0-9]+)_(?P<sta>[A-Z0-9]+)\s+')
SCNL_after_TrigStation = compile(r'^\s*TrigStation\s+(?P<sta>[A-Z0-9]+)\s+(?P<chan>[A-Z0-9]+)\s+(?P<net>[A-Z0-9]+)\s+(?P<loc>(?:[A-Z0-9]+|--))')
SCNL_after_station = compile(r'^\s*station\s+(?P<sta>[A-Z0-9]+)\s+(?P<chan>[A-Z0-9]+)\s+(?P<net>[A-Z0-9]+)\s+(?P<loc>(?:[A-Z0-9]+|--))')
SCNL_after_Send_scnl = compile(r'^\s*Send_scnl\s+(?P<sta>[A-Z0-9]+)\s+(?P<chan>[A-Z0-9]+)\s+(?P<net>[A-Z0-9]+)\s+(?P<loc>(?:[A-Z0-9]+|--))')
SCNL_after_Tank = compile(r'^\s*Tank\s+(?P<sta>[A-Z0-9]+)\s+(?P<chan>[A-Z0-9]+)\s+(?P<net>[A-Z0-9]+)\s+(?P<loc>(?:[A-Z0-9]+|--))')
SCNL_after_GetSCNL = compile(r'^\s*GetSCNL\s+(?P<sta>[A-Z0-9]+)\s+(?P<chan>[A-Z0-9]+)\s+(?P<net>[A-Z0-9]+)\s+(?P<loc>(?:[A-Z0-9]+|--))')
SNCL = compile(r'^\s*(?P<sta>[A-Z0-9]+)\s+(?P<net>[A-Z0-9]+)\s+(?P<chan>[A-Z0-9]+)\s+(?P<loc>(?:[A-Z0-9]{2}|--))')

binder_grid_coord_min_max = compile(r'^\s*(?P<coord_type>(grdlat|grdlon))\s+.*')


class HinvSta(NSCL):

    TYPE = 'hinv_sta.d'

    def _initial_comments(self, comment):
        return []

    def __init__(self, file, prefer, sort, source):
        super().__init__(SNC_prefix_trailing_L, file, prefer, sort, source)


class PickSta(NSCL):

    TYPE = 'pick_sta.d'

    def __init__(self, file, prefer, sort, source):
        super().__init__(SCNL_after_2, file, prefer, sort, source)


class SlinkImports(NS):
    '''
    Old code, no longer used.  File contents are themselves patterns and must be applied to the NSCLS.
    See new code in slink.py
    '''

    TYPE = 'slink_imports.d'

    def __init__(self, file, prefer, sort, source):
        super().__init__(NS_after_Stream, file, prefer, sort, source)


class TrigSta(NSCL):

    TYPE = 'trigsta.scnl'

    def __init__(self, file, prefer, sort, source):
        super().__init__(SCNL_after_TrigStation, file, prefer, sort, source)


class Tbuf2Mseed(NSCL):

    TYPE = 'tbuf2mseed.d'

    def __init__(self, file, prefer, sort, source):
        super().__init__(SCNL_after_Send_scnl, file, prefer, sort, source)


class CarlSta(NSCL):

    TYPE = 'carlsta.scnl'

    def __init__(self, file, prefer, sort, source):
        super().__init__(SCNL_after_station, file, prefer, sort, source)

    def _write(self, file):
        for key, lines in self._sorted_items():
            net, sta, chan, loc = key.split('.')
            if not chan.endswith('Z'):
                log.warning(f'Some carlsta data contains non-Z channels')
            for line in lines:
                file.write(line)


class Fir(NSCL):

    TYPE = 'fir.scnl'

    def __init__(self, file, prefer, sort, source):
        super().__init__(SCNL_after_GetSCNL, file, prefer, sort, source)

    def _write(self, file):
        for key, lines in self._sorted_items():
            net, sta, chan, loc = key.split('.')
            if not chan.endswith('Z'):
                log.warning(f'Some fir data contains non-Z channels')
            for line in lines:
                file.write(line)

                
class BinderGrid(BINDER):
    ''' Handle Binder grid files.

    This parser just copies the content of all 
    binder_grid.d files into one. This doesn't make sense, 
    but it is used to avoid warnings, that no parser for binder_grid.d 
    files is available.
    The actual computation of the grid file for all merged stations
    is done in merge.binder.compute_binder_grid called by ewmerge.py.
    '''
    
    TYPE = 'binder_grid.d'

    def __init__(self, file, prefer, sort, source):
        super().__init__(binder_grid_coord_min_max, file, prefer, sort, source)

    def _write(self, file):
        for key, lines in self._sorted_items():
            for line in lines:
                file.write(line)


class WsvChanList(NSCL):

    TYPE = 'wsv_chan_list.d'

    def __init__(self, file, prefer, sort, source):
        super().__init__(SCNL_after_Tank, file, prefer, sort, source)


class StaList(NSCL):

    TYPE = 'stalist.txt'

    def __init__(self, file, prefer, sort, source):
        # always sorted
        super().__init__(SNCL, file, prefer, 'SNCL', source)


PARSERS[HinvSta.TYPE] = HinvSta
PARSERS['pick_FP_sta.d'] = PickSta
PARSERS[PickSta.TYPE] = PickSta
PARSERS[SlinkImports.TYPE] = SlinkImports
PARSERS[TrigSta.TYPE] = TrigSta
PARSERS[Tbuf2Mseed.TYPE] = Tbuf2Mseed
PARSERS[WsvChanList.TYPE] = WsvChanList
PARSERS[CarlSta.TYPE] = CarlSta
PARSERS[Fir.TYPE] = Fir
PARSERS[StaList.TYPE] = StaList
PARSERS[BinderGrid.TYPE] = BinderGrid


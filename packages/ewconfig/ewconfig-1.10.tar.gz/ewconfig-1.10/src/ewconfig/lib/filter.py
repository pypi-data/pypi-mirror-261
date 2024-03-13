from abc import ABC, abstractmethod
from fnmatch import translate
from logging import getLogger
from re import compile

log = getLogger(__name__)


class BaseFilter(ABC):

    @abstractmethod
    def _default_includes(self):
        raise NotImplemented()

    def __init__(self, name, includes=None, excludes=None):
        self.__name = name
        if isinstance(includes, str) or isinstance(excludes, str):
            raise Exception('Filter takes lists of includes and excludes')
        if not includes: includes = self._default_includes()
        if not excludes: excludes = []
        self.__str = f'{name}: include ' + ','.join(includes)
        if excludes: self.__str += '; exclude ' + ','.join(includes)
        self.__includes = [compile(translate(include)) for include in includes]
        self.__excludes = [compile(translate(exclude)) for exclude in excludes]

    def __call__(self, items, key=None, quiet=False):
        logged = set()
        for item in items:
            if self.test(item, key=key, quiet=quiet, logged=logged):
                yield item

    def test(self, item, key=None, quiet=False, logged=None):
        if not key: key = lambda x: x
        if logged is None: logged = set()
        value = key(item)
        if any(include.match(value) for include in self.__includes):
            if not any(exclude.match(value) for exclude in self.__excludes):
                return True
            else:
                if value not in logged:
                    if not quiet: log.info(f'{self.__name} {value} was explicitly excluded')
                    logged.add(value)
        else:
            if value not in logged:
                if not quiet: log.info(f'{self.__name} {value} was not included')
                logged.add(value)
        return False

    def __str__(self):
        return self.__str


class Filter(BaseFilter):
    """
    A filter for <name> that includes patterns in <includes>
    and then excludes patterns in <excludes>.
    If <includes> is missing then all are initially included.
    If <excludes> is missing then none are excluded.
    Patterns are 'globs' as supported by fnmatch module.
    """

    def _default_includes(self):
        return ['*']


class DottedFilter(BaseFilter):
    """
    Create a filter for <name> that includes patterns in <includes>
    and then excludes patterns in <excludes>.
    If <includes> is missing then none are initially included (differs from Filter)
    If <excludes> is missing then none are excluded.
    Patterns are 'globs' as supported by fnmatch module, but unlike Filter they can contain
    multiple components separated by dots.  When matching (possibly right-incomplete) NSCLs
    the number of components must match.  (In practice these are just characters!  No special
    processing is necessary!)
    """

    def _check_dots(self, pattern):
        # this shouldn't happen when called from the command line because it's verified by the type
        n = pattern.count('.')
        if n not in (1, 3):
            log.warning(f'The pattern {pattern} does not contain 2 or 4 dotted names (N.S or N.S.C.L) so will not be used')

    def __init__(self, name, includes=None, excludes=None):
        if includes:
            for include in includes:
                self._check_dots(include)
        if excludes:
            for exclude in excludes:
                self._check_dots(exclude)
        super().__init__(name, includes=includes, excludes=excludes)

    def _default_includes(self):
        return []

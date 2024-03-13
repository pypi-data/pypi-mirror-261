from argparse import ArgumentParser
from logging import getLogger
from os import mkdir
from os.path import exists
from shutil import copytree

from ewconfig.prune.response import delete_response
from ewconfig.prune.sacp import delete_sacp
from ewconfig.prune.xml import delete_xml
from .lib.args import add_version_args, ParagraphHelpFormatter
from .lib.file import assert_dir
from .lib.filter import DottedFilter
from .lib.log import add_log_args, make_log_from_args
from .lib.markdown import add_md_help_argument
from .merge.chan import ls_chan, PARSERS

log = getLogger(__name__)


def _prepare_dirs(old_dir, force, pruned, backup):
    if force:
        if (not pruned and not backup) or (pruned and backup):
            raise Exception('Provide exactly one of --pruned or --backup with --force')
        if pruned and exists(pruned):
            raise Exception(f'--pruned {pruned} already exists')
        if backup and backup != 'NONE' and exists(backup):
            raise Exception(f'--backup {backup} already exists')
    else:
        if pruned or backup:
            log.warning(f'No output until --force used (ignoring --pruned and --backup)')
    if force:
        if pruned:
            copytree(old_dir, pruned)
            return pruned
        else:  # backup
            if backup == 'NONE':
                log.warning(f'Mutating contents of {old_dir} with no backup')
            else:
                copytree(old_dir, backup)
                log.info(f'Backup in {backup}')
            return old_dir
    else:
        log.warning(f'Dry run - no output (use --force to change)')
        return old_dir


def main(old_dir, filter=DottedFilter('Pattern'), force=False, pruned=None, backup=None):
    dir = _prepare_dirs(old_dir, force, pruned, backup)
    log.debug(f'Working directory is {dir}')
    for file in ls_chan(dir):
        if file in PARSERS:
            Parser = PARSERS[file]
            log.debug(f'Parsing {file} with {Parser}')
            parser = Parser(file, None, False, file)
            parser.read(dir)
            parser.delete(filter, force=force)
            if force:
                parser.write(dir)
        else:
            log.warning(f'Ignoring {file}')
    delete_sacp(dir, filter, force=force)
    delete_response(dir, filter, force=force)
    delete_xml(dir, filter, force=force)
    return dir


def dotted(pattern):
    n = pattern.count('.')
    if n not in (1, 3):
        raise Exception(f'The pattern {pattern} does not contain 2 or 4 dotted names (N.S or N.S.C.L) so will not be used')
    return pattern


def main_args():
    try:
        parser = ArgumentParser(prog='ewprune', add_help=False,
                                formatter_class=ParagraphHelpFormatter,
                                description="""A tool remove specific sources from an EW configuration.
                                
To do this, sources are matched against patterns.  
Patterns are dotted components that can contain *, ? (wildcards), [...] and [!...] (alternatives).
Patterns only match NSCLs if the number of components matches.
So the pattern '*.*.HN[NE].*' will match CI.PASC.HNN.10 for example, but will not match CI.PASC 
(without channel or location).
Multiple patterns can be specified and sources are only deleted if they match a pattern in `--delete` 
and do not match a pattern in `--keep`.

This may seem cumbersome, but seems to be the only approach that gives complete control.

By default the sources to be deleted are displayed (only).
To actually force deletion you must add `--force`.

If --pruned is given, the new, pruned config is placed in that directory.

If --pruned is not given, the pruned config replaces the contents of the --dir directory.  
In this case --backup (which will contain the original contents of --dir) must be given.  
If you really don't want a backup use "--backup NONE".

Examples

To delete all mention of the CI.PASC station (both N.S and N.S.C.L entries in various files):

ewprune DIR --delete CI.PASC CI.PASC.*.* --backup ...

To remove all HHZ channels 

ewprune DIR --delete *.*.HHZ.* --backup ... 

Note that in the example above N.S entries will remain, so if station NET.XXX had only HHZ then that must 
also be explicitly deleted:

ewprune DIR --delete *.*.HHZ.* NET.XXX --backup ... 

Alternatively, maybe we know that only NET.YYY had alternative channels, 
so we can delete all N.S entries except that:

ewprune DIR --delete *.*.HHZ.* *.* --keep NET.YYY --backup ... 
""")
        parser.add_argument('dir', metavar='DIR', type=assert_dir,
                            help='Directory containing the configuration')
        parser.add_argument('--delete', metavar='PATTERN', type=dotted, nargs='+', help='Patterns to delete')
        parser.add_argument('--keep', metavar='PATTERN', type=dotted, nargs='+', help='Patterns to keep')
        parser.add_argument('--force', action='store_true', help='Force deletion')
        parser.add_argument('--pruned', help='Destination directory for pruned config.')
        parser.add_argument('--backup', help='Backup directory for original config (if no --pruned; can be NONE).')
        parser.add_argument('-h', action='help', help='Show this help message and exit.')
        add_version_args(parser)
        add_md_help_argument(parser)
        add_log_args(parser)
        args = parser.parse_args()
        make_log_from_args(parser.prog, args)
        main(args.dir, filter=DottedFilter('Pattern', includes=args.delete, excludes=args.keep),
             force=args.force, pruned=args.pruned, backup=args.backup)
    except Exception as e:
        log.critical(e)
        exit(1)


if __name__ == '__main__':
    main_args()

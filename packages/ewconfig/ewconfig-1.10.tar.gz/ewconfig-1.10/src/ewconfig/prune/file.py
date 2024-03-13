from os import unlink


def delete_file(paths, pattern, parse_path, name, force=False):
    deleted = False
    for path in paths:
        nscl, file = parse_path(path)
        if pattern.test(nscl, quiet=True):
            if not deleted:
                print('DELETIONS:')
                deleted = True
            print('  ', file)
            if force:
                unlink(path)
    if not deleted:
        print(f'UNCHANGED {name}')

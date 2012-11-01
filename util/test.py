import os

__RSYNC_DIR__ = '.rsync'
__VERSION_F__ = '.version.txt'

class ValidationException(Exception):
    pass

def _validate_mod_path(path):
    if not os.path.isdir(path):
        raise ValidationException('Supplied path is not a directory: ' + path)
    try:
        rsync_dir = filter(lambda x: x == __RSYNC_DIR__, os.listdir(path))
        version_file = filter(lambda x: x == __VERSION_F__, os.listdir(path))

        '''
        If there's an rsync directory, then we need to check 
        for the version and
        the dependencies within the folder.  If it's all there, 
        then we assume
        the mod is valid.  We keep track of whether the mod 
        is up to date separately
        from being valid, though a mod cannot be up to 
        date ever if it isn't valid.
        '''
        if not rsync_dir:
            raise ValidationException("No rsync folder found in directory '{0}'".format(path))
        if not version_file:
            raise ValidationException('No version file found in directory "{0}"'.format(path))

    except IOError as e:  # For now raise; we need to handle this properly.
        raise
    except:  # Raise if it's something we don't expect.
        raise

def get_mod_version(path):
    try:
        _validate_mod_path(path)
    except ValidationException:
        return None

    with open(path + "/" + __VERSION_F__, 'r') as f:
        try:
            version = int(f.readline())
        except ValueError:
            version = None
    return version

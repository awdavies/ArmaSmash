import os
from test import get_mod_version


def create_mod(name, version='1', path=os.getcwd()):
    '''
    This (not currently implemented) will create a mod at a specified
    path, then return the initialized mod after it has been created.
    '''
    pass

class Mod():
    '''
    A mod is a high level representation of a
    module for Arma 2.  A mod contains a path.  From
    there it finds out its version and its dependencies
    so long as the path exists.

    Requirements:

    @param: path -- A valid path to a mod.  For now a valid path must be
                  a directory, and it must contain a file '.version.txt'
                  and '.rsync' directory (more constraints coming soon!)
    '''

    class InvalidException(Exception):
        '''
        An exception thrown when a mod is not valid, and any methods
        have not been called.
        '''
        pass

    def __init__(self, path):
        self.path = path
        self.update_info()
        (self.root, self.name) = os.path.split(path)

    def update_info(self):
        version = get_mod_version(self.path)
        if version is not None:
            self.version = version
        else:
            raise Mod.InvalidException("Mod folder invalid!")

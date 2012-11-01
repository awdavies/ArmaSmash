import wx # for if we so choose to force the user to pick the install loc.
import os
import settings

def check_arma_dir():
    '''
    If the directory file for the arma installation exists, then
    open the file up.  If we can't, for now we just fail silently.

    If the directory in the text file is corrupted or is not a directory,
    again, we fail silently.

    TODO: Decide whether any of this should simply be punted to the user
    or if some sort of error message should be displayed (likely the
    latter).
    '''
    dir_file = filter(
            lambda x: x == settings.ARMA_DIR_FILE, 
            os.listdir(settings.INSTALL_DIR),
    )
    if dir_file:
        try:
            dir_file = "{0}/{1}".format(
                settings.INSTALL_DIR, 
                settings.ARMA_DIR_FILE,
            )
            with open(dir_file, 'r') as f:
                line = f.readline().strip()
                if os.path.isdir(line):
                    settings.ARMA_DIR = line
        except:
            pass # for now, fail silently.

check_arma_dir()

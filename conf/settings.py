'''
This file contains global settings.
'''

# By default, this is the directory in which we look.
# this should not be changed manually, as we check to see if the
# arma directory file exists (this contains the location of the arma
# mod directory when running __init__.py).  
# If the file doesn't exist, this stays as default
# and can be changed later by the user using one of the menu commands
#
# TODO: Should we have the user figure this out, or should we try to
# force them to specify upon starting?  Furhermore, if they have
# windows, should we try to check the registry values for the default
# arma 2/operation arrowhead directories?
#
ARMA_DIR = "."

# This is the location of the arma 2 directory file.  This is where
# we will look when attempting to find the arma_dir.txt file which
# contains the saved arma2 directory.
#
# TODO: Again, if this program is installed on windows, or as a package,
# this might need to be checked in order to make sure the file
# is stored in the correct location.
INSTALL_DIR = "."

# This is the file that contains the center of the arma installation dir.
# from here we'll load this up (if possible).
ARMA_DIR_FILE = "arma_dir.txt"

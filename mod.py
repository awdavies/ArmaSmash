import os

__RSYNC_FOLDER__ = '.rsync'
__VERSION_FILE__ = '.version.txt'

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

  Because of the current implementation, a mod is not
  valid unless it contains some form of version data, so
  an empty folder will not suffice for a valid mod.

  A mod is capable of verifying itself based on the mod
  format (the implementation of which may change later).
  '''

  def __init__(self, path):
    self.path = path
    self.valid = False
    self._init_rsync_data()

  def _init_rsync_data(self):
    if not os.path.isdir(self.path):
      raise Exception('Supplied path is not a directory: ' + self.path)
    try:
      rsync_dir = filter(lambda x: x == __RSYNC_FOLDER__, os.listdir(self.path))
      version_file = filter(lambda x: x == __VERSION_FILE__, os.listdir(self.path))

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
        raise Exception("No rsync folder found in directory '{0}'".format(self.path))
      if not version_file:
        raise Exception('No version file found in directory "{0}"'.format(self.path))
    except IOError as e:  # For now pass, but we need to handle this properly.
      raise
    except:  # Raise if it's something we don't expect.
      raise

import os

__RSYNC_DIR__ = '.rsync'
__VERSION_F__ = '.version.txt'

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

    if not os.path.isdir(self.path):
      raise Exception('Supplied path is not a directory: ' + path)
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
        raise Exception("No rsync folder found in directory '{0}'".format(path))
      if not version_file:
        raise Exception('No version file found in directory "{0}"'.format(path))
    except IOError as e:  # For now pass, but we need to handle this properly.
      raise
    except:  # Raise if it's something we don't expect.
      raise

    '''
    Now we have an rsync folder and a version file.  We should get
    the version of the mod and then (maybe?) verify the rsync data.
    '''

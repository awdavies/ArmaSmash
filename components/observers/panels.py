import wx
from conf import settings
from lists import ModList

class ModListPanel(wx.Panel):
    
    def __init__(self, *args, **kwargs):
        wx.Panel.__init__(self, *args, **kwargs)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        modlist = ModList(parent=self, arma_dir=settings.ARMA_DIR)
        hbox.Add(modlist, proportion=1, flag=wx.EXPAND)
        self.SetSizer(hbox)

'''
These silly functions need to be moved into their own module somwhere.
They don't belong here.  Since we're likely going to be going for some
kind of bastardized MVC setup for the file architecture, there should
probably be some kind of "controller" module, since we already have a
model class and an observers class.
'''
def _check_arma_directory(self):
    try:
      f = open(__ARMA_DIR_FILE__, "r")
      self._arma_dir = f.read()
      if not os.path.isdir(self._arma_dir):
        self.show_error('Arma directory invalid.')
        self._get_arma_dir()
    except IOError as e:
      self.show_error('Arma directory not found.')
      self._get_arma_dir()

def show_error(self, msg):
  '''
  Simply lets the user know of an error that occurred.
  Perhaps this should be a more global message, since there
  are likely going to be all manner of errors occuring.
  '''
  dial = wx.MessageDialog(self, msg, 'Error', wx.OK | wx.ICON_ERROR)
  dial.ShowModal()

def _get_arma_dir(self):
    '''
    Gets the arma directory from the supplied folder path.
    TODO: We should probably have some sort of registry read in
    to check to see if the file exists.

    Moreover, if there aren't any binaries in there (or the binaries
    have had their names changed) there won't be a way to, say, start
    the server, or do something like run the game itself.  We should
    check to see if there are the appropriate binaries at some point
    and fail somehow if they don't exist (or maybe ask if they simply
    want to have this directory act as a mod cache if they're partitioning
    things?)

    This could (should) all go on the github issue tracker at some point.

    However!  For now, we're going to simply treat the folder supplied as
    a mod cache.  We're going to be a complete jerk to the user and
    assume that they just want to install mods to any random directory.
    Later, however, we should add in some more functionality to see if 
    this is, indeed, a proper arma 2 installation.
    '''
    dial = wx.DirDialog(self, \
                        'Select the directory of your Arma 2 installation', \
                        '.', \
                        wx.DD_DIR_MUST_EXIST)
    dial.ShowModal()
    self._arma_dir = dial.GetPath()

#  Essentially, if they choose nothing, we'll just kill the program.
    if self._arma_dir == '':
      self.show_error('Empty Directory.  Exiting...')
      self.on_quit()

#  If we're here, then write out the directory to the appropriate file
    try:
      f = open(__ARMA_DIR_FILE__, 'w')
      f.write(self._arma_dir)
    except IOError as e:
      '''
      Don't do anything.  We'll just punt it to the user and have them
      deal with it.
      '''
      self.show_error("I/O error({0}): {1}".format(e.errno, e.strerror))
      return


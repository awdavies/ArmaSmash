import wx
import os

# TODO: Put this into a global module section.
__ARMA_DIR_FILE__ = "./arma_dir.txt"

[wxID_MAIN_WINDOW] = [wx.NewId() for _init_ctrls in range(1)]

class MainWindow(wx.Frame):
  '''
  This is, as the name implies, the main window.  This holds all of
  the subcomponents needed by the window.
  '''
  def __init__(self, parent):
    self._arma_dir = ''
    self._init_components(parent)
    self._CheckArmaDir()

  def _init_components(self, prnt):
    '''
    Initializes all of the components of the window (including any
    major subcomponents.
    '''
    super(MainWindow, self).__init__(style=wx.DEFAULT_FRAME_STYLE, \
                      name='', parent=prnt, title='ArmaSmash', \
                      pos=(320, 175), size=(853,467))
    menuBar = wx.MenuBar()
    fileMenu = wx.Menu()
    fitem = fileMenu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
    menuBar.Append(fileMenu, '&File')
    self.SetMenuBar(menuBar)
    self.Bind(wx.EVT_MENU, self.OnQuit, fitem)

  def _CheckArmaDir(self):
    try:
      f = open(__ARMA_DIR_FILE__, "r")
      self._arma_dir = f.read()
      if not os.path.isdir(self._arma_dir):
        self.ShowError('Arma directory invalid.')
        self._GetArmaDir()
    except IOError as e:
      self.ShowError('Arma directory file not found.')
      self._GetArmaDir()

  def ShowError(self, msg):
      '''
      Simply lets the user know of an error that occurred.
      Perhaps this should be a more global message, since there
      are likely going to be all manner of errors occuring.
      '''
      dial = wx.MessageDialog(self, msg, 'Error', wx.OK | wx.ICON_ERROR)
      dial.ShowModal()
  
  def _GetArmaDir(self):
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

    #  Essentially, if they've hit cancel, we'll just kill the program.
    if self._arma_dir == '':
      self.ShowError('Empty Directory.  Exiting...')
      self.OnExit()

    #  If we're here, then write out the directory to the appropriate file
    try:
      f = open(__ARMA_DIR_FILE__, 'w')
      f.write(self._arma_dir)
    except IOError as e:
      '''
      Don't do anything.  We'll just punt it to the user and have them
      deal with it.
      '''
      self.ShowError("I/O error({0}): {1}".format(e.errno, e.strerror))
      return

  def ReadArmaDir(self):
    '''
    This reads in the arma dir and creates the list of valid mod folders
    that will then be displayed in the mod list on the main tab 
    (coming.... eventually!)  Right now this does nothing.
    '''
    try:
      f = open(self._arma_dir, 'r')
    except IOError as e:
      self.ShowError("I/O error({0}): {1}".format(e.errno, e.strerror))
      self.OnExit()

  def OnQuit(self, e):
    self.Close()

import wx

def create(parent):
  return MainWindow(parent)

[wxID_MAIN_WINDOW] = [wx.NewId() for _init_ctrls in range(1)]

class MainWindow(wx.Frame):
  '''
  This is, as the name implies, the main window.  This holds all of
  the subcomponents needed by the window.
  '''
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

  def __init__(self, parent):
    self._init_components(parent)

  def OnQuit(self, e):
    self.Close()

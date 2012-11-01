import wx
import os
from components.observers.panels import ModListPanel

class MainWindow(wx.Frame):
  '''
  This is, as the name implies, the main window.  This holds all of
  the subcomponents needed by the window.
  '''
  def __init__(self, parent):
    self._arma_dir = ''
    self._init_components(parent)

  def _init_components(self, prnt):
    '''
    Initializes all of the components of the window (including any
    major subcomponents).
    '''
    super(MainWindow, self).__init__(style=wx.DEFAULT_FRAME_STYLE, \
                      name='', \
                      parent=prnt, \
                      title='ArmaSmash', \
                      pos=(320, 175), \
                      size=(853,467))

    ''' Init Menu '''
    menu_bar = wx.MenuBar()
    file_menu = wx.Menu()
    fitem = file_menu.Append(wx.ID_EXIT, 'Quit', 'Quit application')
    menu_bar.Append(file_menu, '&File')
    self.SetMenuBar(menu_bar)
    self.Bind(wx.EVT_MENU, self.on_quit, fitem)

    ''' Mod List Panel '''
    self.mod_list_panel = ModListPanel(self, -1)
  
  def on_quit(self, e):
    self.Close()

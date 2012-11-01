import wx
import os
import time
from components.models import Mod
import conf.settings

class ModList(wx.ListCtrl):
  def __init__(self, parent, arma_dir):
    wx.ListCtrl.__init__(self, parent, style=wx.LC_REPORT)

    ''' 
    For now, just list the elements within the mods folder so
    we can see them.  In the future, we'll simply supply a 
    list of mods that have been created by one of the other
    modules.
    '''
    mod_paths = os.listdir(arma_dir)
    mod_paths = [arma_dir + "/" + mod_path for mod_path in mod_paths]

    self.InsertColumn(0, 'Name')
    self.InsertColumn(1, 'Version')
    self.InsertColumn(2, 'Modified')

    '''
    These numbers are abritrary.  Maybe change them later...
    '''
    self.SetColumnWidth(0, 220)
    self.SetColumnWidth(1, 70)
    self.SetColumnWidth(2, 100)
    self.SetColumnWidth(3, 420)

    i = 0
    for mod_path in mod_paths:
        try:
            mod = Mod(mod_path)
        except Mod.InvalidException:
            continue
        sec = os.path.getmtime(mod.path)
        self.InsertStringItem(i, mod.name)
        self.SetStringItem(i, 1, unicode(mod.version)) 
        self.SetStringItem(i, 2, time.strftime('%Y-%m-%d %H:%M', 
                           time.localtime(sec)))

        if (i % 2) == 0:
            self.SetItemBackgroundColour(i, '#e6f1f5')
        i = i + 1


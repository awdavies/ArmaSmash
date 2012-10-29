import wx
import os
import time
import mod

class ModList(wx.ListCtrl):
  def __init__(self, parent, id, arma_dir):
    wx.ListCtrl.__init__(self, parent, id, style=wx.LC_REPORT)

    ''' 
    For now, just list the elements within the mods folder so
    we can see them.
    '''
    mods = os.listdir(arma_dir)
    mods = [arma_dir + "/" + mod for mod in mods]

    self.InsertColumn(0, 'Name')
    self.InsertColumn(1, 'Version')
    self.InsertColumn(2, 'Size', wx.LIST_FORMAT_RIGHT)
    self.InsertColumn(3, 'Modified')

    '''
    These numbers are abritrary.  Maybe change them later...
    '''
    self.SetColumnWidth(0, 220)
    self.SetColumnWidth(1, 70)
    self.SetColumnWidth(2, 100)
    self.SetColumnWidth(3, 420)

    i = 0
    for mod in mods:
      (path, name) = os.path.split(mod)
      size = os.path.getsize(mod)
      sec = os.path.getmtime(mod)
      self.InsertStringItem(i, name)
      self.SetStringItem(i, 1, 'v0.001') # all the same version!  ahahaha.
      self.SetStringItem(i, 2, str(size) + ' B')
      self.SetStringItem(i, 3, time.strftime('%Y-%m-%d %H:%M', 
                         time.localtime(sec)))

      if (i % 2) == 0:
        self.SetItemBackgroundColour(i, '#e6f1f5')
      i = i + 1

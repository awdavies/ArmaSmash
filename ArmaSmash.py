import wx
import MainWindow
modules= {u'MainWindow': [1, 'Main window', 'MainWindow.py']}

class ArmaSmash(wx.App):
  '''
  The main class!  This handles all the goods.
  '''
  def OnInit(self):
    self.main = MainWindow.MainWindow(None)
    self.main.Centre()
    self.main.Show(1)
    self.SetTopWindow(self.main)
    return True

def main():
  app = ArmaSmash(0)
  app.MainLoop()

if __name__ == '__main__':
  main()

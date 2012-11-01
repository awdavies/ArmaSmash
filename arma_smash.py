import wx
import main_window

class ArmaSmash(wx.App):
  '''
  The main class!  This handles all the goods.
  '''
  def OnInit(self):
    self.main = main_window.MainWindow(None)
    self.main.Centre()
    self.main.Show(1)
    self.SetTopWindow(self.main)
    return True

def main():
  app = ArmaSmash(0)
  app.MainLoop()

if __name__ == '__main__':
  main()

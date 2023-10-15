import wx
from frames.main_frame import MainFrame

if __name__ == '__main__':
    app = wx.App()
    frame = MainFrame()
    frame.Show()
    app.MainLoop()
    
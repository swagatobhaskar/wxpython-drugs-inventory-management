import wx

class ProductsWindow(wx.Frame):
    def __init__(self, parent):
        super().__init__(parent, title='ABC Drugs | Products')

        self.SetBackgroundColour(wx.Colour('Magenta'))
        # add notebook widget

        self.Center()
        self.Show()
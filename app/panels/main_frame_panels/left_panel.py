import wx

class LeftPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, style=wx.BORDER_SIMPLE)

        # Add and display the image
        imgFilePath= 'app/media/images/pharma-product.jpg'
        img = wx.Image(imgFilePath, wx.BITMAP_TYPE_ANY)#.ConvertToBitmap()
        img = img.Scale(300, 600, wx.IMAGE_QUALITY_BOX_AVERAGE)
        img_bitmap = wx.Bitmap(img)
        # self.bitmap = wx.StaticBitmap(left_img_panel, wx.ID_ANY, img_bitmap)
        self.bitmap = wx.StaticBitmap(self, wx.ID_ANY, img_bitmap)

        # self.Layout()
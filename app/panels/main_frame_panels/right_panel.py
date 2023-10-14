import wx

class RightPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, style=wx.BORDER_SIMPLE)

        self.SetBackgroundColour('#f8f8ff')

        # main vertical sizer for this panel   
        self.vbox_main = wx.BoxSizer(wx.VERTICAL)
        # Sizers for contact info, auth form
        self.vbox_contact = wx.BoxSizer(wx.VERTICAL)

        org_name = wx.StaticText(self, label='ABC Pharmaceuticals Wholesale')
        font = org_name.GetFont()
        font.PointSize += 14
        font = font.Bold()
        org_name.SetFont(font)

        address = """66B, Tower Street\nOld Water Park,\nXYZ City, 123456\nContact: +91 1234 8899"""
        address_label = wx.StaticText(self, label=address)
            
        self.vbox_contact.Add(org_name, 0, wx.BOTTOM | wx.ALIGN_LEFT, 5)
        self.vbox_contact.Add(address_label, 0, wx.TOP | wx.BOTTOM | wx.ALIGN_LEFT, 5)
        
        # Create two buttons: Login and Add user
        self.hbox_btns = wx.BoxSizer(wx.HORIZONTAL)
        login_btn = wx.Button(self, label="Login")
        add_user_btn = wx.Button(self, label="Add User")
        login_btn.Bind(wx.EVT_BUTTON, self.handleLogin)
        add_user_btn.Bind(wx.EVT_BUTTON, self.handleSignup, add_user_btn)

        self.hbox_btns.Add(login_btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)
        self.hbox_btns.Add(add_user_btn, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 10)
        
        self.vbox_main.Add(self.vbox_contact, 0, wx.EXPAND | wx.ALL, 10)
        self.vbox_main.Add(self.hbox_btns, 0, wx.EXPAND | wx.ALL | wx.ALIGN_CENTER, 10)

        #---------------------------------------------------------------------
        """Field to appear containing user info after a user logs in."""
        for child in self.hbox_btns.GetChildren():
            # remove the auth buttons
            print("Childs:: ", child)

        self.SetSizer(self.vbox_main)

        # self.SetAutoLayout(True)
        # self.Layout()
        
    def handleLogin(self, event):
        # open form in a popup dialog
        wx.MessageBox("Feature not ready!")

    def handleSignup(self, event):
        # open form in a popup dialog
        wx.MessageBox("Feature not ready!")

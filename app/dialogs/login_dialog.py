import wx
from pubsub import pub

class LoginDialog(wx.Dialog):
    def __init__(self):
        super().__init__(None, title='Employee Login',
                         size=(400, 300), style=wx.DEFAULT_DIALOG_STYLE
                         )
        
        self.InitFormUI()
        self.Center()
        
    def InitFormUI(self):
        # vertical sizer for email and password input
        self.vbox_inputs = wx.BoxSizer(wx.VERTICAL)

        # horizontal sizer for email label and email input
        self.hbox_email = wx.BoxSizer(wx.HORIZONTAL)
        emp_email_lbl = wx.StaticText(self, label="Email:")
        emp_email_input = wx.TextCtrl(self)
        self.hbox_email.AddMany([
            (emp_email_lbl),
            (emp_email_input)
            ])
        
        # horizontal sizer for password label and input
        self.hbox_password = wx.BoxSizer(wx.HORIZONTAL)
        emp_password_lbl = wx.StaticText(self, label="Password:")
        emp_password_input = wx.TextCtrl(self)
        self.hbox_password.AddMany([
            (emp_password_lbl),
            (emp_password_input)
            ])
        
        # Horizontal sizer for buttons
        self.hbox_btns = wx.BoxSizer(wx.HORIZONTAL)
        cancel_btn = wx.Button(self, label='Cancel')
        cancel_btn.Bind(wx.EVT_BUTTON, self.handleCancel)
        submit_btn = wx.Button(self, label='Submit')
        submit_btn.Bind(wx.EVT_BUTTON, self.handleLogin)
        self.hbox_btns.AddMany([
            (cancel_btn),
            (submit_btn)
            ])
        
        self.hline = wx.StaticLine(self, -1, (25, 50), (300,1))
        
        help_lbl = """
        New Employee! Please wait until your credentials are added to the database.\n
        You will be able to Login after that. Sorry for the inconvenience!
        """
        self.help_txt = wx.StaticText(self, label=help_lbl)
        
        # add the email, password, buttons horizontal sizers to the vbox_input sizer
        self.vbox_inputs.AddMany([
             (self.hbox_email),
             (self.hbox_password),
             (self.hbox_btns),
             (self.hline),
             (self.help_txt)
            ])

        self.SetSizer(self.vbox_inputs)

    def handleLogin(self, event):
        pass        

    def handleCancel(self, event):
        self.Destroy()

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
        emp_email_input = wx.TextCtrl(self, size=(220, 20)) # size=(width, height)

        self.hbox_email.AddMany([
            (emp_email_lbl, 1, wx.ALL, 1),
            (emp_email_input, 1, wx.EXPAND | wx.ALL, 1)
            ])
        
        # horizontal sizer for password label and input
        self.hbox_password = wx.BoxSizer(wx.HORIZONTAL)
        emp_password_lbl = wx.StaticText(self, label="Password:")
        emp_password_input = wx.TextCtrl(self, size=(220, 20),
                                         style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER
                                         )

        self.hbox_password.AddMany([
            (emp_password_lbl, 1, wx.ALL, 1),
            (emp_password_input, 1, wx.EXPAND, 1)
            ])
        
        # email & password sizer
        self.hbox_email_password = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox_email_password.AddMany([
            (self.hbox_email, 1, wx.EXPAND | wx.ALL, 5),
            (self.hbox_password, 1, wx.EXPAND | wx.ALL, 5)
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
             (self.hbox_email_password),
             (self.hbox_btns),
             (self.hline),
             (self.help_txt)
            ])

        self.SetSizer(self.vbox_inputs)

    def handleLogin(self, event):
        pub.sendMessage("loggedin_listener", message='true')
        self.Destroy()      

    def handleCancel(self, event):
        self.Destroy()

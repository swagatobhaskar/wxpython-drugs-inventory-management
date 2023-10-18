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
        #------------------------------------------------------------------
        # font = wx.SystemSettings.GetFont(wx.SYS_SYSTEM_FONT)
        # font.SetPointSize(9)

        # define the widgets
        emp_email_lbl = wx.StaticText(self, label="Email:")
        emp_email_input = wx.TextCtrl(self, size=(220, 20)) # size=(width, height)
        # emp_email_input.SetFont(font)

        # horizontal sizer for password label and input        
        emp_password_lbl = wx.StaticText(self, label="Password:")
        emp_password_input = wx.TextCtrl(self, size=(220, 20),
                                         style=wx.TE_PASSWORD|wx.TE_PROCESS_ENTER
                                         )
        
        cancel_btn = wx.Button(self, label='Cancel')
        cancel_btn.Bind(wx.EVT_BUTTON, self.handleCancel)
        submit_btn = wx.Button(self, label='Submit')
        submit_btn.Bind(wx.EVT_BUTTON, self.handleLogin)

        self.hline = wx.StaticLine(self, pos=(0, 50), size=(400, 1))
        
        help_lbl = """
        New Employee!
        Please wait until your credentials are added to the database.
        You will be able to Login after that.
        Sorry for the inconvenience!
        """
        self.help_txt = wx.StaticText(self, label=help_lbl)

        #-----------------------------------------------------------------
        # Define the sizers
        self.vbox_inputs = wx.BoxSizer(wx.VERTICAL)

        self.hbox_email = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox_password = wx.BoxSizer(wx.HORIZONTAL)
        
        self.hbox_email.AddMany([
            (emp_email_lbl, 0, wx.ALL | wx.RIGHT, 15),
            (emp_email_input, 1, wx.EXPAND | wx.ALL, 5)
            ])
        
        self.hbox_password.AddMany([
            (emp_password_lbl, 0, wx.ALL, 5),
            (emp_password_input, 1, wx.EXPAND | wx.ALL, 5)
            ])
        
        self.hbox_btns = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox_btns.AddMany([
            (cancel_btn),
            (submit_btn)
            ])

        # email, password, buttons, & horizontal line sizer
        self.vbox_email_password_btns = wx.BoxSizer(wx.VERTICAL)
        self.vbox_email_password_btns.AddMany([
            (self.hbox_email, 1, wx.EXPAND | wx.ALL, 2),
            (self.hbox_password, 1, wx.EXPAND | wx.ALL, 2),
            (self.hbox_btns, 0, wx.ALIGN_RIGHT | wx.RIGHT, 20),
            (self.hline, 0, wx.EXPAND | wx.ALL, 5)
            ])
        
        # add the email, password, buttons horizontal sizers to the vbox_input sizer
        self.vbox_inputs.AddMany([
             (self.vbox_email_password_btns, 0, wx.ALIGN_CENTER, 2),
             (self.help_txt, 0, wx.ALL | wx.TEXT_ALIGNMENT_JUSTIFIED, 10)
            ])

        self.SetSizer(self.vbox_inputs)
        #----------------------------------------------------

    def handleLogin(self, event):
        pub.sendMessage("loggedin_listener", message='true')
        self.Destroy()      

    def handleCancel(self, event):
        self.Destroy()

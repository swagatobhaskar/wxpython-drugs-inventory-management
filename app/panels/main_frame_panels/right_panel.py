import wx
from pubsub import pub

from dialogs.login_dialog import LoginDialog
from frames.products_window import ProductsWindow

class RightPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent, style=wx.BORDER_SIMPLE)

        self.SetBackgroundColour('#f8f8ff')

        # main vertical sizer for this panel   
        self.vbox_main = wx.BoxSizer(wx.VERTICAL)
        
        #-------------------------------------------------------
        # Sizers for contact info, auth form
        self.vbox_contact = wx.BoxSizer(wx.VERTICAL)

        org_name = wx.StaticText(self, label='ABC Pharmaceuticals Wholesale')
        font = org_name.GetFont()
        font.PointSize += 14
        font = font.Bold()
        org_name.SetFont(font)

        address = """66B, Tower Street\nOld Water Park,\nXYZ City, 123456\nContact: +91 1234 8899"""
        address_label = wx.StaticText(self, label=address)
                
        # Create Login button
        self.login_btn = wx.Button(self, label="Login")
        self.login_btn.Bind(wx.EVT_BUTTON, self.handleLogin)

        self.logout_btn = wx.Button(self, label="Log Out")
        self.logout_btn.Bind(wx.EVT_BUTTON, self.handleLogout)
        self.logout_btn.Hide()

        self.btn_grid_panel = ButtonsGridPanel(self)
        self.btn_grid_panel.Hide()

        #-----------------------------------------------------------
        self.hbox_btns = wx.BoxSizer(wx.HORIZONTAL)
        self.hbox_btns.AddMany(
            [(self.login_btn, 0, wx.ALL, 2), (self.logout_btn, 0, wx.ALL, 2)]
            )

        self.vbox_contact.Add(org_name, 0, wx.BOTTOM | wx.ALIGN_LEFT, 5)
        self.vbox_contact.Add(address_label, 0, wx.TOP | wx.BOTTOM | wx.ALIGN_LEFT, 5)
        self.vbox_contact.Add(self.hbox_btns, 0, wx.ALL | wx.ALIGN_CENTER, 10)

        self.vbox_main.Add(self.vbox_contact, 0, wx.EXPAND | wx.ALL, 10)
        self.vbox_main.Add(self.btn_grid_panel, 1, wx.EXPAND | wx.ALL, 5)
        self.SetSizer(self.vbox_main)
        #---------------------------------------------------------------------
        
        pub.subscribe(self.hideAndShowButtons, "loggedin_listener")

        self.Layout()

    def handleLogout(self, event):
        pub.sendMessage('loggedin_listener', message='false')
        
        if self.logout_btn.IsShown():
            self.logout_btn.Hide()
            self.login_btn.Show()

    def handleLogin(self, event):
        # wx.MessageBox("Feature not ready!",'Info',
        #     wx.OK | wx.ICON_EXCLAMATION)
        dlg = LoginDialog()
        dlg.ShowModal()

    def hideAndShowButtons(self, message):
        if message == 'true':
            self.login_btn.Hide()
            
            if not self.logout_btn.IsShown():
                # Show the logout button
                # insert a confirmation dialog!!
                self.logout_btn.Show()
                self.hbox_btns.Layout()
            
            if not self.btn_grid_panel.IsShown():
                # show the functionality buttons
                self.btn_grid_panel.Show()
                self.vbox_main.Layout()


class ButtonsGridPanel(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

        self.grid_btns = wx.GridSizer(3, 3, 5, 5) # row, col, vgap, hgap

        products_btn = wx.Button(self, label='Products')
        products_btn.Bind(wx.EVT_MENU, self.handleProducts)

        manufacturers_btn = wx.Button(self, label='Manufacturers')
        manufacturers_btn.Bind(wx.EVT_MENU, self.handleManufacturers)

        suppliers_btn = wx.Button(self, label='Suppliers')
        suppliers_btn.Bind(wx.EVT_MENU, self.handleSuppliers)

        buyers_btn = wx.Button(self, label='Buyers')
        buyers_btn.Bind(wx.EVT_MENU, self.handleBuyers)

        sales_btn = wx.Button(self, label='Sales')
        sales_btn.Bind(wx.EVT_MENU, self.handleSales)

        transactions_btn = wx.Button(self, label='Transactions')
        transactions_btn.Bind(wx.EVT_MENU, self.handleTransactions)

        orders_btn = wx.Button(self, label='Orders')
        orders_btn.Bind(wx.EVT_MENU, self.handleOrders)

        self.grid_btns.AddMany([
            (products_btn, 1, wx.EXPAND),
            (manufacturers_btn, 1, wx.EXPAND),
            (suppliers_btn, 1, wx.EXPAND),
            (buyers_btn, 1, wx.EXPAND),
            (sales_btn, 1, wx.EXPAND),
            (transactions_btn, 1, wx.EXPAND),
            (orders_btn, 1, wx.EXPAND),
            ])
        
        self.SetSizer(self.grid_btns)
        
    def handleProducts(self, event):
        self.products_window = ProductsWindow(self)
        self.products_window.Show()

    def handleManufacturers(self, event):
        pass

    def handleSuppliers(self, event):
        pass

    def handleBuyers(self, event):
        pass

    def handleSales(self, event):
        pass

    def handleTransactions(self, event):
        pass

    def handleOrders(self, event):
        pass

import wx

from panels.main_frame_panels.right_panel import RightPanel
from panels.main_frame_panels.left_panel import LeftPanel
from frames.products_window import ProductsWindow

class MainFrame(wx.Frame):
    def __init__(self, parent=None):
        super().__init__(parent, size=(900, 600), title='ABC Drugs')

        self.InitMenubar()
        # self.InitToolbar()

        # Sizer for two panels
        self.hbox = wx.BoxSizer(wx.HORIZONTAL)
        
        # Left panel for image
        self.left_panel = LeftPanel(self)

        # right panel for auth form
        self.right_panel = RightPanel(self)

        # Add the panels to the hbox sizer
        self.hbox.AddMany([
            (self.left_panel, 1, wx.EXPAND | wx.ALL, 1),
            (self.right_panel, 1, wx.EXPAND | wx.ALL, 1)
        ])

        # Set the sizer to the frame
        self.SetSizer(self.hbox)
        self.Center()

    def InitToolbar(self):
        toolbar = self.CreateToolBar()
        toolbar.AddTool(wx.ID_ANY, "Products", wx.Bitmap("Open.bmp"))
        toolbar.AddTool(wx.ID_ANY, "Manufacturers")
        toolbar.AddTool(wx.ID_ANY, "Suppliers")
        toolbar.AddTool(wx.ID_ANY, "Buyers")
        toolbar.AddTool(wx.ID_ANY, "Transactions")
        toolbar.Realize()  

    def InitMenubar(self):
        menubar = wx.MenuBar()
        
        # Create File Menu
        fileMenu = wx.Menu()
        # home_option = fileMenu.Append(wx.ID_ANY, 'Ho&me', 'Go to Home')
        # self.Bind(wx.EVT_MENU, self.goHome, home_option)
        quit = fileMenu.Append(wx.ID_EXIT, '&Quit', 'Close')
        self.Bind(wx.EVT_MENU, self.OnQuit, quit)
        
        # Create Product Menu and its CRUD options as sub-menus
        productsMenu = wx.Menu()
        view_product = productsMenu.Append(wx.ID_ANY, 'View')
        self.Bind(wx.EVT_MENU, self.handleProducts, view_product)
        productsMenu.Append(wx.ID_ANY, 'Add')
        productsMenu.Append(wx.ID_ANY, 'Modify')

        # Manufacturers Menu
        manufacturersMenu = wx.Menu()
        manufacturersMenu.Append(wx.ID_ANY, 'View')
        manufacturersMenu.Append(wx.ID_ANY, 'Add')
        manufacturersMenu.Append(wx.ID_ANY, 'Modify')

        # Suppliers Menu
        suppliersMenu = wx.Menu()
        suppliersMenu.Append(wx.ID_ANY, 'View')
        suppliersMenu.Append(wx.ID_ANY, 'Add')
        suppliersMenu.Append(wx.ID_ANY, 'Modify')

        # Sales & Transactions Menu
        buySellMenu = wx.Menu()

        # Sales sub-menu
        sales = wx.Menu()
        newSale=sales.Append(wx.ID_ANY, 'New Sale')
        #self.Bind(wx.EVT_MENU, self.handleNewSale, newSale)
        sales.Append(wx.ID_ANY, 'Sales History')
        sales.Append(wx.ID_ANY, 'Modify Sale')

        # append sales sub-menu to 'buy & sell' menu
        buySellMenu.Append(wx.ID_ANY, 'S&ales', sales)
        buySellMenu.AppendSeparator()

        # Transactions sub-menu
        transactions = wx.Menu()
        transactions.Append(wx.ID_ANY, 'New Transaction')
        transactions.Append(wx.ID_ANY, 'Transactions History')
        transactions.Append(wx.ID_ANY, 'Modify Transaction')
        # append transactions sub-menu to 'buy & sell' menu
        buySellMenu.Append(wx.ID_ANY, '&Transactions', transactions)

        # App user menu item
        userMenu = wx.Menu()
        userMenu.Append(wx.ID_ANY, 'My Profile')
        userMenu.Append(wx.ID_ANY, 'Log Out')
        about_item = userMenu.Append(wx.ID_ABOUT, 'About', 'Show About')
        #self.Bind(wx.EVT_MENU, self.handleAbout, about_item)

        # Append menu items to the MenuBar
        menubar.Append(fileMenu, '&File')
        menubar.Append(productsMenu, '&Products')
        menubar.Append(manufacturersMenu, '&Manufacturers')
        menubar.Append(suppliersMenu, '&Suppliers')
        menubar.Append(buySellMenu, '&Buy && Sell')
        menubar.Append(userMenu, '&User')

        self.SetMenuBar(menubar)

    def OnQuit(self, event):
        # self.Close()

        # StackOverflow
        wx.CallAfter(self.Destroy)

    def handleProducts(self, event):
        self.products_window = ProductsWindow(self)
        self.products_window.Show()
import wx

class ProductsWindow(wx.Frame):
    def __init__(self, parent, database):
        super().__init__(parent, title='ABC Drugs | Products', size=(900, 600))

        self.database = database

        self.SetBackgroundColour(wx.Colour('Magenta'))

        # Create a panel and a notebook on the panel.
        nb_panel = wx.Panel(self)
        nb = wx.Notebook(nb_panel)

        # Create the page windows as children of the notebook.
        view_page = ViewTab(nb, self.database)
        add_page = AddTab(nb)
        modify_tab = ModifyTab(nb)

        # Add the pages to the notebook with the label to show on the tab.
        nb.AddPage(view_page, 'View')
        nb.AddPage(add_page, 'New')
        nb.AddPage(modify_tab, 'Modify')

        # Finally, put the notebook in a sizer for
        # the panel to manage the layout.
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        nb_panel.SetSizer(sizer)

        self.Center()
        self.Show()

class ViewTab(wx.Panel):
    def __init__(self, parent, database):
        super().__init__(parent)

        self.database = database

        self.list_ctrl = wx.ListCtrl(
            self, size=(870, 350),
            style=wx.LC_REPORT | wx.BORDER_SUNKEN
        )
        # vertical sizer to contain list, button
        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox_list = wx.BoxSizer(wx.HORIZONTAL)
        # self.list = wx.ListCtrl(self, -1, style = wx.LC_REPORT)
        self.list_ctrl.InsertColumn(0, 'ID', width = 10)
        self.list_ctrl.InsertColumn(1, 'Name', wx.LIST_FORMAT_RIGHT, width = 100) 
        self.list_ctrl.InsertColumn(2, 'Price', wx.LIST_FORMAT_RIGHT, 100) 
        self.list_ctrl.InsertColumn(3, 'Composition', wx.LIST_FORMAT_RIGHT, 200)
        self.list_ctrl.InsertColumn(4, 'Pack Size', wx.LIST_FORMAT_RIGHT, 150)
        self.list_ctrl.InsertColumn(5, 'Expiry Date', wx.LIST_FORMAT_RIGHT, 150)
        hbox_list.Add(self.list_ctrl, 1, wx.EXPAND | wx.ALL, 5)
        vbox.Add(hbox_list)

        self.load_medicines()

        view_btn = wx.Button(self, label='View')
        view_btn.Bind(wx.EVT_BUTTON, self.on_view_click)
        vbox.Add(view_btn)

        self.SetSizer(vbox)
    
    def load_medicines(self):
        self.list_ctrl.DeleteAllItems()
        medicines = self.database.get_all_medicines()
        
        index = 0
        for medicine in medicines:
            # index = self.list_ctrl.InsertItem(sys.maxsize, medicine[0])
            self.list_ctrl.InsertItem(index, medicine[0])
            self.list_ctrl.SetItem(index, 1, medicine[1])
            self.list_ctrl.SetItem(index, 2, str(medicine[4]))
            self.list_ctrl.SetItem(index, 3, medicine[2])
            self.list_ctrl.SetItem(index, 4, medicine[3])
            self.list_ctrl.SetItem(index, 5, medicine[8])
            index += 1

    def on_view_click(self, event):
        selection = self.list_ctrl.GetFocusedItem()
        
class AddTab(wx.Panel):
    def __init__(self, parent, database):
        super().__init__(parent)

        self.database = database

        self.grid = wx.FlexGridSizer(3, 4, 2, 4) # rows, cols, vgap, hgap

        name = wx.StaticText(self, label='Medicine Name')
        """
        https://coderslegacy.com/wxpython-tutorial/flexgridsizer/
        """

class ModifyTab(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)

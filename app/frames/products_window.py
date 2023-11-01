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
        add_page = AddTab(nb, self.database)
        modify_tab = ModifyTab(nb, self.database)

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
        wx.MessageBox(str(selection))
        
class AddTab(wx.Panel):
    def __init__(self, parent, database):
        super().__init__(parent)

        self.database = database

        self.wrapper = wx.BoxSizer(wx.VERTICAL)
        self.grid = wx.FlexGridSizer(4, 4, 10, 10) # rows, cols, vgap, hgap

        med_name = wx.StaticText(self, label='Medicine Name')
        self.med_name_input = wx.TextCtrl(self)

        mfr_name = wx.StaticText(self, label='Manufacturer')
        self.mfr_name_input = wx.TextCtrl(self)

        price = wx.StaticText(self, label='Unit Price')
        self.price_input = wx.TextCtrl(self)

        exp_date = wx.StaticText(self, label='Expiry Date')
        self.exp_date_input = wx.TextCtrl(self)

        mfg_date = wx.StaticText(self, label='Manufactured Date')
        self.mfg_date_input = wx.TextCtrl(self)

        batchno = wx.StaticText(self, label='Batch No')
        self.batchno_input = wx.TextCtrl(self)

        composition = wx.StaticText(self, label='Composition')
        self.composition_input = wx.TextCtrl(self)

        self.grid.AddMany([
            (med_name, 0),
            (self.med_name_input, 1, wx.EXPAND),
            (mfr_name, 0),
            (self.mfr_name_input, 1, wx.EXPAND),
            (price, 0),
            (self.price_input, 1, wx.EXPAND),
            (exp_date, 0),
            (self.exp_date_input, 1, wx.EXPAND),
            (mfg_date, 0),
            (self.mfg_date_input, 1, wx.EXPAND),
            (batchno, 0),
            (self.batchno_input, 1, wx.EXPAND),
            (composition, 0),
            (self.composition_input, 1, wx.EXPAND)
        ])

        # self.grid.AddGrowableRow(0, 1)
        # self.grid.AddGrowableRow(1, 1)
        # self.grid.AddGrowableRow(2, 1)

        self.hbox_btns = wx.BoxSizer(wx.HORIZONTAL)
        
        cancel_btn = wx.Button(self, label='Cancel')
        cancel_btn.Bind(wx.EVT_BUTTON, self.handleCancel)
        add_btn = wx.Button(self, label='Add')
        add_btn.Bind(wx.EVT_BUTTON, self.addNewMedicine)

        self.hbox_btns.AddMany([
            (cancel_btn, 0, wx.ALL, 5),
            (add_btn, 0, wx.ALL, 5)
        ])

        self.wrapper.Add(self.grid, 0, wx.ALL | wx.EXPAND | wx.ALIGN_CENTER, 5)
        self.wrapper.Add(self.hbox_btns, 0, wx.ALIGN_RIGHT, 5)
        self.SetSizer(self.wrapper)

    def addNewMedicine(self, event):
      
        name = self.med_name_input.GetValue()
        mfr = self.mfr_name_input.GetValue()
        price = self.price_input.GetValue()
        exp = self.exp_date_input.GetValue()
        mfg = self.mfg_date_input.GetValue()
        batch = self.batchno_input.GetValue()
        composition = self.composition_input.GetValue()

        self.database.add_medicine(name, mfr, price, exp, mfg, batch, composition)

    def handleCancel(self, event):
        self.Refresh()
        # self.med_name_input.AppendText('')
        # self.mfr_name_input.AppendText('')
        # self.price_input.AppendText('')
        # self.exp_date_input.AppendText('')
        # self.mfg_date_input.AppendText('')
        # self.batchno_input.AppendText('')
        
class ModifyTab(wx.Panel):
    def __init__(self, parent, database):
        super().__init__(parent)
        self.database = database

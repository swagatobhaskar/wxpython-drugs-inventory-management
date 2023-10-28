import wx
import wx.lib.mixins.listctrl as listmix
import sqlite3
import pandas as pd
import pathlib

class ABC_wholesale_DB:
    def __init__(self) -> None:
        self.conn = sqlite3.connect('./abc_wholesale.db')
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        csv_path = pathlib.Path.cwd() / 'app/database/csv_data_files/'
        medicines_df = pd.read_csv(csv_path / 'drugs-inventory-medicines-data.csv') 
        mfrs_df = pd.read_csv(csv_path / 'mfrs_data.csv')
        customers_df = pd.read_csv(csv_path / 'drugs-inventory-customers-data.csv')
        users_df = pd.read_csv(csv_path / 'drugs-inventory-app-users.csv')
        suppliers_df = pd.read_csv(csv_path / 'drugs-inventory-suppliers-data.csv')

        # Write the data to a sqlite table
        medicines_df.to_sql(con=self.conn, name='medicines', if_exists='append', index=False)
        mfrs_df.to_sql(con=self.conn, name='manufacturers', if_exists='append', index=False)
        customers_df.to_sql(con=self.conn, name='customers', if_exists='append', index=False)
        users_df.to_sql(con=self.conn, name='users', if_exists='append', index=False)
        suppliers_df.to_sql(con=self.conn, name='suppliers', if_exists='append', index=False)
  
    def get_all_medicines(self):
        self.cursor.execute('SELECT * FROM medicines')
        return self.cursor.fetchall()
    
    def add_medicine(self, name, description):
        self.cursor.execute(
            'INSERT INTO medicines (name, description) VALUES (?, ?)',
              (name, description)
              )
        self.conn.commit()
        # name,price,pack_size_label,short_composition,id,mfr_id,qty_in_stock,batch_no,exp_date,mfg_date

    def update_medicine(self, id, name, composition, price, qty_in_stock, batch_no, exp_date, mfg_date):
        self.cursor.execute(
            'UPDATE medicines SET name=?, short_composition=? WHERE id=?',
            (name, composition, id)
            )
        self.conn.commit()

    def delete_medicine(self, id):
        self.cursor.execute('DELETE FROM medicines WHERE id=?', (id,))
        self.conn.commit()

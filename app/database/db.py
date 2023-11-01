import sqlite3
import pandas as pd
import pathlib

class ABC_wholesale_DB:
    def __init__(self) -> None:
        SQL_DB_PATH = pathlib.Path.cwd()/'app/database/abc_wholesale.db'
        self.conn = sqlite3.connect(SQL_DB_PATH)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        csv_path = pathlib.Path.cwd() / 'app/database/csv_data_files/'
        medicines_df = pd.read_csv(csv_path / 'inventory-medicines.csv', index_col=False) 
        mfrs_df = pd.read_csv(csv_path / 'mfrs_data.csv', index_col=False)
        customers_df = pd.read_csv(csv_path / 'inventory-customers.csv', index_col=False)
        users_df = pd.read_csv(csv_path / 'inventory-users.csv', index_col=False)
        suppliers_df = pd.read_csv(csv_path / 'inventory-suppliers.csv', index_col=False)

        # Write the data to a sqlite table
        medicines_df.to_sql(con=self.conn, name='medicines', if_exists='replace', index=False)
        mfrs_df.to_sql(con=self.conn, name='manufacturers', if_exists='replace', index=False)
        customers_df.to_sql(con=self.conn, name='customers', if_exists='replace', index=False)
        users_df.to_sql(con=self.conn, name='users', if_exists='replace', index=False)
        suppliers_df.to_sql(con=self.conn, name='suppliers', if_exists='replace', index=False)
  
    def get_all_medicines(self):
        self.cursor.execute('SELECT * FROM medicines')
        return self.cursor.fetchall()
    
    def add_medicine(self, name, description, price, batch, exp, mfg, mfr_id):
        self.cursor.execute(
            # auto add ID
            'INSERT INTO medicines (name, price, mfr_id, composition, exp_date, batch_no, mfg_date) VALUES (?, ?, ?, ?, ?, ?, ?)',
              (name, description, mfr_id, price, batch, exp, mfg)
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

    def check_user_exists(self, email, password):
        self.cursor.execute('SELECT id FROM users WHERE email=? AND password=?',
                                     (email, password))
        self.conn.commit()
        return self.cursor.fetchone()
        
    
import pandas as pd
import sqlite3
from sqlalchemy import (
    Column, Integer, String, ForeignKey, Table, create_engine, MetaData)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

engine = create_engine("sqlite:///abc-drugs-inventory.db")
  
# Load CSV data into Pandas DataFrame 
products_df = pd.read_csv('drugs-inventory-products_medicines-data.csv') 
# Write the data to a sqlite table 
products_df.to_sql(con=engine, name='products', if_exists='replace', index=False) 
  
# # Create a cursor object 
# cur = conn.cursor() 
# # Fetch and display result 
# for row in cur.execute('SELECT * FROM meds'): 
#     print(row) 
# # Close connection to SQLite database 
# conn.close()

conn = engine.connect() 
metadata = MetaData()

products = Table('Products', metadata, autoload=True, autoload_with=engine)

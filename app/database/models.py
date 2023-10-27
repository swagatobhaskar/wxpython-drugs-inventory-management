import pandas as pd
import sqlite3
from sqlalchemy import (
    Column, Integer, String, Float, ForeignKey, Table, create_engine, MetaData)
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
  
# Load CSV data into Pandas DataFrame 
products_df = pd.read_csv('csv_data_files/drugs-inventory-products_medicines-data.csv') 
mfrs_df = pd.read_csv('csv_data_files/mfrs_data.csv')
customers_df = pd.read_csv('csv_data_files/drugs-inventory-customers-data.csv')
users_df = pd.read_csv('csv_data_files/drugs-inventory-app-users.csv')
suppliers_df = pd.read_csv('csv_data_files/drugs-inventory-suppliers-data.csv')

engine = create_engine("sqlite+pysqlite:///abc-drugs-inventory.db", echo=True)

# Write the data to an sqlite table 
products_df.to_sql(con=engine, name='products', if_exists='replace', index=False)
mfrs_df.to_sql(con=engine, name='manufacturers', if_exists='replace', index=False)
customers_df.to_sql(con=engine, name='customers', if_exists='replace', index=False)
users_df.to_sql(con=engine, name='users', if_exists='replace', index=False)
suppliers_df.to_sql(con=engine, name='suppliers', if_exists='replace', index=False)

Base = declarative_base()
metadata_obj = MetaData()

"""Follow the declarative mapping process"""
# class Sales(Base):
#     __table__ = 'Sales',
#               Column('Id', Integer(), primary_key=True),
#               Column('customer_id', Integer(), ForeignKey),
#               Column('product', String(255), nullable=False),
#               Column('quantity', Integer(), nullable=False, default=1),
#               Column('Price', Float(), nullable=False)
# )

Orders = Table('Orders', metadata_obj,
              Column('Id', Integer(), primary_key=True),
              Column('mfr_id', Integer(), ForeignKey),
              Column('product', String(255), nullable=False),
              Column('quantity', Integer(), nullable=False, default=1),
              Column('Price', Float(), nullable=False)
)

products = Table('Products', metadata_obj, autoload=True, autoload_with=engine)
customers = Table('Customers', metadata_obj, autoload=True, autoload_with=engine)
mfrs = Table('Manufacturers', metadata_obj, autoload=True, autoload_with=engine)
suppliers = Table('Suppliers', metadata_obj, autoload=True, autoload_with=engine)
Users = Table('Users', metadata_obj, autoload=True, autoload_with=engine)

metadata_obj.create_all(engine) 

conn = engine.connect() 

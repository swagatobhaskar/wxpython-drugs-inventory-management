import pandas as pd
import sqlite3
from sqlalchemy import (
    Column, Integer, String, Float, ForeignKey, Table, create_engine, MetaData)
from sqlalchemy.orm import sessionmaker, Mapped, mapped_column, relationship
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

class Base(declarative_base):
    pass

# This declaration is for overriding reflected tables
metadata_obj = MetaData()

"""
id: Mapped[int] = mapped_column(primary_key=True)
...     name: Mapped[str] = mapped_column(String(30))
...     fullname: Mapped[Optional[str]]
...
...     addresses: Mapped[List["Address"]] = relationship(
...         back_populates="user", cascade="all, delete-orphan"
...     )
...
...     def __repr__(self) -> str:
...         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

"""
class Sales(Base):
    __tablename__ = "sales"

    id: Mapped[int] = mapped_column(primary_key=True)
    customer_id: Mapped[int] = relationship(
          back_populates="customer", cascade="all, delete-orphan"
    )
              Column('product', String(255), nullable=False)
              Column('quantity', Integer(), nullable=False, default=1)
              Column('Price', Float(), nullable=False)
    
    def __repr__(self) -> str:
        return f"Customer(id={self.id!r}"

Orders = Table('Orders', metadata_obj,
              Column('Id', Integer(), primary_key=True),
              Column('mfr_id', Integer(), ForeignKey),
              Column('product', String(255), nullable=False),
              Column('quantity', Integer(), nullable=False, default=1),
              Column('Price', Float(), nullable=False)
)

"""Overriding the following reflected tables"""
products = Table('Products', metadata_obj,
                 Column('id', Integer, primary_key=True),
                 Column('mfr_id',Integer, ForeignKey(mfrs.id))
                 autoload_with=engine
                 )
customers = Table('Customers', metadata_obj,
                  Column('id', Integer, primary_key=True),
                  autoload_with=engine
                  )
mfrs = Table('Manufacturers', metadata_obj,
             Column('id', Integer, primary_key=True),
             autoload_with=engine
             )
suppliers = Table('Suppliers', metadata_obj,
                  Column('id', Integer, primary_key=True),
                  autoload_with=engine
                  )
Users = Table('Users', metadata_obj,
              Column('id', Integer, primary_key=True),
              autoload_with=engine
              )

# metadata_obj.create_all(engine)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine) 
session = Session() 

# conn = engine.connect() 

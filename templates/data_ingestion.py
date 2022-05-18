import pandas as pd
import mysql
import mysql.connector
from sqlalchemy import create_engine


mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Ethio4life(001)",
        db = "tractortek"
)

engine = create_engine('mysql+pymysql://root:Ethio4life(001)@localhost/tractortek')

# data table
file_name="Data/date_table.csv"
df = pd.read_csv(file_name)
df.to_sql('date_table', con=engine,if_exists='append',index=False)

# employee table
file_name="Data/employee.csv"
df = pd.read_csv(file_name)
df.to_sql('employee', con=engine,if_exists='append',index=False)

# esp price table
file_name="Data/esp_price.csv"
df = pd.read_csv(file_name)
df.to_sql('esp_price', con=engine,if_exists='append',index=False)

# esp sales table
file_name="Data/esp_sales.csv"
df = pd.read_csv(file_name)
df.to_sql('esp_sales', con=engine,if_exists='append',index=False)

# prodcut info table
file_name="Data/prod_info.csv"
df = pd.read_csv(file_name)
df.to_sql('prod_info', con=engine,if_exists='append',index=False)

# prodcut price table
file_name="Data/prod_price.csv"
df = pd.read_csv(file_name)
df.to_sql('prod_price', con=engine,if_exists='append',index=False)

#prod_sales
file_name="Data/prod_sales.csv"
df = pd.read_csv(file_name)
df.to_sql('prod_sales', con=engine,if_exists='append',index=False)

import os
import pandas as pd
from sqlalchemy import create_engine

# Securely fetch credentials
hostname = os.getenv('MYSQL_HOST', 'localhost')
username = os.getenv('MYSQL_USER', 'manu')
password = os.getenv('MYSQL_PASS', 'manu!123')
database = os.getenv('MYSQL_DB', 'manu_dev_db')

# MySQL connection
engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database}')

# File path
excel_file_path = r"D:\Users\Documents\Users.xlsx"

# Read Excel file
try:
    df = pd.read_excel(excel_file_path)
except Exception as e:
    print(f"Error reading Excel file: {e}")
    exit()

# Upload to MySQL
table_name = 'User'
try:
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    print(f'Excel file has been uploaded to the MySQL table "{table_name}".')
except Exception as e:
    print(f"Error uploading data to MySQL: {e}")

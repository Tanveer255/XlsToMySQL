# README

## Overview

This script reads data from an Excel file and uploads it to a MySQL database table using Python. It uses the following libraries:

- `pandas`: For handling Excel files and data manipulation.
- `sqlalchemy`: For database connection and interaction.
- `openpyxl`: For reading `.xlsx` Excel files.
- `pymysql`: For connecting to a MySQL database.

## Prerequisites

### Python Packages

Ensure the following Python packages are installed:

```bash
pip install pandas sqlalchemy openpyxl pymysql
```

### MySQL Database

1. Ensure the MySQL database is running and accessible.
2. Verify the database credentials (hostname, username, password, and database name).
3. Ensure the user has the necessary permissions to create or replace tables.

## Usage

### Script Configuration

1. Update the `hostname`, `username`, `password`, and `database` variables with your MySQL connection details.
2. Specify the path to the Excel file using the `excel_file_path` variable. Use a raw string (prefix the string with `r`) to avoid issues with backslashes in file paths.
3. Set the `table_name` variable to the name of the target MySQL table.

### Running the Script

Save the script as `ReadDataExcel.py` and execute it using the following command:

```bash
python ReadDataExcel.py
```

### Example Script

```python
import os
import pandas as pd
from sqlalchemy import create_engine

# Securely fetch credentials
hostname = os.getenv('MYSQL_HOST', '192.168.0.12')
username = os.getenv('MYSQL_USER', 'edge')
password = os.getenv('MYSQL_PASS', 'ko7Mar^e8cAQc')
database = os.getenv('MYSQL_DB', 'edge_AuthServer_dev_db')

# MySQL connection
engine = create_engine(f'mysql+pymysql://{username}:{password}@{hostname}/{database}')

# File path
excel_file_path = r"D:\EdgeCTP.Net8.0\edge_authServer_db.xlsx"

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
```

## Error Handling

- **Authentication Errors**: Ensure the provided credentials and host details are correct.
- **Excel File Reading Errors**: Verify the file path and ensure the file exists in the specified location.
- **Database Schema Issues**: Ensure the DataFrame's structure matches the target table schema.

## Additional Notes

- Avoid hardcoding credentials in production. Use environment variables or a configuration file for better security.
- Test the script in a development environment before running it in production.

## Support

If you encounter any issues or have questions, feel free to reach out for assistance:

- [Tanveer255](https://github.com/Tanveer255)
- [Muhammad Tanveer](https://www.linkedin.com/in/muhammad-tanveer-5b0a111a0/)

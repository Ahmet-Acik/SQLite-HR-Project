import sqlite3
import pandas as pd

# Connect to the HR sample database
conn = sqlite3.connect('../hr.db')

# Example query: List all employees
df = pd.read_sql_query('SELECT * FROM employees', conn)
print(df.head())

conn.close()
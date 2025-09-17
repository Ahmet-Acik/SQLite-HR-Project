import sqlite3
import pandas as pd

# Connect to the HR sample database
conn = sqlite3.connect('hr_sample.db')

# Example query: List all employees
df = pd.read_sql_query('SELECT * FROM employees', conn)
print(df.head())

conn.close()

import sqlite3

def run_sql_file(db_path, sql_file_path):
    with open(sql_file_path, 'r', encoding='utf-8') as f:
        sql = f.read()
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        cursor.executescript(sql)
        print(f"Executed {sql_file_path}")

# Example usage:
run_sql_file('hr_sample.db', 'scripts/sql_examples/select_examples.sql')
import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), '../hr_sample.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'hr_schema.sql')
DATA_PATH = os.path.join(os.path.dirname(__file__), 'hr_data.sql')

def run_sql_script(db_path, script_path):
    with open(script_path, 'r', encoding='utf-8') as f:
        sql_script = f.read()
    with sqlite3.connect(db_path) as conn:
        conn.executescript(sql_script)
    print(f"Executed {os.path.basename(script_path)} successfully.")

def main():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Removed existing database: {DB_PATH}")
    run_sql_script(DB_PATH, SCHEMA_PATH)
    run_sql_script(DB_PATH, DATA_PATH)
    print(f"Database created at {DB_PATH}")

if __name__ == "__main__":
    main()

import sqlite3
import re

DB_PATH = 'hr_sample.db'
SQL_FILE = 'scripts/sql_examples/select_examples.sql'

def get_select_statements(sql_text):
    # Remove comments and extract SELECT statements robustly
    cleaned = []
    for line in sql_text.splitlines():
        line = line.strip()
        if line.startswith('--') or not line:
            continue
        cleaned.append(line)
    cleaned_sql = ' '.join(cleaned)
    # Split on semicolon, filter only SELECT statements
    statements = [s.strip() for s in cleaned_sql.split(';') if s.strip().lower().startswith('select')]
    return statements

def run_and_print_selects(db_path, sql_file):
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_text = f.read()
    selects = get_select_statements(sql_text)
    print(f"Found {len(selects)} SELECT statements.")
    with sqlite3.connect(db_path) as conn:
        for i, stmt in enumerate(selects, 1):
            print(f'--- Query {i} ---')
            print(f'Executing: {stmt}')
            try:
                cursor = conn.execute(stmt)
                columns = [desc[0] for desc in cursor.description]
                print('\t'.join(columns))
                for row in cursor.fetchall():
                    print('\t'.join(str(x) for x in row))
            except Exception as e:
                print(f'Error: {e}')
            print()

if __name__ == '__main__':
    run_and_print_selects(DB_PATH, SQL_FILE)

import sqlite3
import os
import glob

def get_select_statements(sql_text):
    cleaned = []
    for line in sql_text.splitlines():
        line = line.strip()
        if line.startswith('--') or not line:
            continue
        cleaned.append(line)
    cleaned_sql = ' '.join(cleaned)
    statements = [s.strip() for s in cleaned_sql.split(';') if s.strip().lower().startswith('select')]
    return statements

def run_and_print_selects(db_path, sql_file):
    with open(sql_file, 'r', encoding='utf-8') as f:
        sql_text = f.read()
    selects = get_select_statements(sql_text)
    print(f"\n=== {sql_file} ===")
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

def run_all_sql_examples(db_path, folder):
    sql_files = sorted(glob.glob(os.path.join(folder, '*.sql')))
    for sql_file in sql_files:
        run_and_print_selects(db_path, sql_file)

if __name__ == '__main__':
    DB_PATH = 'hr_sample.db'
    SQL_FOLDER = 'scripts/sql_examples'
    run_all_sql_examples(DB_PATH, SQL_FOLDER)

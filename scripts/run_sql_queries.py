import sqlite3

conn = sqlite3.connect("database/mutual_fund.db")
cursor = conn.cursor()

print("Connected Successfully")

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table';
""")

tables = cursor.fetchall()

print("\nTables Found:")

for table in tables:
    table_name = table[0]

    cursor.execute(
        f"SELECT COUNT(*) FROM {table_name}"
    )

    row_count = cursor.fetchone()[0]

    print(f"{table_name}: {row_count} rows")

conn.close()
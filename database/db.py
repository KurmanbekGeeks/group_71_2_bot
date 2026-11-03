import sqlite3
from database.queries import create_product_table

path_db = 'database/sqlite3.db'

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(create_product_table)
    print('DB connection!')
    conn.commit()
    conn.close()



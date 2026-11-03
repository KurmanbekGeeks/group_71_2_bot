create_product_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_product TEXT,
        price INTEGER,
        description TEXT,
        photo TEXT
    )
"""

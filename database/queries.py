create_product_table = """
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_product TEXT,
        price INTEGER,
        product_id INTEGER NOT NULL
    )
"""


add_product = 'INSERT INTO products (name_product, price, product_id) VALUES (?, ?, ?)'

get_products = """
SELECT p.name_product, p.price, pd.photo, pd.description, pd.category, p.product_id 
FROM products p
INNER JOIN products_detail pd ON p.product_id = pd.product_id;
"""


create_products_detail_table = """
    CREATE TABLE IF NOT EXISTS products_detail (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT,
        photo TEXT,
        category TEXT,
        product_id INTEGER NOT NULL
    )
"""

add_product_detail = 'INSERT INTO products_detail (description, photo, category, product_id) VALUES (?, ?, ?, ?)'


update_product = 'UPDATE {table} SET {field} = ? WHERE product_id = ?'
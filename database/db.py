import aiosqlite
from database import queries

path_db = 'database/bot.db'


async def init_db():
    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(queries.create_product_table)
        await conn.execute(queries.create_products_detail_table)
        await conn.commit()
    print('db connection')


async def add_product_db(name, price, description, photo, category, product_id):
    async with aiosqlite.connect(path_db) as conn:
        # await conn.execute(queries.add_product, (name, price, product_id))
        await conn.execute(queries.add_product_detail, (description, photo, category, product_id))
        await conn.commit()


async def get_products_db():
    async with aiosqlite.connect(path_db) as conn:
        cursor = await conn.execute(queries.get_products)
        products = await cursor.fetchall()
    return products


async def update_product_db(field, value, product_id):
    if field in ('name', 'price'):
        table = 'products'
    elif field in ('description', 'category'):
        table = 'products_detail'
    else:
        print(f'Нет таблицы для вашего поля {field}')
        return

    query = queries.update_product.format(table=table, field=field)

    async with aiosqlite.connect(path_db) as conn:
        await conn.execute(query, (value, product_id))
        await conn.commit()

# ==========================================================
# import sqlite3
# from database.queries import create_product_table

# path_db = 'database/sqlite3.db'

# def init_db():
#     conn = sqlite3.connect(path_db)
#     cursor = conn.cursor()
#     cursor.execute(create_product_table)
#     print('DB connection!')
#     conn.commit()
#     conn.close()



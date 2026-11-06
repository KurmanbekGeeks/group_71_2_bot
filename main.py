import asyncio
import logging
from config import bot, dp
from handlers import commands, echo, fsm_add_product
from database import db


async def on_startup():
    await db.init_db()
    await bot.send_message(chat_id=995712956, text="Бот включен!")


dp.include_router(router=commands.router_commands)
dp.include_router(router=fsm_add_product.router_add_product)

dp.include_router(router=echo.router_echo)


dp.startup.register(on_startup)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(dp.start_polling(bot))

    
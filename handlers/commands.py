from aiogram import F, Router
from aiogram.filters import Command
from aiogram.types import Message, FSInputFile, CallbackQuery
from config import bot
from database import db
from handlers.buttons import main_buttons, menu_buttons

router_commands = Router()

@router_commands.message(Command('start'))
async def start_handler(message: Message):
    await message.answer('Привет мир!', reply_markup=menu_buttons)

    await bot.send_message(chat_id=message.from_user.id, 
                           text=f'Привет! {message.from_user.full_name} \nТвой телеграм ID > {message.from_user.id}')


@router_commands.message(F.text == 'привет')
async def hello_handler(message: Message):
    await message.answer('Салам')


@router_commands.message(Command('sticker'))
async def sticker_handler(message: Message):
    await message.answer_sticker(sticker='CAACAgIAAxkBAAM5auCySPyaBYsHzBJnxxDp79pfm1sAAqirAAKFa_lIF38CcJWB3Wg9BA')
    await message.answer_sticker(sticker='CAACAgIAAxkBAAM1auCx0ITQ88ljCxCaBsYQuKdB2vEAAuMAA1eEbA_LD3f9g8IMvD0E')



@router_commands.message(Command('mem'))
async def mem_handler(message: Message):
    photo = FSInputFile('media/image.png')
    await message.answer_photo(photo=photo)


@router_commands.callback_query(F.data == 'mem')
async def mem_handler_inline_test(call: CallbackQuery):
    photo = FSInputFile('media/image.png')
    await call.message.answer_photo(photo=photo)


@router_commands.message(Command('products'))
async def get_products(message: Message):
    products = await db.get_products_db()

    for name_product, price, description, photo in products:
        await message.answer_photo(photo=photo, caption=f"Название - {name_product} \nЦена - {price} \nОписание - {description}")
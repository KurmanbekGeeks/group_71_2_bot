from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from database.db import add_product_db

class AddProduct(StatesGroup):
    name_product = State()
    price = State()
    description = State()
    photo = State()
    product_id = State()
    category = State()


router_add_product = Router()


@router_add_product.message(Command('add_product'))
async def add_start_fsm(message: Message, state: FSMContext):
    await message.answer('Введите название товара:')
    await state.set_state(AddProduct.name_product)


@router_add_product.message(AddProduct.name_product)
async def add_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Введите цену товара:')
    await state.set_state(AddProduct.price)


@router_add_product.message(AddProduct.price)
async def add_price(message: Message, state: FSMContext):
    await state.update_data(price=message.text)
    await message.answer('Введите описание товара:')
    await state.set_state(AddProduct.description)


@router_add_product.message(AddProduct.description)
async def add_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await message.answer('Отправьте фото товара:')
    await state.set_state(AddProduct.photo)


@router_add_product.message(AddProduct.photo)
async def add_photo(message: Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await message.answer('ВВедите артикул для товара:')
    await state.set_state(AddProduct.product_id)

@router_add_product.message(AddProduct.product_id)
async def add_product_id(message: Message, state: FSMContext):
    await state.update_data(product_id=message.text)
    await message.answer('Введите категорию товара:')
    await state.set_state(AddProduct.category)

@router_add_product.message(AddProduct.category)
async def add_category(message: Message, state: FSMContext):
    await state.update_data(category=message.text)

    data = await state.get_data()

    await add_product_db(name=data['name'], price=data['price'], description=data['description'], photo=data['photo'],
                          category=data['category'], product_id=data['product_id'])

    await message.answer_photo(photo=data['photo'], 
                               caption=f"Товар добавлен: \nНазвание - {data['name']} \nцена - {data['price']}" 
                               f"\nОписание - {data['description']} \nКатегория - {data['category']} \nАртикул = {data['product_id']}")

    await state.clear()
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class AddProduct(StatesGroup):
    field = State()
    new_value = State()

router_edit_product = Router()

# edit:100

# edit 100

@router_edit_product.callback_query(F.data.startswith("edit:"))
async def edit_start(call: CallbackQuery, state: FSMContext):
    product_id = call.data.split(':')[1]
    print(product_id)
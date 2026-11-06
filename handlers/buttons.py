from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


main_buttons = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='/start'), KeyboardButton(text='/mem')]
    ],
    resize_keyboard=True
)


menu_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Мем', callback_data='mem')]
    ]
)
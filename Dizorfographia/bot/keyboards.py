import random as rd

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

kb_start_test = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Начать тест')]],
    resize_keyboard=True
)


async def create_buttons(text: list):
    rd.shuffle(text)
    builder = ReplyKeyboardBuilder()
    [builder.button(text=txt) for txt in text]
    return builder.as_markup(resize_keyboard=True)

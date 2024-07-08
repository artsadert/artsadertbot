from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="Кнопка 2")],
    [KeyboardButton(text="Кнопка 3"), KeyboardButton(text="Кнопка 4")],
])

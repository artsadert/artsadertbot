from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


# Кнопки для удобного испльзования бота
keyboard = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Кнопка 1"), KeyboardButton(text="Кнопка 2")],
    [KeyboardButton(text="Кнопка 3"), KeyboardButton(text="Кнопка 4")],
])

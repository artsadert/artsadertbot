from os import getenv
import asyncio
import logging
import sys

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from modules.buttons import keyboard


dp = Dispatcher()

@dp.message(CommandStart())
async def start_menu(message: Message) -> None:
    await message.answer("Здравствуй дорогой читатель,\n это телеграм бот, созданный для практики работы с yoomoney и google sheets!", reply_markup=keyboard)

@dp.message()
async def echo_handler(message: Message) -> None:
    await message.answer(str(message.text))

async def main(TOKEN: str) -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    # loading token
    load_dotenv()
    if not(TOKEN := getenv("TOKEN_BOT")):
        print("TOKEN must be in .env file!!!")
        quit(1)
    TOKEN = str(TOKEN)
    # run main stream and turn on logging
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main(TOKEN))

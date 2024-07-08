from os import getenv
import asyncio
import logging
import sys

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message, FSInputFile
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from modules.buttons import keyboard
from modules.payment.yoomoney_payment import YoomoneyPay


load_dotenv()
dp = Dispatcher()
try:
    payment = YoomoneyPay(str(getenv("CARD_ID")))
except ValueError:
    print("CARD_ID must be in .env")

@dp.message(CommandStart())
async def start_menu(message: Message) -> None:
    await message.answer("Здравствуй дорогой читатель,\n это телеграм бот, созданный для практики работы с yoomoney и google sheets!", reply_markup=keyboard)

@dp.message()
async def echo_handler(message: Message) -> None:
    match message.text:
        case "Кнопка 1":
            await message.answer("Ленина 1 в городе Сочи:\n https://yandex.com/maps/-/CDGvFAi~")
        case "Кнопка 2":
            payment_url = payment.quickpay()
            await message.answer(f"Ссылка на оплату 2р:\n{payment_url}")
        case "Кнопка 3":
            img = FSInputFile("./assets/img1.jpg")
            await message.answer_photo(img, "Мемасик")

        case "Кнопка 4":
            pass
        case _:
            await message.answer(str(message.text))

async def main(TOKEN: str) -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    # loading token
    if not(TOKEN := getenv("TOKEN_BOT")):
        print("TOKEN must be in .env file!!!")
        quit(1)
    TOKEN = str(TOKEN)
    # run main stream and turn on logging
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main(TOKEN))

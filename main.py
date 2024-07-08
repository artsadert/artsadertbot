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
from modules.sheets.date_sheet import Sheets
from modules.getenv_smart import getenv_smart
from modules.date_check import is_valid_date


load_dotenv()
dp = Dispatcher()
payment = YoomoneyPay(getenv_smart("CARD_ID"))

sheets = Sheets(getenv_smart("SPREADSHEET_A2"), getenv_smart("SPREADSHEET_DATES"), "./creds.json")


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
            await message.answer(f"В ячейке 2 находиться: {sheets.get_value()}")
        case _:
            if is_valid_date(str(message.text)):
                sheets.next_value(str(message.text))
            else:
                await message.answer("Дата введена некорректно")

async def main(TOKEN: str) -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    # loading token
    TOKEN = getenv_smart("TOKEN_BOT")
    # run main stream and turn on logging
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main(TOKEN))

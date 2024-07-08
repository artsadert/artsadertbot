# artsadertbot

Этот бот создан для работы с yoomoney и google sheets

# Установка Linux
## Настройка виртуального окружения
### Создайте виртуальное окружение 
pip -m venv .venv
### активируйте его командой:
source .venv/bin/activate
### Установите зависимости из requirements.txt
pip install -r requirements.txt 

## Настройка .env
Добавьте TOKEN_BOT в .env
Добавьте YOOMONEY_TOKEN в .env
Добавьте CARD_ID в .env
Добавьте два SPREADSHEET в .env

## Настройка credentials
В google api необходимо скачать credentials для корректной работы с google sheets

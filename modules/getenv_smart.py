from os import getenv


# Функция для подгрузки данных из .env файла
def getenv_smart(value: str) -> str:
    if not(res := getenv(value)):
        print(f"Поле {value} должо быть в .env файле!")
        quit(1)
    return str(res)


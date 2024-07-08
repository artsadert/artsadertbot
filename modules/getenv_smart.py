from os import getenv

def getenv_smart(value: str) -> str:
    if not(res := getenv(value)):
        print(f"{value} must be in .env file")
    return str(res)


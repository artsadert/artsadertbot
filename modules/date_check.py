from dateutil.parser import parse, ParserError


# Функция, которая парсит дату и проверяет валидна она или нет
def is_valid_date(date: str | None):
    if not date:
        return False
    try:
        parse(date)
        return True
    except ParserError:
        return False


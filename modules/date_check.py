from dateutil.parser import parse, ParserError


def is_valid_date(date: str):
    if not date:
        return False
    try:
        parse(date)
        return True
    except ParserError:
        return False


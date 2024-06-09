from datetime import date

from bs4 import BeautifulSoup
from requests import get, Response
from requests.exceptions import ReadTimeout

from .error import MoonCalendarError


_link: str = "https://horoscopes.rambler.ru/moon/calendar/{calendar_date}/"


def get_day(calendar_date: date = date.today(),
            timeout: int = 1,) -> BeautifulSoup:
    """Вернуть объект BeautifulSoup."""

    if not isinstance(calendar_date, date):
        raise MoonCalendarError("Attribute calendar_date must be a date.")
    
    try:
        resp: Response = get(_link.format(calendar_date=calendar_date), timeout=timeout,)
    except ReadTimeout:
        raise MoonCalendarError(f"No information for date '{calendar_date}'.")
    status_code: int = resp.status_code

    if status_code != 200:
        raise MoonCalendarError(f"Error status code: {status_code}")
    
    content: bytes = resp.content
    resp.close()
    
    return BeautifulSoup(content, "html.parser",)

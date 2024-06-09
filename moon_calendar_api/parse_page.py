from collections import OrderedDict
from datetime import date
from typing import List, Optional, Union

from bs4 import BeautifulSoup
from bs4.element import Tag, NavigableString

from .calendar_day import CalendarDay
from .error import MoonCalendarError
from .get_day import get_day
from .moon_day import MoonDay, moon_day


def normalize(element: Tag) -> str:
    """Получить нормализованный текст элемента."""

    if not element:
        return

    return (element
           .text
           .replace('\xa0', ' ',)
           .replace('  ', ' ',)
           .strip())


def parse_page(page: BeautifulSoup, calendar_date: date,) -> CalendarDay:
    """Вернуть объект CalendarDay из page."""

    if not isinstance(page, BeautifulSoup):
        raise MoonCalendarError("page must be a BeautifulSoup object.")
    elif not isinstance(calendar_date, date):
        raise MoonCalendarError("calendar_date must be a datetime.date type.")
    
    moon_info: Tag = page.find("div", {"class": "eG1Gp s63PD _3IJOS"})
    moon_desc: Tag = page.find("div", {"class": "dGWT9 cidDQ"})

    element: Union[Tag, NavigableString] = moon_desc.next

    item_header: Optional[str] = None
    item_keys: List[str] = []
    item_values: List[str] = []

    moon_days_info: List[str] = []
    calendar_info: OrderedDict = OrderedDict()
    moon_phase: str = ""

    while element:
        if isinstance(element, Tag):
            text: str = normalize(element)
            if element.get("class") == ['R2dbF', 'inVfT', '_8OzEU']:
                moon_phase = item_header
                calendar_info = OrderedDict(zip(item_keys, item_values))
                break
            elif element.get("class") == ['_1uCdn', 'iVDG2']:
                if not item_keys and item_header:
                    moon_days_info.append("\n".join(item_values))
                item_header = text
                item_keys = []
                item_values = []
            elif element.get("class") == ['PzAWM', 'AW4W0']:
                item_keys.append(text)
            elif element.get("class") == ['_5yHoW', 'AjIPq']:
                item_values.append(text)

        element = element.next
    
    year: int = calendar_date.year

    _moon_days: List[str] = [normalize(day)
                             for day in moon_info
                            .findAll("span", {"class": "ZciAj"},)]
    _periods: List[str] = [normalize(period)
                           for period in moon_info
                          .findAll("span", {"class": "_4FHaJ DSpR9 v5AKG"},)]
    
    moon_days: List[MoonDay] = [
        moon_day(day_name,
                 dates,
                 info,
                 year,)
        for day_name, dates, info in zip(_moon_days, _periods, moon_days_info,)
    ]

    return CalendarDay(calendar_date, moon_phase, moon_days, calendar_info,)


def calendar_info(calendar_date: date = date.today()) -> CalendarDay:
    """Получить данные Лунного календаря на дату."""

    page: BeautifulSoup = get_day(calendar_date=calendar_date)

    return parse_page(page=page, calendar_date=calendar_date,)

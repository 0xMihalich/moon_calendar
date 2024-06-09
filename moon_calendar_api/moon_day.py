from datetime import datetime
from enum import Enum
from typing import List, NamedTuple

from tzlocal import get_localzone

try:
    from zoneinfo import ZoneInfo
except ImportError:
    from backports.zoneinfo import ZoneInfo # type: ignore


tzinfo = ZoneInfo("Europe/Moscow")


class MoonDay(NamedTuple):
    """Продолжительность лунного дня."""

    name: str
    start: datetime
    end: datetime
    info: str

    def __str__(self: "MoonDay") -> str:
        """Вывод информации на страницу."""

        return "\n".join([f"\n{self.name}: "
                          f"{self.start.astimezone(get_localzone())} — "
                          f"{self.end.astimezone(get_localzone())}",
                          f"{self.info}",])

    def __repr__(self) -> str:
        """Вывод информации на печать."""

        return self.__str__()


class Months(Enum):
    """Перечисление месяцев."""

    Jan: str = "января"
    Feb: str = "февраля"
    Mar: str = "марта"
    Apr: str = "апреля"
    May: str = "мая"
    Jun: str = "июня"
    Jul: str = "июля"
    Aug: str = "августа"
    Sep: str = "сентября"
    Oct: str = "октября"
    Nov: str = "ноября"
    Dec: str = "декабря"


def parse_datetime(date_str: str,
                   year: int,) -> datetime:
    """Преобразование строки рамблер в формат datetime."""

    day: str
    month: str
    time: str
    strptime: str = "%Y%d%b%H:%M"

    day, month, time = date_str.split()

    return datetime.strptime(f"{year}{day}{Months(month).name}{time}",
                             strptime,).replace(tzinfo=tzinfo)


def moon_day(day_name: str,
             dates: str,
             info: str,
             year: int,) -> MoonDay:
    """Сборка объекта MoonDay(NamedTuple)."""

    date_start: datetime
    date_end: datetime
    dates_str: List[str] = dates.split(" — ")

    date_start, date_end = (parse_datetime(date_str, year,)
                            for date_str in dates_str)
    
    if date_start > date_end:
        end_year: int = date_end.year - 1
        date_end = date_end.replace(year=end_year)
    
    return MoonDay(day_name, date_start, date_end, info,)

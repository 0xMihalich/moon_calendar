from datetime import date
from typing import List, NamedTuple, OrderedDict

from .moon_day import MoonDay


class CalendarDay(NamedTuple):
    """Объект даты календаря."""

    date: date
    moon_phase: str
    moon_days: List[MoonDay]
    info: OrderedDict[str, str,]

    def __str__(self: "CalendarDay") -> str:
        """Вывод информации на страницу."""

        info: str = "\n".join(f" - {key}: {value}"
                              for key, value
                              in self.info.items())
        moon_days: str = "\n".join(str(moon_day)
                                   for moon_day
                                   in self.moon_days)

        return "\n".join([f"Дата: {self.date}",
                          f"Фаза луны: {self.moon_phase}",
                          moon_days,
                          "\nРекомендации на этот день:",
                          info,
                          "",])

    def __repr__(self) -> str:
        """Вывод информации на печать."""

        return self.__str__()

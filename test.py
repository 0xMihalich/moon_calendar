from moon_calendar_api import date, calendar_info, MoonCalendarError


if __name__ == '__main__':
    """Пример получения информации на определенную дату календаря."""
    try:
        print(calendar_info(date(2024, 7, 2,)))
    except MoonCalendarError as e:
        print(e)

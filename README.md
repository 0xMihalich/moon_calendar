# moon_calendar
API для получения информации с сервиса Rambler Лунный календарь

Спросил маму зачем ей в 2024 году отрывной календарь на стене?
Говорит "ну как же, там же лунные циклы смотреть можно".
Говорю "А что в интернете посмотреть нельзя?"
"Да нет там говорит правильной информации вот тут прям точная."

Ну ок, проверил несколько разных сервисов, нашел на Rambler полное совпадение с тем, что на отрывном календаре.

В общем, сделал пока такое API, в функцию calendar_info нужно передать объект date с необходимой датой (не выше 1 января следующего года), либо не передавать ничего (выведет информацию для сегодняшнего дня).

Даты лунных дней для метода print выводятся для местного часового пояса, в классе CalendarDay при этом они хранятся в часовом поясе ZoneInfo("Europe/Moscow") (GMT+3)

Вобще данный репозиторий это основа для будущего проекта специально для моей мамы, забор информации с сервиса переведу на aiohttp, для хранения данных скорее всего буду использовать SQLite3, архитектуру БД пока продумываю, так же возможно сделаю какой-то локальный синтез речи, чтобы всю необходимую информацию проговаривал.

Из плюшек как минимум буду реализовывать фильтр по лунным дням типо "посмотри, когда ближайшее новолуние" и все такое.

В файле test.py можно увидеть пример работы сервиса

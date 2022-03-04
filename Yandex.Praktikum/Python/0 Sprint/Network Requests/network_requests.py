# Python вместо браузера

# Задача
# Пора учить Анфису разговаривать с серверами в обход браузеров. Отработаем этот навык на разговорах о погоде.
# wttr.in — это сайт с прогнозом погоды, удобный для разработчиков. Если набрать адрес этого сайта без параметров,
# то получим прогноз погоды на несколько дней (попробуйте сделать это в браузере).
# Чтобы вывод был компактным и отображался в тренажёре, задаём следующие параметры:
# 0 - погода только на текущий момент
# T - только текст, чёрно-белый
# Откройте в браузере новый URL с параметрами: страницу http://wttr.in/?0T. Посмотрите, что получается.
# Затем сделайте аналогичный HTTP-запрос на чистом Python.
# Сравните результаты.

import requests

url = 'http://wttr.in/?0T'

response = requests.get(url)  # выполните HTTP-запрос

print(response.text)  # напечатайте текст HTTP-ответа


############


# Передаём параметры в URL

# Задача 1
# Запросите погодный сервис http://wttr.in по URL без параметров. А их задайте словарём weather_parameters.
# Функция get() должна принимать его, как отдельный аргумент params.

import requests

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
    'T': ''
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)

# Задача 2
# Добавьте в словарь с параметрами weather_parameters ещё два параметра:
# M без значения — чтобы скорость ветра была в метрах в секунду, как принято у метеорологов;
# lang со значением ru, чтобы прогноз выдавался на русском языке.
# Обратите внимание на изменения при добавлении этих параметров. О других параметрах можно прочитать в документации.

import requests

url = 'https://wttr.in'  # не изменяйте значение URL

weather_parameters = {
    '0': '',
    # добавьте параметр запроса `T`, чтобы вернулся чёрно-белый текст
    'T': '',
    'M': '',
    'lang': 'ru'
}

response = requests.get(url, params=weather_parameters)  # передайте параметры в http-запрос

print(response.text)


############


# Заголовки запросов и ответов

# Задача
# На прошлом уроке вы заказывали страницу на русском языке через параметры в URL.
# Сейчас сделайте то же самое, только русский язык запрашивайте через заголовок запроса 'Accept-Language'.

import requests

url = 'https://wttr.in'

weather_parameters = {
    '0': '',
    'T': '',
    'M': '',
}

request_headers = {
    # заполните словарь с заголовками
    'Accept-Language': 'ru'
}

# не забудьте передать параметры и заголовки в http-запрос
# через аргументы `params` и `headers` функции get()
response = requests.get(url, params=weather_parameters, headers=request_headers)
print(response.text)


############


# Обработка ошибок

# Задача
# Напишите функцию what_weather(), которую затем будете использовать в коде Анфисы:
# Выполните HTTP-запрос, поместив вызов функции get() внутрь блока try.
# Значения URL и параметров получите из функций make_url() (в неё нужно передать нужный город как аргумент city)
# и make_parameters().
# При «выбрасывании» исключения типа requests.ConnectionError — функция what_weather() должна возвращать сообщение
# об ошибке '<сетевая ошибка>'.
# Если код HTTP-ответа равен 200 (всё хорошо), верните из функции текст ответа. В противном случае функция должна
# вернуть строку '<ошибка на сервере погоды>'.

import requests

cities = [
    'Омск',
    'Калининград',
    'Челябинск',
    'Владивосток',
    'Красноярск',
    'Москва',
    'Екатеринбург'
]


def make_url(city):
    # в URL задаём город, в котором узнаем погоду
    return f'http://wttr.in/{city}'


def make_parameters():
    params = {
        'format': 2,  # погода одной строкой
        'M': ''  # скорость ветра в "м/с"
    }
    return params


def what_weather(city):
    # Напишите тело этой функции.
    # Не изменяйте остальной код!
    try:
        request = requests.get(make_url(city), params=make_parameters())
        # print(request.status_code)
        if request.status_code == 200:
            return request.text
        else:
            return '<ошибка на сервере погоды>'
    except requests.ConnectionError:
        return '<сетевая ошибка>'


print('Погода в городах:')
for city in cities:
    print(city, what_weather(city))


############


# Анфиса на все руки

# Задача
# В список запросов queries в функции runner() добавлены новые запросы про погоду:
# Коля, как погода?
# Соня, как погода?
# Антон, как погода?
# Научите Анфису отвечать на вопросы такого вида. Для этого:
# Добавьте в функцию process_friend() обработку ещё одного запроса 'как погода?'.
# Для получения ответа на этот вопрос используйте значение city — это город, в котором живёт друг.
# Затем вызовите функцию what_weather() — вы написали на прошлом уроке почти такую же.
# Она уже доступна в коде этого задания.
# Верните результат выполнения этой функции как результат process_friend().

import datetime as dt
import requests


DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Алексей': 'Калининград',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск',
    'Артём': 'Владивосток',
    'Петя': 'Михайловка'
}

UTC_OFFSET = {
    'Москва': 3,
    'Санкт-Петербург': 3,
    'Новосибирск': 7,
    'Екатеринбург': 5,
    'Нижний Новгород': 3,
    'Казань': 3,
    'Челябинск': 5,
    'Омск': 6,
    'Самара': 4,
    'Ростов-на-Дону': 3,
    'Уфа': 5,
    'Красноярск': 7,
    'Воронеж': 3,
    'Пермь': 5,
    'Волгоград': 3,
    'Краснодар': 3,
    'Калининград': 2,
    'Владивосток': 10
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def what_time(city):
    offset = UTC_OFFSET[city]
    city_time = dt.datetime.utcnow() + dt.timedelta(hours=offset)
    f_time = city_time.strftime("%H:%M")
    return f_time


def what_weather(city):
    url = f'http://wttr.in/{city}'
    weather_parameters = {
        'format': 2,
        'M': ''
    }
    try:
        response = requests.get(url, params=weather_parameters)
    except requests.ConnectionError:
        return '<сетевая ошибка>'
    if response.status_code == 200:
        return response.text
    else:
        return '<ошибка на сервере погоды>'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count = len(DATABASE)
        return f'У тебя {format_count_friends(count)}.'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE)
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def process_friend(name, query):
    if name in DATABASE:
        city = DATABASE[name]
        if query == 'ты где?':
            return f'{name} в городе {city}'
        elif query == 'который час?':
            if city not in UTC_OFFSET:
                return f'<не могу определить время в городе {city}>'
            time = what_time(city)
            return f'Там сейчас {time}'
        elif query == 'как погода?':
            return what_weather(city)
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


def process_query(query):
    elements = query.split(', ')
    if elements[0] == 'Анфиса':
        return process_anfisa(elements[1])
    else:
        return process_friend(elements[0], elements[1])


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?',
        'Алексей, который час?',
        'Артём, который час?',
        'Антон, который час?',
        'Петя, который час?',
        'Коля, как погода?',
        'Соня, как погода?',
        'Антон, как погода?'
    ]
    for query in queries:
        print(query, '-', process_query(query))


runner()


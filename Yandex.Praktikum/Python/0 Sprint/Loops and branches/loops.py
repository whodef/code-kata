# Циклы

# Задача 1
# Напечатайте с помощью цикла названия месяцев из списка months.

months = [
    'Январь',
    'Февраль',
    'Март',
    'Апрель',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
    'Декабрь'
]
for month in months:
    print(month)

# Задача 2
# Напечатайте приглашение на ужин: циклом выведите имена приглашённых из списка pigs.
# Опишите условие и тело цикла — и всё заработает.

pigs = ['Ниф-Ниф', 'Наф-Наф', 'Нуф-Нуф']
print('Дорогие свиньи!')

for pig in pigs:
    print(pig)

print('приглашаю вас на ужин!')
print('Любящий вас Волк.')

############

# Диапазоны от и до

# Задача 1
# В этом уроке четыре задачи. Напечатайте магическую мантру, она поможет справиться с ними:

# Я расправлюсь с задачей 1
# Я расправлюсь с задачей 2
# Я расправлюсь с задачей 3
# Я расправлюсь с задачей 4
# Я всех победю!

# Вместо многоточий вставьте необходимый код — имя переменной и диапазон.
# Внутреннюю переменную цикла можно назвать i: так традиционно называют переменную,
# принимающую числа из последовательного числового ряда.

for task in range(1, 5):
    print('Я расправлюсь с задачей', task)
print('Я всех победю!')

# Задача 2
# Если бы Джек, который построил дом, строил его из чисел, дом выглядел бы так:
# Это первый этаж.
# А это 2 этаж, он на один выше, чем этаж 1
# А это 3 этаж, он на один выше, чем этаж 2
# ...

# Постройте с помощью цикла десятиэтажный дом. Последней строкой цикл должен вывести такую:
# А это 10 этаж, он на один выше, чем этаж 9

print('Это первый этаж.')
# Первый этаж построен, начинайте строить со второго
for i in range(2, 11):
    # Здесь вместо многоточий
    # вставьте номер текущего этажа,
    # вычислите и вставьте номер предыдущего этажа.
    print('А это', i, 'этаж, он на один выше, чем этаж', int(i - 1))

# Задача 3
# Разверните год наоборот: напечатайте месяцы в обратном порядке.

months = [
    'Январь',
    'Февраль',
    'Март',
    'Апрель',
    'Май',
    'Июнь',
    'Июль',
    'Август',
    'Сентябрь',
    'Октябрь',
    'Ноябрь',
    'Декабрь'
]

for month in reversed(months):
    print(month)

# Задача 4
# Настало время великих стартов: Tesla улетела на гелиоцентрическую орбиту за Марсом,
# а вам предстоит отправить ракету с питоном на Сатурн.
# Сгенерируйте строку с обратным предстартовым отсчётом.
# Она должна выглядеть так:

# 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, поехали!

# Это задание очень похоже на пример со считалкой про зайца, этим можно воспользоваться.

countdown_str = ''

for i in reversed(range(0, 11)):
    countdown_str = countdown_str + str(i) + ', '
countdown_str = countdown_str + 'поехали!'

print(countdown_str)
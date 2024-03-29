# Задача 1
# Доработайте программу подсчёта тёплых дней в мае 2017 г. : допишите функцию comfort_count()
# так, чтобы она возвращала подсчитанное количество тёплых дней.

may_2017 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25,
            17, 19]


# Допишите эту функцию
def comfort_count(temperatures):
    count = 0
    for temp in temperatures:
        if 22 <= temp <= 26:
            count += 1
    # Функция должна вернуть значение переменной count
    return count


# Код ниже не изменяйте:
# вызовем функцию comfort_count(), передадим в неё список may_2017,
# результат работы сохраним в переменную nice_days
nice_days = comfort_count(may_2017)

# Напечатаем значение, сохранённое в nice_days
print('Количество тёплых дней в этом месяце:', nice_days)


# Задача 2
# Плотник Афанасий зачем-то решил построить из стекла и палок восемь одинаковых кубов; рёбра кубов будут из палок,
# а грани — из стекла. Ребро куба, по чертежам Афанасия, должно быть 3 метра.

# Допишите программу так, чтобы она печатала общую длину палок, необходимых для строительства восьми кубов.
# Функцию для подсчёта периметра одного куба Афанасий написал: эта функция принимает на вход длину ребра куба,
# а возвращает периметр куба — сумму длин всех его рёбер.
# Вызовите функцию calc_cube_perimeter() с аргументом 3 и присвойте возвращаемое функцией значение переменной
# one_cube_perimeter. Теперь в этой переменной будет храниться периметр одного куба.
# Вычислите суммарный периметр для восьми кубов и присвойте получившееся значение переменной full_length.

# Функция для вычисления периметра куба.
def calc_cube_perimeter(side):
    return side * 12


# Присвойте переменной one_cube_perimeter значение,
# которое вернёт функция calc_cube_perimeter() с аргументом 3:
# 3 метра - это длина ребра куба.

one_cube_perimeter = calc_cube_perimeter(3)

# Вычислите общую длину палок, необходимых
# для строительства 8 кубов,
# и сохраните это значение в переменную full_length
full_length = one_cube_perimeter * 8

# А теперь напечатаем результат (в этой строке ничего изменять не нужно)
print('Необходимый метраж палок для 8 кубов:', full_length)


# Задача 3
# Вычислим площадь стекла, необходимого для постройки восьми кубов. Кубы все одинаковые, длина ребра у кубов —
# три метра. Афанасий начал писать функцию, вычисляющую площадь стекла для одного куба, но потом отвлёкся
# и не дописал часть расчётов и инструкцию return.
# Допишите программу: вычислите общую площадь стекла, необходимого для постройки восьми кубов.

# Функция для вычисления площади куба.
def calc_cube_area(side):
    # Формулу для вычисления площади одной грани куба Афанасий написал:
    one_face = side * side

    # Вычислите полную площадь куба: у него шесть одинаковых граней.
    cube_area = one_face * 6

    # Удалите многоточие и допишите функцию так,
    # чтобы она возвращала полную площадь куба
    return cube_area


# Присвойте переменной one_cube_area значение,
# которое вернёт функция calc_cube_area() с аргументом 3:
# 3 метра - это длина ребра куба.
one_cube_area = calc_cube_area(3)

# Вычислите общую площадь стекла, необходимого
# для строительства 8 кубов,
# и сохраните это значение в переменную full_area
full_area = one_cube_area * 8

print('Необходимая площадь стекла для 8 кубов, кв.м:', full_area)

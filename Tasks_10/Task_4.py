"""
4. Возведение в степень.
Дано: два списка одинаковой длины: чисел X и степеней Y.

Задание: написать функцию, которая возвращает список [x1^y1, x2^y2, ..],
где X=[x1, x2, ..], Y=[y1, y2, ..].

Пример:
 X = [2, 3, 4], Y = [10, 11, 12], результат: [1024, 177147, 16777216]
"""


def exponentiate(base_list: list[float], exponent_list: list[int])\
        -> list[float]:
    numbers = [x**y for x, y in zip(base_list, exponent_list)]
    return numbers


def do_main():
    x = [2, 3, 4]
    y = [10, 11, 12]
    z = exponentiate(x, y)
    print(z)


if __name__ == '__main__':
    do_main()

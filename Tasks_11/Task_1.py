"""
1. Случайности не случайны.
Дано: n - целое число.

Задание: написать функцию-генератор, которая возвращает n дробных чисел из диапазона [0, n].
Используйте функцию random.uniform для генерации случайных чисел.

Пример:
 list(f(3)), результат: [0.460552766096591, 2.6440795402868016, 0.3830553232366699]
"""


import random


def generate_random_float(n, start_of_range = 0, end_of_range = 5):
    nums = [
        random.uniform(start_of_range, end_of_range) for i in range(n)
    ]
    return nums


if __name__ == '__main__':
    nums = list(generate_random_float(3))
    print(nums)

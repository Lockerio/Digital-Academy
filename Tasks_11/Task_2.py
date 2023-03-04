"""
2. Ленивое объединение
Дано: 2 списка произвольной длины.

Задание: написать функцию, которая возвращает результат объединения этих списков. Используйте функцию itertools.chain.

Пример:
 list(f([1, 2], [3, 4])), результат: [1, 2, 3, 4]
"""


import itertools


def merge_2_lists(list1, list2):
    return itertools.chain(list1, list2)


if __name__ == '__main__':
    list1 = ["a", 97, "c"]
    list2 = [1, 5, 9]
    print(list(merge_2_lists(list1, list2)))

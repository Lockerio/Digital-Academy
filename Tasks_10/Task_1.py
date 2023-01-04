"""
1. Градусник.
Дано: список градусов Цельсия.

Задание: написать функцию, которая преобразовывает исходный список градусов
Цельсия в список градусов Фаренгейта.

Пример:

 [39.2, 36.5, 37.3, 37.8], результат:
 [102.56, 97.700000000000003, 99.140000000000001, 100.03999999999999]
"""


def convert_celsius_to_fahrenheit(celsius_list: list[float]) -> list[float]:
    """
    Функция, преобразующая градусы Цельсия в Фаренгейта.
    :param celsius_list: Исходный список градусов Цельсия.
    :return: Получившийся список градусов Фаренгейта.
    """
    fahrenheit_list = [x * 9/5 + 32 for x in celsius_list]
    # Еще один вариант
    # fahrenheit_list = list(map(lambda x: (x * 9/5 + 32), celsius_list))
    return fahrenheit_list


def do_main():
    celsius_list = [39.2, 36.5, 37.3, 37.8]
    fahrenheit_list = convert_celsius_to_fahrenheit(celsius_list)
    print(fahrenheit_list)


if __name__ == "__main__":
    do_main()

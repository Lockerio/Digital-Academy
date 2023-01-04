"""
2. Длинномер.
Дано: список строковых значений.

Задание: написать функцию, которая возвращает список длин каждой строки.

Пример:
 ['Tina', 'Raj', 'Tom'], результат: [4, 3, 3]
"""


def calculate_length(string_list: list[str]) -> list[int]:
    """
    Функция, определяющая длину каждой строки в исходном списке.
    :param string_list: Исходный список строк.
    :return: Список длин строк.
    """
    length_list = list(map(len, string_list))
    return length_list


def do_main():
    string_list = ['Tina', 'Raj', 'Tom']
    length_list = calculate_length(string_list)
    print(f'{string_list} -> {length_list}')


if __name__ == "__main__":
    do_main()

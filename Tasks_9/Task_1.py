"""
1. Список из числа.
Дано: натуральное число N.

Задание: написать функцию, которая возвращает список всех цифр
этого числа в обратном порядке.

Пример:

 123, результат: [3, 2, 1]
"""


def set_int_value():
    """
    Функция ввода и проверки чисел.
    :return: Натуральное число.
    """
    while 1:
        try:
            x = input('Введите число: ')
            int_x = int(x)

            if int_x <= 0:
                raise Exception

            return int_x

        except ValueError:
            print('Ошибка. Вы можете ввести только натуральное число!')

        except Exception:
            print('Ошибка. Число должно быть больше 0!')


def get_list_of_ints(number):
    """
    Функция, перерабатывающая число в список с обратным порядком элементов.
    :param number: Натуральное число.
    :return: Список.
    """
    reverse_integer_dictionary = []
    while number:
        reverse_integer_dictionary.append(number % 10)
        number //= 10

    return reverse_integer_dictionary


user_int = set_int_value()
reverse_int = get_list_of_ints(user_int)
print(reverse_int)

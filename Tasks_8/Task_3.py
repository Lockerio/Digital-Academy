"""
3. Удвоенные нечетные.
Дано: x, y, z, n.

Задание: нужно получить список "удвоенных" нечетных чисел от 0 до n.

Пример:
 n = 5, результат: [2, 6]
"""
class DoubleUneven:
    """
    Класс для вычисления удвоенных нечетных чисел, в диапазоне
    [0, 'Введенное пользователем число'].
    """
    def __init__(self, number):
        self.number = number
        self.double_uneven_numbers = []

    def __repr__(self):
        return repr(self.number)

    @classmethod
    def set_number(cls):
        """
        Дополнительный конструктор, нужен для ввода с клавиатуры.
        Проверяет текст, который ввел пользователь.
        :return: Корректно введенное число.
        """
        while 1:
            try:
                user_input = input('Введите число: ')
                int_user_input = int(user_input)
                return cls(int_user_input)

            except Exception:
                print('Ошибка. Вы можете ввести только целое число.\n'
                      'Попробуйте еще раз.')

    def get_double_uneven_numbers(self):
        """
        Функция идет по нечетным числам, до введенного
        пользователем число, и удваивает их.
        :return: Список удвоенных нечетных чисел.
        """
        for i in range(self.number)[1::2]:
            self.double_uneven_numbers.append(i * 2)

        return self.double_uneven_numbers


number = DoubleUneven.set_number()
uneven_numbers = number.get_double_uneven_numbers()
print(f'Список нечетных удвоенных элементов: {uneven_numbers}')

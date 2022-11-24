"""
2. Перестановки.
Дано: x, y, z, n.

Задание: нужно получить список всех возможных перестановок чисел x, y, z,
где x + y + z != n.

Пример:

 x = 0 y = 0 z = 1 n = 2,
 результат: [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""


class Sequences:
    """
    Класс, который позволяет вывести все возможные последовательности
    переменных, а сумма этих переменных не равна введенному
    пользователем значением.
    """
    def __init__(self, user_sequence, incorrect_sum):
        self.variables_amount = 3
        self.user_sequence = user_sequence
        self.incorrect_sum = incorrect_sum
        self.correct_sequences = self.calculate_correct_sequences_3vars()

    @classmethod
    def set_data(cls):
        user_sequence = cls.set_user_sequence()
        incorrect_sum = cls.set_incorrect_sum()
        return cls(user_sequence, incorrect_sum)

    @staticmethod
    def set_user_sequence():
        """
        Функция, записывающая и проверяющая введенные пользователем переменные.
        :return: Список целых чисел.
        """
        n = 3
        variables_dictionary = []
        print('Введите последовательность ваших переменных.')

        for i in range(n):
            while 1:
                try:
                    user_input = input(f'Переменная №{i + 1}: ')
                    variable = int(user_input)

                    variables_dictionary.append(variable)
                    break

                except ValueError:
                    print('Ошибка. Введенное может быть только целым числом.')

        return variables_dictionary

    @staticmethod
    def set_incorrect_sum():
        while 1:
            try:
                user_input = input('Введите "нежелательную" сумму: ')
                variable = int(user_input)
                break

            except ValueError:
                print('Ошибка. Введенное может быть только целым числом.')

        return variable

    def calculate_correct_sequences_3vars(self):
        """
        Функция, составляющая список всех возможных последовательностей
        из введенных пользователем переменных. Работает только для
        3 переменных.

        Не знаю, как оптимизировать этот алгоритм для
        другого количества переменных.

        :return: Список -> все последовательности, сумма элементов которых
        не равна введенному пользователем числу.
        """
        n = self.variables_amount
        source_sequence = self.user_sequence
        sequences = []
        already_encountered_sequences = []

        for i in range(n):
            for j in range(n):
                for k in range(n):
                    new_sequence = [source_sequence[i], source_sequence[j],
                                    source_sequence[k]]

                    if new_sequence in already_encountered_sequences:
                        continue
                    elif sum(new_sequence) == self.incorrect_sum:
                        continue

                    already_encountered_sequences.append(new_sequence)
                    sequences.append(new_sequence)

        return sequences


my_sequence = Sequences.set_data()
print(f'Ответ: {my_sequence.correct_sequences}')

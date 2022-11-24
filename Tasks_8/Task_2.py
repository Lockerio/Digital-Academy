"""
2. Перестановки.
Дано: x, y, z, n.

Задание: нужно получить список всех возможных перестановок
чисел x, y, z, где x + y + z != n.

Пример: Добавить примеры! x = y = z = 1 n = 2, результат:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""


from math import factorial


class SequencesGenerator:
    def __init__(self, source_sequence):
        self.source_sequence = sorted(source_sequence)
        self.length = len(source_sequence)
        self.sequences_amount = factorial(self.length)
        self.list_of_sequences = []

    def __repr__(self):
        return repr(self.source_sequence)

    @classmethod
    def set_source_sequence(cls):
        """
        Дополнительный конструктор, нужен для ввода с клавиатуры.
        Проверяет текст, который ввел пользователь.
        :return: Корректно введенный список.
        """
        while 1:
            try:
                user_input = input('Введите список элементов через '
                                   'пробел: ')
                user_list = user_input.split()
                int_user_list = list(map(int, user_list))
                return cls(int_user_list)

            except Exception:
                print('Ошибка. В списке могут быть только целые числа.\n'
                      'Попробуйте еще раз.')

    def get_list_of_defined_sequences(self):
        self.list_of_sequences.append(self.source_sequence)

        for i in range(self.sequences_amount):
            new_sequence = self.generate_next_sequence()
            if new_sequence:
                self.list_of_sequences.append(new_sequence)
            else:
                break

        return self.list_of_sequences

    def generate_next_sequence(self):
        current_index = self.length - 2
        sequence = self.source_sequence[:]

        while (current_index != -1 and sequence[current_index] >=
               sequence[current_index + 1]):
            current_index -= 1

        if current_index == -1:
            return None

        index_to_change = self.length - 1

        while sequence[current_index] >= sequence[index_to_change]:
            index_to_change -= 1

        sequence[current_index], sequence[index_to_change] = \
            sequence[index_to_change], sequence[current_index]

        sequence = sequence[:current_index + 1] + sorted(sequence[current_index + 1:])
        self.source_sequence = sequence[:]
        return sequence


# Какой смысл этого задания? Если мы будем перебирать каждую
# последовательность, нам еще нужно перебирать последовательности,
# когда они равны нулю.

user_list = SequencesGenerator.set_source_sequence()
# user_list = SequencesGenerator([1, 3, 4])
print(user_list)

print(user_list.get_list_of_defined_sequences())

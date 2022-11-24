"""
[Junior] 4. Дешифратор.
Дано: шифровальная решетка (4 на 4) и зашифрованный пароль (4 на 4)
представлены, как массив строк.

Задание. Помогите Софи написать дешифратор для паролей, которые Никола
зашифровал с помощью шифровальной решетки.

Шифрорешетка - это квадрат 4 на 4 с четырьмя вырезанными окошками.
Поместите решетку на листе бумаги такого же размера с буквами, выписываете
первые 4 символа, которые видно в окошках (см. рисунок). Затем поверните
решетку на 90 градусов по часовой стрелке. Выпишите следующие символы и
повторите поворот. В итоге процедура повторяется 4 раза. Таким образом сложно
узнать пароль без специальной решетки.

Напишите программу, которая поможет проводить данную процедуру.

Пример:

 (('X...',
   '..X.',
   'X..X',
   '....'),
  ('itdf',
   'gdce',
   'aton',
   'qrdi'), результат: 'icantforgetiddqd'

 (('....',
   'X..X',
   '.X..',
   '...X'),
  ('xhwc',
   'rsqx',
   'xqzz',
   'fyzr')), результат: 'rxqrwsfzxqxzhczy'
"""


from numpy import rot90


class Decoder:
    """
    Класс, позволяющий корректно вводить зашифрованный пароль и шифровальную
    решетку, и с ее помощь расшифровать этот пароль.
    """
    def __init__(self, matrix_rank):
        self.matrix_rank = matrix_rank
        self.encrypted_password = self.set_encrypted_password()
        self.cipher_grill = self.set_cipher_grill()
        self.decrypted_password = ''

    @classmethod
    def set_matrix_rank(cls):
        """
        Функции для ввода ранга матрицы.
        :return: Целое положительное число -> ранг матрицы.
        """
        while 1:
            # Ввод и проверка значения ранга матрицы.
            try:
                user_input = input('Введите ранг матрицы: ')
                matrix_rank = int(user_input)

                if matrix_rank <= 0:
                    raise Exception

                return cls(matrix_rank)

            except ValueError:
                print('Ошибка. Ранг матрицы должен быть числом!'
                      '\nПопробуйте еще раз.')

            except Exception:
                print('Ошибка. Ранг матрицы может быть только положительным!'
                      '\nПопробуйте еще раз.')

    def set_encrypted_password(self):
        """
        Функция, которая позволяет ввести зашифрованный пароль.
        :return: Матрица -> зашифрованный пароль.
        """
        n = self.matrix_rank
        matrix = []

        # Поочередно вводим n строк матрицы,
        # попутно проверяя их на корректность.
        for i in range(n):
            while 1:
                list_elements = input(f'Строка {i + 1}. Введите {n}'
                                      f' элемента(ов) через пробел: '
                                      ).split()

                # Если во введенной строке не n символа, просим
                # пользователя ввести еще раз.
                if len(list_elements) != n:
                    print(f'Ошибка в строке {i + 1}. Вы можете ввести только '
                          f'{n} символа(ов).')
                    continue

                matrix.append(list_elements)
                break

        return matrix

    def set_cipher_grill(self):
        """
        Функция, которая позволяет ввести шифровальную решетку
        и проверить ее на корректность.
        :return: Матрица -> шифровальная решетка.
        """
        n = self.matrix_rank
        matrix = []

        # Поочередно вводим n строк матрицы,
        # попутно проверяя их на корректность.
        for i in range(n):
            while 1:
                try:
                    list_elements = input(f'Строка {i + 1}. Введите {n} '
                                          'элемента(ов) ("X" или ".") '
                                          'через пробел: ').split()

                    # Если во введенной строке не n символа,
                    # просим пользователя ввести еще раз.
                    if len(list_elements) != n:
                        print(f'Ошибка в строке {i + 1}. Вы можете ввести'
                              f' только {n} символа(ов).')
                        continue

                    # Проверка введенных элементов.
                    # Если введенные символы не являются "X" или ".",
                    # вызывается исключение.
                    for j in list_elements:
                        if j not in ['X', '.']:
                            raise Exception

                    matrix.append(list_elements)
                    break

                except Exception:
                    print(f'Ошибка в строке {i + 1}. Вы можете ввести только '
                          'символы: "X" или ".".')

        return matrix

    def get_decrypted_password(self):
        """
        Основная функция, которая позволяет определить расшифрованный пароль.
        :return: Строка -> расшифрованный пароль.
        """
        matrix = self.cipher_grill
        n = self.matrix_rank
        marked_elements = []
        rotations_amount = 4

        # 4 раза поворачиваем матрицу решетки и запоминаем позицию
        # каждого "X" в текущей итерации.
        for rotation in range(rotations_amount):
            for i in range(n):
                for j in range(n):
                    if matrix[i][j] == 'X':
                        marked_elements.append([i, j])

            # Идем по списку позиций "X" и добавляем символ из матрицы
            # нерасшифрованного пароля, позиции текущего "X". После завершения
            # цикла обнуляем временную переменную позиций "X". И поворачиваем
            # матрицу решетки на 90 градусов по часовой стрелке.
            for i in marked_elements:
                self.decrypted_password += self.encrypted_password[i[0]][i[1]]

            marked_elements = []
            matrix = rot90(matrix, k=-1)

        return self.decrypted_password


cipher = Decoder.set_matrix_rank()
decrypted_password = cipher.get_decrypted_password()
print(f'Расшифрованный пароль: {decrypted_password}')

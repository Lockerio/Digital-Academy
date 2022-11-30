"""
[Junior-] 4. Пешки.
Дано: координаты расставленных пешек в виде набора строк.

Задание. Шахматы известны по всему миру, и практически всем людям знакомы
их основные правила игры. В игре используется набор фигур, которые могут
ходить по игровому полю различными способами, что обеспечивает огромное
количество различных игровых комбинаций (к примеру, количество возможных
шахматных партий оценивается Шенноном в 10^118). В этой задаче мы будем
исследовать правила игры пешками.

Шахматы - это стратегическая игра двух игроков, которая разыгрывается на
игровой доске с клетками, расположенными в восьми рядах
(называемых горизонталями и обозначаемых цифрами от 1 до 8)
и в восьми колонках (называемых вертикалями и обозначаемых буквами от a до h).
Каждая клетка доски идентифицируется уникальной парой координат,
состоящей из буквы и цифры (например, "a1", "h8", "d6"). В этой задаче
мы будем иметь дело только с пешками. Пешка может бить пешку противника,
которая находится перед ней в соседней клетке по диагонали справа
или слева, переходя в эту клетку. У белых пешек клетки перед ними
имеют номер горизонтали на единицу больше.

Сама по себе пешка является слабой фигурой, но мы можем использовать до восьми
пешек для построения оборонительной стены. Стратегия оборонительной стены
основывается на защите друг друга. Пешка защищена, если её клетка находится
под ударом другой своей пешки. На игровом поле находятся только белые пешки.
Вы должны реализовать функцию, позволяющую определить
сколько пешек защищены в этой позиции.

Вам предоставляется набор координат, в которых расставлены белые пешки.
Вы должны подсчитать количество защищенных пешек.

Примеры:

 {"b4", "d4", "f4", "c3", "e3", "g5", "d2"}, результат: 6
 {"b4", "c4", "d4", "e4", "f4", "g4", "e5"}, результат: 1
"""


def define_pawns_indexes(array):
    """
    Функция, разделяющая пользовательский список позиций пешек,
    на отдельные два списка: позиция в строке (буква) и в столбце (цифра).
    :param array: Пользовательский список позиций пешек.
    :return: Список двух списков.
    """
    letters = []
    numbers = []

    for i in array:
        letters.append(i[0])
        numbers.append(int(i[1]))

    return [letters, numbers]


def define_defended_pawns(array):
    """
    Функция, определяющая защищенные пешки.
    :param array: Пользовательский список позиций пешек.
    :return: Множество защищенных пешек.
    """
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]
    letter_index = 0
    number_index = 1
    defended_positions = set()

    # Разбиваем входной список еще на два списка: позиция
    # в строке (буква) и в столбце (цифра).
    pawns_positions = define_pawns_indexes(array)

    for i in zip(pawns_positions[letter_index],
                 pawns_positions[number_index]):
        letter = i[letter_index]
        number = i[number_index]

        if number != numbers[-1]:
            new_defend_number = numbers[numbers.index(number) + 1]

            if letter == letters[0]:
                new_defend_letter = letters[letters.index(letter) + 1]
                defended_positions.add(new_defend_letter
                                       + str(new_defend_number))

            elif letter == letters[-1]:
                new_defend_letter = letters[letters.index(letter) - 1]
                defended_positions.add(new_defend_letter
                                       + str(new_defend_number))

            else:
                new_defend_letter = letters[letters.index(letter) + 1]
                defended_positions.add(new_defend_letter
                                       + str(new_defend_number))
                new_defend_letter = letters[letters.index(letter) - 1]
                defended_positions.add(new_defend_letter
                                       + str(new_defend_number))

    defended_pawns = set.intersection(set(array), defended_positions)
    return defended_pawns


pawns_matrix = ["b4", "d4", "f4", "c3", "e3", "g5", "d2"]
defended_pawns = define_defended_pawns(pawns_matrix)
print(f'Всего {len(defended_pawns)} защищенных пешек: {defended_pawns}')

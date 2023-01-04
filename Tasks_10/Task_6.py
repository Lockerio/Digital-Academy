"""
6. Самый большой прямоугольник.
Дано: список высот всех столбцов в гистограмме (список целых чисел).

Задание: У вас есть гистограмма. Попробуйте найти размер самого большого
прямоугольника, который можно построить из столбцов гистограммы.

Примеры:
 largest_histogram([5]) == 5
 largest_histogram([5, 3]) == 6
 largest_histogram([1, 1, 4, 1]) == 4
 largest_histogram([1, 1, 3, 1]) == 4
 largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8
"""


def find_largest_rectangle(hist: list[int]) -> int:
    """
    Функция, которая находит больший прямоугольник из вершин гистограммы.
    :param hist: Пользовательская гистограмма.
    :return: Площадь большего прямоугольника.
    """
    '''
    Работает это следующим образом: 
    1) Находим множество высот, используем его как цикл;
    2) В каждой итерации идем по всей гистограмме;
    3) Если высота в гистограмме не меньше текущей высоты в множестве,
       тогда прибавляем к временной площади значение уникальной высоты;
    4) Если высота в гистограмме не меньше текущей высоты в множестве,
       тогда сравниваем большую площадь со временной, если вторая больше,
       то меняем значение максимальной на значение временной;
    5) По завершению внутреннего цикла еще раз сравниваем большую площадь
       со временной.
    '''
    max_square = 0
    unique_columns = set(hist)

    for unique_column in unique_columns:
        temp_square = 0
        for i in hist:
            if i < unique_column:
                if temp_square > max_square:
                    max_square = temp_square

                temp_square = 0
                continue

            temp_square += unique_column

        if temp_square > max_square:
            max_square = temp_square

    return max_square


def do_main():
    histogram = [2, 1, 4, 5, 1, 3, 3]
    print(find_largest_rectangle(histogram))


if __name__ == '__main__':
    do_main()

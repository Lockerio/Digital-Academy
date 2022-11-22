class GhostAgeCalculator:
    """
    Класс, позволяющий рассчитать возраст призрака, по его прозрачности.
    """
    def __init__(self, degree_of_transparency):
        self.degree_of_transparency = degree_of_transparency
        self.ghost_age = self.calculate_ghost_age()

    @classmethod
    def set_degree_of_transparency(cls):
        """
        Функции для ввода степени прозрачности призрака.
        :return: Целое положительное число -> степень прозрачности призрака.
        """
        while 1:
            # Ввод и проверка значения степени прозрачности.
            try:
                user_input = input('Введите степень прозрачности призрака: ')
                degree_of_transparency = int(user_input)

                if not 0 <= degree_of_transparency <= 10000:
                    raise Exception

                return cls(degree_of_transparency)

            except ValueError:
                print('Ошибка. Степень прозрачности должна быть '
                      'числом!\nПопробуйте еще раз.')

            except Exception:
                print('Ошибка. Степень прозрачности должна быть '
                      'в диапазоне [0; 10000]!\nПопробуйте еще раз.')

    def calculate_ghost_age(self):
        """
        Функция, вычисляющая возраст призрака.
        :return: Целое положительное число -> возраст призрака.
        """
        fibonacci_numbers = [0, 1]
        transparency_to_lose = 10000
        death_age = 5000
        ghost_age = 0

        # Призрак только что родился.
        if self.degree_of_transparency == transparency_to_lose:
            return 0

        # Вычисляем возраст призрака.
        while transparency_to_lose != self.degree_of_transparency:
            # Если возраст является числом Фибоначчи, вычитаем это значение
            # из степени прозрачности. Иначе прибавляем к ней единицу.
            if ghost_age in fibonacci_numbers:
                transparency_to_lose -= ghost_age
            else:
                transparency_to_lose += 1

            # Генерируем новое число Фибоначчи.
            fibonacci_numbers.append(fibonacci_numbers[-2] +
                                     fibonacci_numbers[-1])
            ghost_age += 1

            # Призрак исчез, возраст неизвестен.
            if ghost_age == death_age:
                return None

        return ghost_age - 1


ghost_Ivan = GhostAgeCalculator.set_degree_of_transparency()
print(f'Степень прозрачности призрака - {ghost_Ivan.degree_of_transparency}'
      f'\nВозраст призрака - {ghost_Ivan.ghost_age}')

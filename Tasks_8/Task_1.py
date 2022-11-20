class Array:
    """
    Этот класс нужен для инициализации списка и поиска не уникальных
    элементов в нем.
    """
    def __init__(self, user_list):
        self.user_list = user_list

    @classmethod
    def set_list(cls):
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

    def get_not_unique_elements(self):
        """
        Функция поиска не уникальных элементов.
        Перебирает элементы введенного списка, если элемент встречается в
        исходном списке не один раз, то вносим его в дополнительный список.
        :return: Список не уникальных элементов.
        """
        array = self.user_list
        not_unique_elements = [i for i in array if array.count(i) > 1]
        return not_unique_elements


user_list = Array.set_list()
not_unique_elements = user_list.get_not_unique_elements()
print(f'Ответ: {not_unique_elements}')

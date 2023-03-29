"""
1. Друзья.
Дано: n - целое число.

Задание:

Создайте класс "Friends", который должен содержать данные о людях (их имена) и о связях между ними. Имена представлены в виде текстовых строк, чувствительных к регистру. Связи не имеют направлений, то есть, если существует связь "sofia" с "nikola", это справедливо и в обратную сторону.

class Friends(connections)

Возвращает новый объект, экземпляр класса Friends. Параметр "connections" имеет тип "итерируемый объект", содержащий множества (set) с двумя элементами в каждом. Каждая связь содержит два имени в виде текстовых строк. Связи могут повторяться в параметре инициализации, но в объекте хранятся только уникальные пары. Каждая связь имеет только два состояния - присутствует или не присутствует.

# >>> Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"})
# >>> Friends([{"1", "2"}, {"3", "1"}])

add(connection)

Добавляет связь в объект. Параметр "connection" является множеством (set) из двух имен (строк). Возвращает True, если заданная связь новая и не присутствует в объекте. Возвращает False, если заданная связь уже существует в объекте.

# >>> f = Friends([{"1", "2"}, {"3", "1"}])
# >>> f.add({"1", "3"})
False
# >>> f.add({"4", "5"})
True

remove(connection)

Удаляет связь из объекта. Параметр "connection" является множеством (set) из двух имен (строк). Возвращает True, если заданная связь существует в объекте. Возвращает False, если заданная связь не присутствует в объекте.

# >>> f = Friends([{"1", "2"}, {"3", "1"}])
# >>> f.remove({"1", "3"})
True
# >>> f.remove({"4", "5"})
False

names()

Возвращает множество (set) имён. Множество содержит имена, которые имеют хотя бы одну связь.

# >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "d"})
# >>> f.names()
{"a", "b", "c", "d"}
# >>> f.remove({"d", "c"})
True
# >>> f.names()
{"a", "b", "c"}

connected(name)

Возвращает множество (set) имён, которые связаны с именем, заданным параметром "name". Если "name" не присутствует в объекте, возвращается пустое множество (set).

# >>> f = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"})
# >>> f.connected("a")
{"b", "c"}
# >>> f.connected("d")
set()
# >>> f.remove({"c", "a"})
True
# >>> f.connected("c")
{'b'}

В этом задании все входные данные корректны, и выполнять их проверку не обязательно.
"""


class Friends:
    def __init__(self, friends: list):
        self.friends = []
        for connection in friends:
            self.add(connection)

    def __repr__(self):
        return repr(self.friends)

    def add(self, connection: set) -> bool:
        if connection in self.friends:
            return False
        self.friends.append(connection)
        return True

    def remove(self, connection: set) -> bool:
        if connection in self.friends:
            self.friends.remove(connection)
            return True
        return False

    def define_unique_names(self) -> set:
        unique_names = set()
        for connection in self.friends:
            for name in connection:
                unique_names.add(name)

        return unique_names

    def connected(self, src_name) -> set:
        connections = set()
        for connection in self.friends:
            if src_name in connection:
                for name in connection:
                    if name == src_name:
                        continue
                    connections.add(name)

        return connections


if __name__ == '__main__':
    src_list = [{"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}]
    print(f"Исходный список: {src_list}")
    friends = Friends(src_list)
    print(f"Обработанный список: {friends}\n\n")

    # Добавление
    # Уже имеющаяся связь
    print("Добавим связь {'a', 'b'}")
    answer = friends.add({"a", "b"})
    print(f"Ответ функции: {answer}")
    print(f"Получившийся список: {friends}\n")

    # Связи нет в списке
    print("Добавим связь {'z', 'a'}")
    answer = friends.add({"z", "a"})
    print(f"Ответ функции: {answer}")
    print(f"Получившийся список: {friends}\n\n")


    # Удаление
    # Уже имеющаяся связь
    print("Удалим связь {'a', 'b'}")
    answer = friends.remove({"a", "b"})
    print(f"Ответ функции: {answer}")
    print(f"Получившийся список: {friends}\n")

    # Связи нет в списке
    print("Удалим связь {'Pasha', 'Pivo'}")
    answer = friends.remove({"a", "b"})
    print(f"Ответ функции: {answer}")
    print(f"Получившийся список: {friends}\n\n")


    # Уникальные имена
    print(f"Вернем уникальные имена: {friends.define_unique_names()}\n")

    print("Удалим связь {'z', 'a'}")
    answer = friends.remove({"z", "a"})
    print(f"Ответ функции: {answer}")
    print(f"Получившийся список: {friends}\n")

    print(f"Вернем уникальные имена: {friends.define_unique_names()}\n\n")

    # Связи по имени
    names = ["a", "b", "c", "Pasha"]
    for name in names:
        print(f"Вычислим связи {name}: {friends.connected(name)}")

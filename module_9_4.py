"""
Домашнее задание по теме "Создание функций на лету"
"""
"""
Lambda-функция:
Необходимо составить lambda-функцию для следующего выражения - list(map(?, first, second)).
Результатом должен быть список совпадения букв в той же позиции.
"""

first = 'Мама мыла раму'
second = 'Рамена мало было'

result = list(map(lambda x, y: x == y, first, second))
print(result)

"""
Замыкание:
Напишите функцию get_advanced_writer(file_name), принимающую название файла для записи.
Внутри этой функции, напишите ещё одну - write_everything(*data_set),
где *data_set - параметр принимающий неограниченное количество данных любого типа.
"""

def get_advanced_writer(file_name):
    file = open(file_name, 'a', encoding='utf-8')

    def write_everything(*data_set):
        for i in data_set:
            file.write(str(i) + '\n')
        file.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

"""
Метод __call__:
Создайте класс MysticBall, объекты которого обладают атрибутом words хранящий коллекцию строк.
В этом классе также определите метод __call__ который будет случайным образом выбирать слово
из words и возвращать его. Для случайного выбора с одинаковой вероятностью для каждого данного
в коллекции можете использовать функцию choice из модуля random.
"""

from random import choice

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)


first_ball = MysticBall('Да', 'Нет', 'Наверное', 'Может быть', 'Конечно')
print(first_ball())
print(first_ball())
print(first_ball())


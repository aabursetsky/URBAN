"""
Задача "Многопроцессное считывание":
Необходимо считать информацию из нескольких файлов одновременно, используя многопроцессный подход.
"""
import multiprocessing
from datetime import datetime

"""
Создайте функцию read_info(name), где name - название файла. Функция должна:
1. Создавать локальный список all_data.
2. Открывать файл name для чтения.
3. Считывать информацию построчно (readline), пока считанная строка не окажется пустой.
4. Во время считывания добавлять каждую строку в список all_data.
"""
def read_info(name):
    all_data = []
    file_info =  open(name, "r")
    while True:
        line = file_info.readline()
        all_data.append(line)
        if not line:
            break

"""
1.  Создайте список названий файлов в соответствии с названиями файлов архива.
2.  Вызовите функцию read_info для каждого файла по очереди (линейно) и
    измерьте время выполнения и выведите его в консоль.
3.  Вызовите функцию read_info для каждого файла, используя многопроцессный подход:
    контекстный менеджер with и объект Pool. Для вызова функции используйте метод map,
    передав в него функцию read_info и список названий файлов.
    Измерьте время выполнения и выведите его в консоль.
"""
if __name__ == '__main__':
    filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]
    start = datetime.now()
# Линейный вызов
#    for names in filenames:
#        read_info(names)
# 0:00:20.904814

# Многопроцессный
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
# 0:00:08.755009
    end = datetime.now()
    print(end - start)


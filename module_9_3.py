"""
Домашнее задание по теме "Генераторные сборки"
1. В переменную first_result запишите генераторную сборку, которая высчитывает
   разницу длин строк из списков first и second, если их длины не равны. Для перебора
   строк попарно из двух списков используйте функцию zip.
2. В переменную second_result запишите генераторную сборку, которая содержит результаты
   сравнения длин строк в одинаковых позициях из списков first и second. Составьте эту
   сборку НЕ используя функцию zip. Используйте функции range и len.
"""

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(x[0]) - len(x[1]) for x in zip(first, second) if len(x[0]) != len(x[1]))
second_result = (len(first[x]) == len(second[x]) for x in range(0 ,len(first)))

print(list(first_result))
print(list(second_result))

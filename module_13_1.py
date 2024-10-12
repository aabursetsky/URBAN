"""
Задача "Асинхронные силачи":
Необходимо сделать имитацию соревнований по поднятию шаров Атласа.
Напишите асинхронную функцию start_strongman(name, power), где name - имя силача,
power - его подъёмная мощность. Реализуйте следующую логику в функции:
1. В начале работы должна выводиться строка - 'Силач <имя силача> начал соревнования.'
2. После должна выводиться строка - 'Силач <имя силача> поднял <номер шара>'
   с задержкой обратно пропорциональной его силе power.
   Для каждого участника количество шаров одинаковое - 5.
3. В конце поднятия всех шаров должна выводится строка 'Силач <имя силача> закончил соревнования.'

Также напишите асинхронную функцию start_tournament, в которой создаются 3 задачи для функций start_strongman.
Имена(name) и силу(power) для вызовов функции start_strongman можете выбрать самостоятельно.
После поставьте каждую задачу в ожидание (await).
Запустите асинхронную функцию start_tournament методом run.
"""

import asyncio

async def start_strongman(name, power):
    time_wait = 60
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6):
        await asyncio.sleep(time_wait / power)
        print(f'Силач {name} поднял {i}-й шар')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Pasha', 3))
    task2 = asyncio.create_task(start_strongman('Denis', 4))
    task3 = asyncio.create_task(start_strongman('Apollon', 5))
    await task1
    await task2
    await task3

if __name__ == '__main__':
    asyncio.run(start_tournament())

"""
Силач Pasha начал соревнования.
Силач Denis начал соревнования.
Силач Apollon начал соревнования.
Силач Apollon поднял 1-й шар
Силач Denis поднял 1-й шар
Силач Pasha поднял 1-й шар
Силач Apollon поднял 2-й шар
Силач Denis поднял 2-й шар
Силач Apollon поднял 3-й шар
Силач Pasha поднял 2-й шар
Силач Denis поднял 3-й шар
Силач Apollon поднял 4-й шар
Силач Pasha поднял 3-й шар
Силач Denis поднял 4-й шар
Силач Apollon поднял 5-й шар
Силач Apollon закончил соревнования.
Силач Denis поднял 5-й шар
Силач Denis закончил соревнования.
Силач Pasha поднял 4-й шар
Силач Pasha поднял 5-й шар
Силач Pasha закончил соревнования.
"""
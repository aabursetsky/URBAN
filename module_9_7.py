"""
Декораторы в Python
"""

#Напишите 2 функции:
# 1. Функция, которая складывает 3 числа (sum_three)
# 2. Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
# и "Составное" в противном случае.

def is_prime(func):
    def wrapper(*args):
        number = func(*args)
        prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break
            prime = True

        if prime:
            print('Простое')
        else:
            print('Составное')

        return number
    return wrapper

@is_prime
def sum_three(first, second, trird):
    return first + second + trird

result = sum_three(2, 3, 6)
print(result)

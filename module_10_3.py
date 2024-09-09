"""
Задача "Банковские операции":
"""
"""
Методы объекта:
Метод deposit:
Будет совершать 100 транзакций пополнения средств.
Пополнение - это увеличение баланса на случайное целое число от 50 до 500.
Если баланс больше или равен 500 и замок lock заблокирован - lock.locked(), то разблокировать его методом release.
После увеличения баланса должна выводится строка "Пополнение: <случайное число>. Баланс: <текущий баланс>".
Также после всех операций поставьте ожидание в 0.001 секунды, тем самым имитируя скорость выполнения пополнения.
Метод take:
Будет совершать 100 транзакций снятия.
Снятие - это уменьшение баланса на случайное целое число от 50 до 500.
В начале должно выводится сообщение "Запрос на <случайное число>".
Далее производится проверка: если случайное число меньше или равно текущему балансу, то произвести снятие, уменьшив
balance на соответствующее число и вывести на экран "Снятие: <случайное число>. Баланс: <текущий баланс>".
Если случайное число оказалось больше баланса, то вывести строку "Запрос отклонён, недостаточно средств" и
заблокировать поток методом acquiere.
"""

import threading
from time import sleep
from random import randint


class Bank:
    balance = 0
    lock = threading.Lock()
    last_d_transaction = 100
    last_t_transaction = 100

    def deposit(self):
        while self.last_d_transaction > 0:
            resupply = randint(50, 500)
            #            print(self.lock.locked())
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            else:
                self.balance = self.balance + resupply
                self.last_d_transaction -= 1
                print(f'Пополнение: {resupply}. Баланс: {self.balance}')
                sleep(0.001)

    def take(self):
        while self.last_t_transaction > 0:
            waste = randint(50, 500)
            print(f'Запрос на {waste}')
            if self.balance >= waste:
                self.balance = self.balance - waste
                print(f'Снятие: {waste}. Баланс: {self.balance}')
                self.last_t_transaction -= 1
                sleep(0.001)
            else:
                print(f'Запрос отклонён, недостаточно средств')
                try:
                    self.lock.acquire()
                finally:
                    self.lock.release()
                    if self.last_d_transaction == 0 and self.balance < 50:
                        self.last_t_transaction = 0


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')

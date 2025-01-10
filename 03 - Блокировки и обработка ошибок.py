# Блокировки и обработка ошибок
# Задача "Банковские операции"

import threading
import time
import random

counter = 0
class Bank:
    lock = threading.Lock()
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self):
        for i in range(100):
            increase = random.randint(50,500)
            self.balance += increase
            time.sleep(0.001)

            print (f'№ {i+1} - Пополнение: {increase}. Баланс: {self.balance}')
            if self.balance > 499 and self.lock.locked():
                self.lock.release()

    def take(self):
        for i in range(100):
            decrease = random.randint(50,500)
            print (f'Запрос на {decrease}.')
            if decrease <= self.balance:
                self.balance -= decrease
                time.sleep(0.001)

                print (f'№ {i+1} - Снятие: {decrease}. Баланс: {self.balance}')
            else:
                print (f'Запрос отклонён, недостаточно средств')
                self.lock.acquire()
            if self.balance > 499 and self.lock.locked():
                self.lock.release()


bk = Bank()

th1 = threading.Thread(target=Bank.deposit, args=(bk,))

th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()


print(f'Итоговый баланс: {bk.balance}')


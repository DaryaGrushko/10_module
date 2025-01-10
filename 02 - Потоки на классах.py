# Потоки на классах
# Задача "За честь и отвагу!"

import threading
import time

class Knight(threading.Thread):
    counter = 0
    army = 100

    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print (f'{self.name}, на нас напали!')
        time.sleep(1)
        while self.army:
            self.army -= self.power
            self.counter += 1
            print (f'{self.name} сражается {self.counter} дней, осталось {self.army} воинов.')

        print (f'{self.name} одержал победу спустя {self.counter} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight('Sir Galahad', 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print ('Все битвы закончились!')


# Создание потоков

import threading
import time

def wite_words(word_count, file_name):
   # print ('word_count = ', word_count, ', file_name = ', file_name)
    with open(file_name, 'w', encoding='utf8') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i+1} \n')
    time.sleep(1)
    print (f'Завершилась запись в файл {file_name}\n')

start_time = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')

finish_time = time.time()
print (f'Время в миллисекундах:{(finish_time-start_time)*1000}')

print ('-------------------------')
start_time = time.time()
thread1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'), daemon=True) #поток создается
thread2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'), daemon=True)
thread3 = threading.Thread(target=wite_words, args=(200, 'example7.txt'), daemon=True)
thread4 = threading.Thread(target=wite_words, args=(100, 'example8.txt'), daemon=True)


thread1.start() #запускаем  поток
thread2.start()
thread3.start()
thread4.start()

thread1.join() # ждать
thread2.join()
thread3.join()
thread4.join()

finish_time = time.time()
print (f'Время в миллисекундах:{(finish_time-start_time)*1000}')

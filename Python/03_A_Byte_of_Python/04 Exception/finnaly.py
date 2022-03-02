''' finnaly

'''

import time

file = open('text.txt', 'r', encoding='UTF-8')

try:
    while True:
        line = file.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)
except KeyboardInterrupt :
    print(str(' Отмена чтения файла! ').center(40,'-'))
finally:
    file.close()
    print(str(' Закрытие файла ').center(40,'-'))

file.close
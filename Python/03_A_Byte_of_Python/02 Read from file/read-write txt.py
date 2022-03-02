''' read/write txt

просто записывает в файл и считывает из него с последующим выводом''' 


text = '''\
Многострочный текст
Вторая строка
Важная третья строка
Зкалючительная четвёртая строка
'''

file = open('text.txt', 'w', encoding='UTF-8')
file.write(text)
file.close()

file = open('text.txt', 'r', encoding='UTF-8')

while True:
    line = file.readline()
    if len(line) == 0:
        break
    print(line, end='')

file.close

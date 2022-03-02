''' exceptions

отлавливает исключение'''

class ShortInputException(Exception):
    def __init__(self, lengh, atleast):
        Exception.__init__(self)
        self.lengh = lengh
        self.atleast = atleast

try:
    min_len = 4
    text = input('Введите строку длиной больше трёх символов:')
    if len(text) < min_len:
        raise ShortInputException(len(text), min_len)
except EOFError:
    print('введен символ конца файла')
except KeyboardInterrupt:
    print('\n'+'отмена!')
except ShortInputException as sh_ex:
    print('''ShortInputException. Введена строка недостаточной длины. 
Длина введёной строки {0}, минимальная длина {1}'''.format(sh_ex.lengh, sh_ex.atleast))
else: 
    print('Введена строка длинной {lengh}'.format(lengh = len(text)))
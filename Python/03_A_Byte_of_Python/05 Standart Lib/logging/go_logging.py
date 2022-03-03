import os, platform, logging

if platform.platform().startswith('Windows'):
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),os.getenv('HOMEPATH'),'logging_py.log')
else:
    logging_file = os.path.join(os.getenv('HOME'),'logging_py.log')

print('Сохраняем файл логов в ', logging_file)

logging.basicConfig(
    level=logging.DEBUG,
    style='{',
    format='{asctime} : {levelname:>7s} : {message}',
    filename=logging_file,
    filemode='w',
    encoding='UTF-8'
)

logging.debug('Начало программы')
logging.info('Операция в программе')
logging.warning('В программе ошибка')


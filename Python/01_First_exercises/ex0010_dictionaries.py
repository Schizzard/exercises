# Learning dictionaries

phones = {
    'MoneyQuick' : '88005553535',
    'FreeHolydays' : '83452468119'
}

print(phones)           # {'MoneyQuick': '88005553535', 'FreeHolydays': '83452468119'}

phones['nice'] = '69420'
print(phones['nice'])   # 69420


print('Введите имя для поиска (точное совпадение)') # find
find = str(input())

if find in phones :
    print(phones[find])
else :
    print('Такой записи нет')


music = {
    "rap": ["Каста", "Ноггано", "Guf"],             # container in container
    "rock": ["Психея", "Аматори", "Ария"],
    "djs": ["Momentum", "Keo5na"]
}
print(music["rock"])     # ['Психея', 'Аматори', 'Ария']
print(music["rock"][1])     # Аматори
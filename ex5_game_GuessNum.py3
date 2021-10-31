# Game "guess the number"

ext = 0
while ext != 1 :
    import random
    r_int = random.randint(1, 6)
    print("Бросаю кубик! Угадай число от 1 до 6!!!")
    g_int = int(input())

    while g_int > 6 or g_int < 1 :
        print("Ты ввёл не от 1 до 6")
        print("Введи как следует")
        g_int = int(input())

    if g_int == r_int :
        print("Ты угадал! Выпало действительно ", r_int)
    else :
        print("Не повезло! Выпало ", r_int)

    print("Выход? 1 - да")
    ext = int(input())
    if ext == 1 : exit
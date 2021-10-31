ex = 0
while ex != 1:
    print("Введите первое число:")
    num1 = int(input())

    print("Выберите действие (введите номер действия от 1 до 4)")
    print("1. +")
    print("2. -")
    print("3. *")
    print("4. /")
    act = int(input())

    print("Введите второе число:")
    num2 = int(input())

    if act == 1 :
        print("Результат = ", num1 + num2)
    if act == 2 :
        print("Результат = ", num1 - num2)
    if act == 3 :
        print("Результат = ", num1 * num2)
    if act == 4 :
        if num2 != 0:
            print("Результат = ", num1 / num2)
        else:
            print("Делить на ноль нельзя!")
    
    print("Выйти? 1=да")
    ex = int(input())
# Better calc
# Learn exceptions

try :
    num1 = int(input("Введите первое число (делимое): "))
    num2 = int(input("Введите второе число (делитель): "))
except ValueError :
    print('Было введено не число.')
    # raise SystemExit
    quit()

try :
    print("Результат = ", num1 / num2)

except ZeroDivisionError :
    print('На ноль делить нельзя!')
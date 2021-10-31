# Learn Functions

def even_оr_odd(x=0) :      # =0 - by default (x is optional). 
    if x % 2 == 0 :         # This is bad example for show optional var.
        return True
    else :
        return False

print('Введите число для проверни на чётность/нечётность')
num = int(input())
answer = even_оr_odd(num)

if answer :
    print('Введённое число - чётное')
else :
    print('Введённое число - нечётное')
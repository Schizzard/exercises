# Step 3
'''
print(True if -15 < a <= 12 or 14 < a < 17 or 19<=a else False)
'''

# Solve 1 (my)
a, b, c = (input() for _ in '123')
if c in ['/','mod','div'] and float(b)==0.0: 
    print('Деление на 0!')
else:
    a = str('('+str(float(a))+')'+'{0}'+'('+str(float(b))+')')
    if c in ['mod','div','pow']:
        c = [['mod','%'],['div','//'],['pow','**']][['mod','div','pow'].index(c)][1]
    print(eval(a.format(c)))


# Solve 2 (my)
a, b, c = (input() for _ in '123')
if c in ['/','mod','div'] and float(b)==0.0: 
    print('Деление на 0!')
else:
    print(eval(str('('+a+')'+'{0}'+'('+b+')').format([['mod','%'],['div','//'],['pow','**']][['mod','div','pow'].index(c)][1] if c in ['mod','div','pow'] else c)))

# Solve 3 (from comments)
operations = {
      "+": lambda x, y: x + y,
      "-": lambda x, y: x - y,
      "/": lambda x, y: x / y,
      "*": lambda x, y: x * y,
      "mod": lambda x, y: x % y,
      "pow": lambda x, y: x ** y,
      "div": lambda x, y: x // y
}

x, y = float(input()), float(input())
operation = input()

if operation in ["mod", "div", "/"] and y == 0:
    print("Деление на 0!")
else:
    print(operations[operation](x, y))

# Solve 4 (from comments)
first = float(input())
second = float(input())
action = input()
operations = {"mod": "%", "div": "//", "pow": "**"}
try:
    print(eval("(" + str(first) + ")" + operations.get(action, action) + str(second)))
except ZeroDivisionError:
    print('Деление на 0!')
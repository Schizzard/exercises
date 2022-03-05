# Step 5

A = int(input())
B = int(input())
H = int(input())

if H < A:
    print('Недосып')
elif H > B:
    print('Пересып')
else:
    print('Это нормально')

# Comments
f = lambda a, b, h: "Недосып" if h < a else "Пересып" if h > b else "Это нормально"
print(f(int(input()), int(input()), int(input())))
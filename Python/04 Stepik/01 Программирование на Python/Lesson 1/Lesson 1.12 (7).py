# Step 7

# Solve 1 (my)
a=int(input())
print('Счастливый') if sum(int(b) for b in str(a//1000)) == sum(int(b) for b in str(a%1000)) else print('Обычный')

# Solve 2 (from comments)
a, b, c, d, e, f = input()
n= int(a)+int (b)+int(c)
m= int(d)+int (e)+int(f)
if n==m:
    print ('Счастливый')
else:
    print ('Обычный')


# Solve 3 (from comments)
n = list(map(int, list(input())))
print('Счастливый' if sum(n[:3]) == sum(n[3:]) else 'Обычный')


# Solve 4 (from comments)
a,b,c,d,e,f=(int(n) for n in input())
print(('Обычный','Счастливый')[a+b+c == d+e+f])
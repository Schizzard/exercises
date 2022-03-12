# Step 8


# Solve 1 (my)
a = int(input())
b=[]
for i in range(a+1):
    for ii in range(i):
        b.append(i)
    if len(b) > a: 
        break
print(*b[:int(a)])



# Solve 2 (from comments)
print(*[int( 1/2 + (2 * n)**0.5 ) for n in range(1, int(input())+ 1)])


# Solve 3 (from comments)
n=int(input())
print(*[i for i in range(1,n+1) for j in range(i)][:n])
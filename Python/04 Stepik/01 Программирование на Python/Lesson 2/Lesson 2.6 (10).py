# Step 10

# Solve 1 (my)
# b = [['1', '2', '3'], 
#      ['4', '5', '6'], 
#      ['7', '8', '9']]

b=[]
while True:
    a = input()
    if a == 'end': break
    b.append([int(i) for i in a.split()])

ans = [[0 for i in range(len(b[0]))] for ii in range(len(b))]
cc = [[0,-1],[0,1],[-1,0],[1,0]]
for i in range(len(b)):
    for j in range(len(b[i])):
        current=b[i][j]
        sum_1 = 0
        for ccc in range(len(cc)):
            di, dj = cc[ccc]
            try_di = (i+di)%len(b)
            try_dj = (j+dj)%len(b[i])
            sum_1+=b[try_di][try_dj]
        ans[i][j]=sum_1
for ii in ans:
    print(*ii)


# Solve 2 (from comments)
a = [[int(i) for i in input().split()]]
b = input()
while b != 'end' :
    a.append([int(i) for i in b.split()])
    b = input()
for i in range(len(a)): 
    for j in range(len(a[i])): 
        print((a[i-1][j] + a[(i+1) % len(a)][j] + a[i][j-1] + a[i][(j+1) % len(a[i])]), end=' ')
    print()
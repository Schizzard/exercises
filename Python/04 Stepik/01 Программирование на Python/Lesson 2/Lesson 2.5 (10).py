# Step 10


# Solve 1 (my)
a = [int(a) for a in input().split()]
if len(a)>1:
    for i in range(len(a)-1):
        print(a[i-1]+a[i+1], end=' ')
    print(a[0]+a[-2], end=' ')
else:
    print(*a)


# Solve 2 (from comments)
arr = list(map(int, input().split()))
print(*arr if len(arr) == 1 else [arr[i - 1] + arr[(i + 1) % len(arr)] for i in range(len(arr))])
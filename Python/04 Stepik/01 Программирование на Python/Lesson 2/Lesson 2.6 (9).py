# Step 9


# Solve 1 (my)
a = [int(a) for a in input().split()]
b = int(input())
if b in a:
    for i in range(len(a)):
        print(i, end=' ') if a[i] == b else ''
else:
    print('Отсутствует')

# Solve 2 (from comments)
l, n = [int(i) for i in input().split()], int(input())
print(*[x for x in range(len(l)) if l[x]==n] if n in l else ["Отсутствует"])

# Solve 2 (from comments)
L, n = input().split(), input()
print(*([i for i, c in enumerate(L) if n == c] or ['Отсутствует']))
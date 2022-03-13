# Step 7

# Solve 1 (my)
s=int(input())
a = [int(input()) for i in range(s)]
b={i:0 for i in a}
for n in b.keys():
    b[n] = f(n)
for m in a:
    print(b[m])


# Solve 2 (from comments)
a=[int(input()) for i in range(int(input()))]
b={x:f(x) for x in set(a)}
for i in a:
    print(b[i])
# Step 10


# Solve 1 (my)
a = [int(a) for a in input().split()]
print(*{i for i in a if a.count(i)>1})


# Solve 2 (my)
a = [int(a) for a in input().split()]
b=[]
for i in a:
    if a.count(i)>1 and i not in b:
        b.append(i)
print(*b)

# Solve 3 (from comments)
[[print(i, end=' ') for i in set(x) if x.count(i) > 1] for x in [input().split()]]

# Solve 4 (from comments)
a=input().split()
[a.remove(i) for i in set(a)]
print(*set(a))
        

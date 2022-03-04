# Step 5

# Solve 1 (my)
a=[]
for _ in range(3):
    a.append(int(input()))
print(a.pop(a.index(max(a))))
print(a.pop(a.index(min(a))))
print(a.pop(a.index(max(a))))


# Solve 2 (from comments)
print("{2}\n{0}\n{1}".format(*sorted([int(input()) for i in range(3)])))
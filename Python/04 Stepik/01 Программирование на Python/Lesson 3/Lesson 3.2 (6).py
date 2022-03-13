# Step 6

# Solve 1 (my)
s=input()
ans = {w:0 for w in s.lower().split()}
for i in ans:
    ans[i] = s.lower().split().count(i)
for itt in ans.items():
    print(*itt)


# Solve 2 (from comments)
s = input().lower().split()
for i in set(s):
    print(i, s.count(i))
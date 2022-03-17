# Step 3
'''
4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic

---
stepic
champignons
the
'''

# Solve 1 (my)
d = [input().lower() for i in range(int(input()))]
s = [input().lower().split() for i in range(int(input()))]
a = set()
for l in s:
    for w in l:
        if w not in d: a.add(w)
for aa in a:
    print(aa)

# Solve 2 (my)
dct = [input().lower() for i in range(int(input()))]
txt = [input().lower().split() for i in range(int(input()))]
ans = {wrd for ln in txt for wrd in ln if wrd not in dct}
print(*ans, sep='\n')


# Solve 3 (from comments)
dic = {input().lower() for i in range(int(input()))}
wrd = set()
for w in range(int(input())):
    wrd |= {i.lower() for i in input().split()}
print(*wrd.difference(dic), sep="\n")
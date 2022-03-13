# Step 2

# Solve 1 (my)
with open('dataset_3363_2 (3).txt', 'r', encoding='UTF-8') as textfile:
    s=textfile.readline().strip()+' '

ans=''
d=''
for i in range(len(s)-1):
    if s[i].isalpha():
        c=s[i]
    else:
        d+=s[i]
        if not s[i+1].isdigit():
            ans += c*int(d)
            d=''

with open('ans_for_dataset_3363_2 (3).txt', 'w', encoding='UTF-8') as textfile:
    textfile.write(ans)

# Solve 2 (from comments)
with open('dataset_3363_2 (3).txt', 'r') as f:
    s = f.readline().strip()
i = 0
while i < len(s):
    j = i + 1
    while j < len(s) and s[j].isdigit():
        j += 1
    print(s[i] * int(s[i+1:j]), end='')
    i = j

# Solve 3 (from comments)
s, d = input(), []
for i in s:
    if not i.isdigit(): d.append(i)
    else: d[-1] += i
print(*[i[0]*int(i[1:]) for i in d], sep='')
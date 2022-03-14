# Step 3

# Solve 1 (my)
with open('dataset_3363_3.txt', 'r', encoding='UTF-8') as textfile:
    s=''
    for line in textfile.readlines():
        s+=line.strip()+' '

d={}
for i in s.lower().split():
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
vv=0
for k, v in d.items():
    if v>vv: 
        kk = k
        vv=v
print(kk, vv)


# Solve 2 (from comments)
with open('dataset_3363_3.txt') as f:
    text = f.read().lower().split()
popular_word = max(set(text), key=text.count)
print(popular_word, text.count(popular_word))
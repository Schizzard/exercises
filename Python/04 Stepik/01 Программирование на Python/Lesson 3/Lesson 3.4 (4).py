# Step 4

# Solve 1 (my)
with open('dataset_3363_4.txt', 'r', encoding='UTF-8') as textfile:
    d={}
    for line in textfile.readlines():
       name, math, phys, lang = line.strip().split(';')
       d[name]=[int(math), int(phys), int(lang)] 

m, p, l = 0, 0, 0
for st, sc in d.items():
    print(sum(sc)/len(sc))
    m,p,c = m+sc[0], p+sc[1], l+sc[2]
print(m/len(d), p/len(d), l/len(d))


# Solve 2 (from comments)
koll, a1, b1, c1 = 0, 0, 0, 0
with open('dataset_3363_4.txt', 'r') as inf:
    for line in inf:
        line = line.strip().split(';')
        a, b, c = int(line[1]), int(line[2]), int(line[3])
        print((a+b+c)/3)
        koll += 1
        a1 += a
        b1 += b
        c1 += c
print((a1/koll), (b1/koll), (c1/koll))


# Solve 3 (from comments)
st = [x.split(';') for x in open('dataset_3363_4.txt').readlines()]
print(*[sum([int(y) for y in x[1:]])/3 for x in st], sep='\n')
print(*[sum([int(y) for y in [st[x][z] for x in range(len(st))]])/len(st) for z in range(1,4)])
# Step 1
'''
3
Спартак;9;Зенит;10
Локомотив;12;Зенит;3
Спартак;8;Локомотив;15
'''

# Solve 1 (my)
s = int(input())
d = [input() for i in range(s)]
t = [i.split(';') for i in d]
com_set = set()
for i in range(len(t)):
    com_set.add(t[i][0])
    com_set.add(t[i][2])
itogi = {com:[0,0,0,0,0] for com in com_set}

for i in range(len(t)):
    com1, com2 = t[i][0], t[i][2]
    num1, num2 = int(t[i][1]), int(t[i][3])
    
    itogi[com1][0]+=1
    itogi[com2][0]+=1
    
    if num1>num2:
        itogi[com1][1]+=1
        itogi[com2][3]+=1
        itogi[com1][4]+=3
    
    elif num1<num2:
        itogi[com2][1]+=1
        itogi[com1][3]+=1
        itogi[com2][4]+=3
    
    elif num1==num2:
        itogi[com1][2]+=1
        itogi[com2][2]+=1
        itogi[com1][4]+=1
        itogi[com2][4]+=1

for k,v in itogi.items():
    print(k, end=':')
    print(*v)



# Solve 2 (from comments)
def command(c, res):
    if not c in dct: dct[c] = [0, 0, 0, 0, 0]
    dct[c] = [dct[c][0] + 1, 
                dct[c][1] + 1 if res == 3 else dct[c][1],
                dct[c][2] + 1 if res == 1 else dct[c][2],
                dct[c][3] + 1 if res == 0 else dct[c][3],
                dct[c][4] + res,]  
dct = {}
for i in range(int(input())):
    c1, g1, c2, g2 = input().split(';')    
    command(c1, 3 if g1 > g2 else 1 if g1 == g2 else 0)
    command(c2, 3 if g2 > g1 else 1 if g1 == g2 else 0)
for c in dct:
    print('{}:{} {} {} {} {}'.format(c, *dct[c]))



# Solve 3 (from comments)
a=[input().split(';') for i in range(int(input()))]
b={i:[] for i in set([i[0] for i in a])|set([i[2] for i in a])}
for i in a:
	b[i[0]].append(1 if i[1]==i[3] else 3 if i[1]>i[3] else 0)
	b[i[2]].append(1 if i[1]==i[3] else 3 if i[1]<i[3] else 0)
for i in b: print('%s:%i %i %i %i %i'%(i,len(b[i]),b[i].count(3),b[i].count(1),b[i].count(0),sum(b[i])))
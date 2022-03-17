# Step 4
'''4
север 10
запад 20
юг 30
восток 40'''

# Solve 1 (my)
dct={'север':[0,1],
     'юг':[0,-1],
     'запад':[-1,0],
     'восток':[1,0],
    }

d = [input().split() for i in range(int(input()))]
ans = [0,0]
ch = []
for com in d:
    ch[:] = dct[com[0]]
    for i in range(len(ch)):
        ch[i]=int(ch[i])*int(com[1])
    ans = [*map(lambda x, y: x + y, ans, ch)]
print(*ans)



# Solve 2 (from comments)
n=int(input())
d={'север':0,'запад':0,'юг':0,'восток':0}
for i in range(n):
    x=input().split()
    d[x[0]]+=int(x[1])
print(d['восток']-d['запад'], d['север']-d['юг'])
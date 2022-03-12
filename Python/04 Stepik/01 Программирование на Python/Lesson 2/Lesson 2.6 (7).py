# Step 7


# Solve 1 (my)
sum1, sum2 = 0, 0
while True:
    a=int(input())
    sum1+=a
    sum2+=a**2
    if sum1==0:
        print(sum2)
        break


# Solve 2 (from comments)
s=[int(input())]
while sum(s)!=0: s.append(int(input()))
print(sum([i**2 for i in s]))
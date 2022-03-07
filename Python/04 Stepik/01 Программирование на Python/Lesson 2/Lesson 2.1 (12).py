# Step 12

# Solve 1 (my)
a,b,c,ans = int(input()), int(input()), 1, 0
while c!=0:
    c, ans = (ans+1)%a + (ans+1)%b, ans + 1
print(ans)

# Solve 2 (from comments)
import math
A=int(input()) #999983 999979 =)
B=int(input())
print (A*B//math.gcd(A,B))


# Solve 3 (from comments)
a, b, i = int(input()), int(input()), 1
while not (i % a == 0 and i % b == 0):
    i += 1
print(i)

# Solve 3+ (from comments)
a, b, i = int(input()), int(input()), 1
while i%a or i%b:
    i += 1
print(i)
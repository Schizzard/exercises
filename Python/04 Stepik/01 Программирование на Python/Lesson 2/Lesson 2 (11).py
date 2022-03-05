# Step 11

# Solve 1 (my)

ans=0
a=1
while a !=0:
    a=int(input())
    ans+=a
print(ans)


# Solve 2 (from comments)   
import sys
print(sum(int(x) for x in sys.stdin.readlines()))
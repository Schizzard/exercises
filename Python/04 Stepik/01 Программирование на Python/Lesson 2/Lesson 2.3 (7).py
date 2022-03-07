# Step 7

# Solve 1 (my)
a, b = (int(input()) for i in range(2))
c,d = 0, 0
for i in range(a,b+1):
   if i%3==0:
      c+=i
      d+=1
print(c/d)
      

# Solve 2 (from comments)
a,b = int(input()), int(input())
a += -a%3
b -= b%3
print((a+b)/2)


# Solve 3 (from comments)
x = [x for x in range(int(input()),int(input()) + 1) if x % 3 == 0]
print(sum(x)/len(x))    

# Solve 4 (from comments)
print((((int(input())-1)//3)+1+int(input())//3)*1.5)
# Step 1

# Solve 1 (my)
a = int(input())
ans = [[0 for i in range(a)] for ii in range(a)]
i,j = 0, 0
c=1
d=0
while c<=a**2:
    if d == 0:
        while j<a and ans[i][j]==0:
            ans[i][j]=c
            if j<a-1 and ans[i][j+1]==0: 
                j+=1
            c+=1
        else:
            d+=1
            i+=1
            
    elif d==1:
        while i<a and ans[i][j]==0:
            ans[i][j]=c
            if i<a-1 and ans[i+1][j]==0: 
                i+=1
            c+=1
        else:
            d+=1
            j-=1
    
    elif d==2:
        while i<a and ans[i][j]==0:
            ans[i][j]=c
            if j>0 and ans[i][j-1]==0: 
                j-=1
            c+=1
        else:
            d+=1
            i-=1
    
    elif d==3:
        while i<a and ans[i][j]==0:
            ans[i][j]=c
            if i>0 and ans[i-1][j]==0: 
                i-=1
            c+=1
        else:
            d=0
            j+=1
for ii in ans:
    print(*ii)


# Solve 2 (from comments)
n=int(input())
t=[[0]*n for i in range (n)]
i,j=0,0
for k in range(1, n*n+1):
  t[i][j]=k
  if k==n*n: break
  if i<=j+1 and i+j<n-1: j+=1
  elif i<j and i+j>=n-1: i+=1
  elif i>=j and i+j>n-1: j-=1
  elif i>j+1 and i+j<=n-1: i-=1
for i in range(n):
  print(*t[i])
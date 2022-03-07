# Step 4

# Solve 1 (my)
g = input()+' '
ii=1
ans=''
for i in range(len(g)-1):
    if g[i] == g[i+1]:
        ii+=1
    else:
        ans+=g[i]+str(ii)
        ii=1
print(ans)



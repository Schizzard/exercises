# Step 3

# Solve 1 (my)
a, b, c, d = (int(input()) for i in range(4))
for i in range(c,d+1):
   print('\t', i, sep='', end='')

for i in range(a,b+1):
   print()
   print(i, '\t', end='')
   for ii in range(c,d+1):
      print(i*ii, '\t', sep='', end='')


# Solve 2 (from comments)
a, b, c, d = (int(input()) for i in range(4))
print('\t', *range(c, d+1), sep='\t')
for i in range(a,b+1):
    print(i, *range(i*c,(i*d)+1, i), sep='\t')


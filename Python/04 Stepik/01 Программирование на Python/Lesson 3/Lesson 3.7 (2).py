# Step 2
'''
abcd
*d%#
abacabadaba
#*%*d*%
'''

# Solve 1 (my)
d = [input() for i in range(4)]

table1 = str.maketrans(d[0],d[1])
table2 = str.maketrans(d[1],d[0])
s1 = d[2].translate(table1)
s2 = d[3].translate(table2)
print(s1)
print(s2)



# Solve 2 (my)
d = [input() for i in range(4)]
print(d[2].translate(str.maketrans(d[0],d[1])), d[3].translate(str.maketrans(d[1],d[0])),sep='\n')



# Solve 3 (from comments)
source, dest = input(), input()
decoded = input()
encoded = input()

print(decoded.translate(str.maketrans(source, dest)))
print(encoded.translate(str.maketrans(dest, source)))
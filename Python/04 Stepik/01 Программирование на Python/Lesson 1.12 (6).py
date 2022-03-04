# Step 6

# Solve 1 (my)
a=int(input())

if int(str(a)[-2:]) in range(11,21) or int(str(a)[-1]) in [0, 5, 6, 7, 8, 9] :
    print(a, 'программистов')
elif int(str(a)[-1]) in [2,3,4]:
    print(a, 'программиста')
else:
    print(a, 'программист')

# Solve 2 (from comments)
num = str(input())
ov = ('0', '11', '12', '13', '14', '5', '6', '7', '8', '9')
ta = ('2', '3', '4')
if num.endswith(ov):
    print(num + " программистов")
elif num.endswith('1'):
    print(num + " программист")
elif num.endswith(ta):
    print(num + " программиста")


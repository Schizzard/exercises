# Step 1

a, b, c = (input() for _ in '123')
p=(a+b+c)/2
print(float((p*(p-a)*(p-b)*(p-c))**0.5))
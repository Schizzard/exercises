# Step 4

# Solve 1 (my)
formulas = {
    'треугольник': lambda a, b, c : ((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**0.5,
    'прямоугольник': lambda a, b : a*b,
    'круг': lambda r : 3.14*r**2
}

oper_count = {
    'треугольник': 3,
    'прямоугольник': 2,
    'круг': 1
}

type_1 = input()
a=[]
for _ in range(oper_count.get(type_1)):
    a.append(float(input()))
print(formulas[type_1](*a))


# Solve 2 (from comments)
figura = {'треугольник': [3, lambda a, b, c: ((a+b+c)/2*((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c))**0.5], 
          'прямоугольник': [2, lambda a, b: a*b], 
          'круг': [1, lambda r: 3.14*r**2]}
f = input()
print(figura[f][1](*(float(input()) for _ in range(figura[f][0]))))

# Step 8

# Solve 1 (my)
def f(x):
    if x<=-2:   return 1-(x+2)**2
    if -2<x<=2: return -x/2
    if 2<x:     return (x-2)**2+1


# Solve 2 (from comments)
def f(x): return (lambda x :1 - (x + 2) ** 2 if x <= -2 else -x / 2 if x < -2 or x <= 2 else (x - 2) ** 2 + 1)(x)
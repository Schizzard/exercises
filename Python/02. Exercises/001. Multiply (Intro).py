# 001. Multiply (Intro)

# Bad idea for multiply

def mult_two(n,m):
    p=0
    for _ in range(m):
        for _ in range(n):
            p = -~p
    return p

print(mult_two(10,200))
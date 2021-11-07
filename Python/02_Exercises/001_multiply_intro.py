# 001. Multiply (Intro)

# So this mission is the easiest one. Write a function that will receive 2 
# numbers as input and it should return the multiplication of these 2 numbers.

# Input: Two arguments. Both are of type int
# Output: Int.

# Example:
# mult_two(2, 3) == 6
# mult_two(1, 0) == 0


# Find realy bad idea for multiply

def mult_two(n,m):
    p=0
    for _ in range(m):
        for _ in range(n):
            p = -~p
    return p

print(mult_two(10,200))
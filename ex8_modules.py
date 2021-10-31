# Learning modules using math as an example

import math

print(math.pi)
print(math.cos(math.pi))


import time, random

i = 0
n=0
while i != 100 :
    i = random.randint(1, 100) 
    print(i)
    time.sleep(1)
    n += 1
print("попыток: ", n)
import math

def is_int(x):
    r = x % 1
    if math.isclose(0, r):
        return True
    else:
        return False
    
print(is_int(3))

total = 0.100 + 0.200 + 0.299 + 0.401
print(total)

def is_prob(p1, p2, p3):
    if math.isclose(p1 + p2 + p3, 1):
        return True
    return False
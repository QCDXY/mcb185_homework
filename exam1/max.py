def max3(a,b,c):
    largest = a
    if b > largest:
        largest = b
    if c > largest:
        largest = c
    return largest

print(max3(1,2,3))
print(max3(7,2,3))
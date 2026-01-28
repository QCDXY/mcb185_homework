def triangular(n):
    if n < 0: return 'not a valid input'
    total = 0
    for i in range(1,n+1):
        total += i
    return total

print(triangular(3))
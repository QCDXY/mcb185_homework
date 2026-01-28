def factorial(n):
    if n == 0: return 1
    if n == 1: return 1
    if n < 0: return 'not a valid number'
    fac = 1
    while(True):
        fac *= n
        n -= 1
        if(n==0):
            break
    return fac

print(factorial(5))

def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    for i in range(2, n):
        print(f'i:{i}')
        if n % i == 0: 
            return False
        i += 1
    print(f'n:{n}')
    return True 

print(is_prime(11))
def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    for i in range(2, n):
        if n % i == 0: 
            return False
        i += 1
    return True 

output = ""
for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        output = "FizzBuzz"
    elif i % 3 == 0:
        output = "Fizz"
    elif i % 5 == 0:
        output = "Buzz"
    else:
        output = str(i)
    
    if is_prime(i) == True:
        output += "*"
    print(output)
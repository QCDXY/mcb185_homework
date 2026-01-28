import math

n=0
euler_est = 0 
while True:
    previous =  euler_est
    euler_est += 1 / math.factorial(n)
    print(euler_est)
    if previous == euler_est:
        break
    n += 1

        
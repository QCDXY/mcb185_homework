import math

pi_est = 3
n = 2
sign = 1
term = 0
while True:
    term = 4/(n*(n+1)*(n+2))
    pi_est += sign * term
    print(pi_est)
    
    next_term = -1 * sign * (4/((n+2)*(n+3)*(n+4)))
    if sign == 1:
        upper_bound = pi_est
        lower_bound = pi_est + next_term
    else:
        upper_bound = pi_est + next_term
        lower_bound = pi_est
    
    if upper_bound - math.pi <= 1e-6 and math.pi - lower_bound <= 1e-6:
        break

    n += 2
    sign *= -1

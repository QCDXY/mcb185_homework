import random

trials = 0
success = 0

while True:
    x = random.random()
    y = random.random()
    trials += 1
    if x*x + y*y <= 1:
        success += 1
    pi_est = 4 * (success/trials)
    print(f'The estimation of pi is:{pi_est}')

 
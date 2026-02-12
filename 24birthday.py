import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

success = 0

for i in range(0,trials):
    calendar = [0] * days
    for j in range(0,people):
       birthday = random.randint(0,days-1)
       calendar[birthday] += 1
    for day, value in enumerate(calendar):
        if calendar[day] >= 2: 
            success += 1
            break

prob = success / trials
prob *= 100
print(f"The probobility of {people} persons in a class room with same brithday is: {prob}%")


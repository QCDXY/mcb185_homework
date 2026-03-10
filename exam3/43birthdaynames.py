import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

success = 0

for i in range(0,trials):
    birthday = []
    for j in range(0,people):
        birthday.append(random.randint(1,days))
    if len(birthday) != len(set(birthday)): success += 1


prob = success / trials
prob *= 100
print(f"The probobility of {people} persons in a class room with same brithday is: {prob}%")
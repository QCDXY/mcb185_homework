import random

result = random.randint(1,20)

if result >= 5: print("Success at DC 5")
if result >= 10: print("Success at DC 10")
if result >= 15: print("Success at DC 15")
if result < 5: print("Failed")
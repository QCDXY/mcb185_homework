import sys

filename = sys.argv[1]

with open(filename, 'r') as f:
    text = f.read()

result = []
sign = 1 

for char in text:
    if sign == 1:
        result.append(char.upper())
    else:
        result.append(char.lower())
    sign *= -1

print(''.join(result))
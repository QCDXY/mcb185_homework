import math
import sys

def mean(values):
    return sum(values) / len(values)
    
def median(values):
    values = sorted(values)
    n = len(values)
    mediannumber = n // 2
    if n % 2 == 0: return values[mediannumber]
    else: return (values[mediannumber-1] + values[mediannumber]) / 2

def stddev(values):
    meanvalue = mean(values)
    variance = sum((x - meanvalue) ** 2 for x in values) / (len(values) - 1)
    return math.sqrt(variance)

def maxmin(values):
    largest = values[0]
    smallest = values[0]
    for i in range(len(values)):
        if values[i] > largest: largest = values[i]
        if values[i] < smallest: smallest = values[i]
    return largest, smallest

input = []
for arg in sys.argv[1:]:
    input.append(float(arg))

print(f"Count:{len(input)}")
print(f"Max value and Min Value:{maxmin(input)}")
print(f"Mean: {mean(input)}")
print(f"Standard Deviation: {stddev(input)}")
print(f"Median: {median(input)}")
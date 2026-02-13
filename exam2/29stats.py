def stats(x):
    meanvalue = sum(x)/len(x)

    total = 0
    for num in x:
        total += (num - meanvalue) ** 2
    stddev = (total / (len(x) - 1)) ** 0.5

    sorted_x = sorted(x)
    n = len(sorted_x)
    mediannumber = n // 2
    if n % 2 != 0: median = sorted_x[mediannumber]
    else: median = (sorted_x[mediannumber-1] + sorted_x[mediannumber]) / 2

    return meanvalue, stddev, median

test = [4,2,3,5,6]

print(stats(test))
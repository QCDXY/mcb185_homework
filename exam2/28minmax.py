def minmax(x):
    smallest = x[0]
    largest = x[0]

    for i, num in enumerate(x):
        if x[i] < smallest:
            smallest = num
        if x[i] > largest:
            largest = num

    return smallest, largest

test = [1, 3, 78, -1]

print(minmax(test))
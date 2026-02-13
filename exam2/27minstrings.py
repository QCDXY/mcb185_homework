def minstr(strings):
    smallest = strings[0]

    for i, s in enumerate(strings):
        if len(s) < len(smallest):
            smallest = s

    return smallest

test = ['1232', 'sfafasfasfsafa', '78', 'ATCGTCG']

print(minstr(test))
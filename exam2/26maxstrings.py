def maxstr(strings):
    longest = strings[0]

    for i, s in enumerate(strings):
        if len(s) > len(longest):
            longest = s

    return longest

test = ['1232', 'sfafasfasfsafa', '78', 'ATCGTCG']

print(maxstr(test))

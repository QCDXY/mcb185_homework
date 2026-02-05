for a in range(1, 100):
    for b in range(a, 100):
        c2 = a*a + b*b
        c = int(c2 ** 0.5)
        if c*c == c2:
            print(a, b, c)

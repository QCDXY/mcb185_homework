def oligotm(a, b, c, d):
    if a+b+c+d <= 13:
        return (a+b)*2 + (c+d)*4
    return 64.9 + (41*(c+d-16.4)/(a+b+c+d))

print(oligotm(1,1,1,1))
print(oligotm(10,6,7,4))
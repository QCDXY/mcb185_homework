import sys

def oligo_tm(s):
    a = s.count('A')
    t = s.count('T')
    c = s.count('C')
    g = s.count('G')
    if len(s) <= 13: return (a+t)*2 + (g+c)*4
    return 64.9 + 41 * (g+c -16.4) / (a+t+g+c)

print(oligo_tm(sys.argv[1]))
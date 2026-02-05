import math
def phred_to_prob(c):
    Q = ord(c) - 33
    return 10 ** (-Q/10)

def prob_to_phred(p):
    Q = -10 * math.log10(p)
    return chr(round(Q)+33)

print(prob_to_phred(0.001))
print(phred_to_prob('A'))
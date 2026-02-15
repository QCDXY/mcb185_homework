import random

def mutation(dna, p):
    if not (0.0 <= p <= 1.0):
        raise ValueError('Not valid probability')
    mutated = []
    nts = ['A','T','C','G']

    for each in dna:
        if each not in nts:
            raise ValueError('Not valid nucleotides')
        if random.random() < p:
            possible_mutation = nts.copy()
            possible_mutation.remove(each)
            mutated.append(random.choice(possible_mutation))
        else:
            mutated.append(each)

    return ''.join(mutated)

print(mutation('ACGTACGTACGT',0.3))
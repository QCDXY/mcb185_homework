import random

def random_dna(n, X=[0.25, 0.25, 0.25, 0.25]):
    if n<0:
        raise ValueError('n could not be negative.')
    if len(X) != 4:
        raise ValueError('Invalid weight list.')
    nts = ['A','T','C','G']
    return ''.join(random.choices(nts,X,k=n))
 


print(random_dna(10,))
print(random_dna(10,[1.0,0,0,0]))
print(random_dna(10,[0,1.0,0,0]))
print(random_dna(10,[0.1,0.5,0.3,0.1,0.1]))
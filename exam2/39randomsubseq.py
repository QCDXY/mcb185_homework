import random

def random_subseq(seq,n,k):
    if k > len(seq):
        raise ValueError('Length of subsequence should not be higher than length of sequence')
    max_range = len(seq) - k
    result = []
    for i in range(0,n):
        start_pos = random.randint(0,max_range)
        result.append(seq[start_pos:start_pos+k])
    return result

print(random_subseq('ATCGGCTA',40,4))
print(random_subseq('ATCGGCTA',3,5))
print(random_subseq('ATCGGCTA',4,8))
print(random_subseq('ATCGGCTA',4,8))

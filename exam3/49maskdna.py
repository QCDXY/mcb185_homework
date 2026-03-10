import sys
import gzip
import math

filename = sys.argv[1]
window = int(sys.argv[2])
threshold = float(sys.argv[3])

def read_fasta(file):
    name = None
    seqs = ""

    if file.endswith('gz'): f = gzip.open(file, 'rt')
    else: f = open(file)

    for line in f:
        line = line.strip()

        if line.startswith('>'):
            if len(seqs) > 0:
                yield(name,seqs)
                name = line[1:]
                seqs = ""
            else:
                name = line[1:]
        else:
            seqs += line
    
    yield name, seqs
    f.close()

def entropy(seq):
    a = seq.count('A')
    c = seq.count('C')
    g = seq.count('G')
    t = seq.count('T')

    h = 0.0
    n = len(seq)

    for count in (a, c, g, t):
        if count == 0:
            continue
        p = count / n
        h -= p * math.log2(p)

    return h

def mask_sequence(seq, window, threshold):
    masked = list(seq)
    n = len(seq)
    masking = [False] * n

    for i in range(n - window + 1):
        window_seq = seq[i:window+i]
        if entropy(window_seq) < threshold:
            for j in range(i,window+i):
                masking[j] = True

    for i in range(n):
        if masking[i]:
            masked[i] = 'N'
    
    return ''.join(masked)

for name,seq in read_fasta(filename):
    print(f'{name}:')
    print(mask_sequence(seq,window,threshold))
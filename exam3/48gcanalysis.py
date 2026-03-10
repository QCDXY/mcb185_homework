import sys
import gzip

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

def gc_comp(seq):
    gc = 0
    for base in seq:
        if base == "G" or base == "C":
            gc += 1
    return gc / len(seq)

def gc_skew(seq):
    g = 0
    c = 0

    for base in seq:
        if base == "G":
            g += 1
        elif base == "C":
            c += 1

    if g + c == 0:
        return 0.0

    return (g - c) / (g + c)

def analyze_sequence(name, seq, window):
    for i in range(0, len(seq)):
        slice = seq[i:i + window]
        if len(slice) == 0:
            continue

        comp = gc_comp(slice)
        skew = gc_skew(slice)

        print(name, i+1, i + len(slice), f"{comp:.4f}", f"{skew:.4f}")

fasta = sys.argv[1]
window = int(sys.argv[2])

for name, seq in read_fasta(fasta):
    analyze_sequence(name,seq,window)
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

def analyze_sequence(name, seq, window):
    first_window = seq[0:window]
    g = first_window.count('G')
    c = first_window.count('C')
    gc_comp = (g+c) / window
    if g + c == 0: 
        gc_skew = 0
    else: 
        gc_skew = (g - c) / (g + c)
    print(name, 1, window, f"{gc_comp:.4f}", f"{gc_skew:.4f}")

    for i in range(1,len(seq)-window+1):
        if seq[i-1] == 'C': c -= 1
        if seq[i-1] == 'G': g -= 1
        if seq[i+window-1] == 'C': c += 1
        if seq[i+window-1] == 'G': g += 1
        gc_comp = (g+c) / window
        if g + c == 0: 
            gc_skew = 0
        else: 
            gc_skew = (g - c) / (g + c)

        print(name, i+1, i + window, f"{gc_comp:.4f}", f"{gc_skew:.4f}")


fasta = sys.argv[1]
window = int(sys.argv[2])

for name, seq in read_fasta(fasta):
    analyze_sequence(name,seq,window)

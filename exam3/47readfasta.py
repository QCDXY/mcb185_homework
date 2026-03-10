import sys
import gzip

filename = sys.argv[1]


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


for name, seq in read_fasta(filename):
    print(name, len(seq))


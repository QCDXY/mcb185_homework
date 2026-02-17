import itertools

codons = [''.join(t) for t in itertools.product('ACGT', repeat=3)]
trans = 'KNKNTTTTRSRSIIMIQHQHPPPPRRRRLLLLEDEDAAAAGGGGVVVV*Y*YSSSS*CWCLFLF'

def translate(seq):
    seq_codons = []
    result = ''
    translate_index = dict(zip(codons,trans))
    for i in range(0, len(seq), 3):
        seq_codons.append(seq[i:i+3])
    for index, value in enumerate(seq_codons):
        try:    
            result += translate_index[value]
        except KeyError:
            result += 'X'
    return result

def translate1(seq):
    codon = ''
    result = []

    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if len(codon) != 3:
            result.append('X')
            continue
        if any(nt not in 'ACGT' for nt in codon):
            result.append('X')
            continue
        index = codons.index(codon)
        result.append(trans[index])

    return ''.join(result)

print(translate('AAATTTCCCGGG'))
print(translate('AAATTTCCCGGGG'))
print(translate('AAANTTTCCCGGG'))
print(translate('AAANNNTTTCCCGGG'))

print(translate1('AAATTTCCCGGG'))
print(translate1('AAATTTCCCGGGG'))
print(translate1('AAANTTTCCCGGG'))
print(translate1('AAANNNTTTCCCGGG'))





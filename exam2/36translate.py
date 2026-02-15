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

print(translate('AAATTTCCCGGG'))
print(translate('AAATTTCCCGGGG'))
print(translate('AAANTTTCCCGGG'))
print(translate('AAANNNTTTCCCGGG'))





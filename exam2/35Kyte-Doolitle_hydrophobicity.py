aas = 'ACDEFGHIKLMNPQRSTVWY'
kdh = (1.8, 2.5, -3.5, -3.5, 2.8, -0.4, -3.2, 4.5, -3.9, 3.8, 1.9, -3.5, -1.6,
	-3.5, -4.5, -0.8, -0.7, 4.2, -0.9, -1.3)

def hydropathy(seq):
    kdh_index = dict(zip(aas,kdh))
    result = 0
    try:
        for index, value in enumerate(seq):
            result += kdh_index[seq[index]]
    except KeyError:
        return 'Input include invalid amino acid'
    return result

def hydropathy1(seq):
    result = 0
    for ami in seq:
        try:
            index = aas.index(ami)
            result += kdh[index]
        except ValueError:
            return 'Input include invalid amino acid'
    return result

print(hydropathy('MKTIIALSYWACD'))
print(hydropathy('MKTIIALSYWACDX'))
print(hydropathy1('MKTIIALSYWACD'))
print(hydropathy1('MKTIIALSYWACDX'))
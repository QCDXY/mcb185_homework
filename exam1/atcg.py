def complement(nt):
    if nt == 'A': return 'T'
    if nt == 'T': return 'A'
    if nt == 'C': return 'G'
    if nt == 'G': return 'C'
    return 'not a valid input'

print(complement('A'))
print(complement('T'))
print(complement('C'))
print(complement('G'))
print(complement('N'))
print(complement(1))

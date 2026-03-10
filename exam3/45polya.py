def polya(dna):
    longest = 0
    current = 0

    for base in dna:
        if base == 'A':
            current += 1
            if current > longest:
                longest = current
        else:
            current = 0

    return longest
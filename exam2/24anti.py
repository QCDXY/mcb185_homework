def anti(nt):
    anti_seq = ""
    for i in range(0,len(nt)):
        if nt[i] == 'A': anti_seq += 'T'
        if nt[i] == 'T': anti_seq += 'A'
        if nt[i] == 'C': anti_seq += 'G'
        if nt[i] == 'G': anti_seq += 'C'
    return anti_seq

print(anti("ATCG"))
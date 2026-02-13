def gc_comp(s):
    sum_gc = s.count('G')+ s.count('C')
    comp = sum_gc/len(s)
    return comp

sequence = input("Enter sequence here:")

print(f"GC composition for this sequence is {gc_comp(sequence)*100}%")
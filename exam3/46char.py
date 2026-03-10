import sys

filename = sys.argv[1]

counts = {}

with open(filename) as f:
    for line in f:
        for ch in line:
            if ch not in counts:
                counts[ch] = 0
            counts[ch] += 1

for ch in sorted(counts):
    if ch.isprintable():
        label = ch
    else:
        label = f"ASCII_{ord(ch)}"

    print(label, counts[ch])

print(counts)
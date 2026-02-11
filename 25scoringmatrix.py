import sys

string1 = sys.argv[1]
match = int(sys.argv[2])
mismatch = int(sys.argv[3])

print("  ", end="")
for c in string1:
    print(f"{c:>3}", end="")
print("\n")

for row in string1:
    print(row, end=" ")
    for col in string1:
        if row == col:
            print(f"{match:>3}", end="")
        else:
            print(f"{mismatch:>3}", end="")
    print("\n")

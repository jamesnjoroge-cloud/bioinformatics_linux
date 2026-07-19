from collections import Counter

with open("rosalind_ini.txt", "r") as f:
    sequence = f.read().strip()

counts = Counter(sequence)
results = f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"
print(results)

with open("output.txt", "w") as f:
    f.write(results)
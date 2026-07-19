from collections import Counter

with open("rosalind_dna.txt", "r") as f:
    dna = f.read().strip()

counts = Counter(dna)
result = f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}"
print(result)

with open("output.txt", "w") as f:
    f.write(result)
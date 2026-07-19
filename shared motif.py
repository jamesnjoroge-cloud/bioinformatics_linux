from Bio import SeqIO

records = list(SeqIO.parse("rosalind_lcsm.txt", "fasta"))
sequences = [str(record.seq) for record in records]

shortest= min(sequences, key=len)

others = [seq for seq in sequences if seq != shortest]

longest_match = ""

for i in range(len(shortest)):
    for j in range(i+1, len(shortest)+1):
        candidate= shortest[i:j]
        if len(candidate)> len(longest_match) and all(candidate in seq for seq in others):
            longest_match= candidate
print(longest_match)

with open("output.txt", "w") as f:
    f.write(longest_match)
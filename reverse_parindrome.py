from Bio import SeqIO

from Bio.Seq import Seq

records = list(SeqIO.parse("rosalind_revp.txt", "fasta"))
dna = str(records[0].seq)

results = []

for i in range(len(dna)):
    for length in range(4, 13):
        substring = dna[i:i+length]
        if len(substring) != length:
            continue
        seq_obj = Seq(substring)
        if substring == str(seq_obj.reverse_complement()):
            results.append(f"{i + 1} {length}")

for line in results:
    print(line)

with open("output.txt", "w") as output_file:
    output_file.write("\n".join(results))
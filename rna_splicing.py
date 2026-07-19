from Bio import SeqIO

records = list(SeqIO.parse("rosalind_splc.txt", "fasta"))
dna = records[0].seq
substrings = [str(record.seq) for record in records[1:]]

for substring in substrings:
    dna = dna.replace(substring, "")
print(dna)

protein = dna.translate(to_stop=True)
print(protein)

with open('output.txt', 'w') as f:
    f.write(str(protein))
from Bio import SeqIO, Entrez

Entrez.email = "jamesnjoroge.info@gmail.com"
with open("rosalind_frmt.txt", "r") as f:
    ids = list(f.read().split())

hundle = Entrez.efetch(db="nucleotide", id=ids, rettype = "fasta")
records = list(SeqIO.parse(hundle, "fasta"))
shortest_record = records[0]

for record in records:
    if len(record.seq) <= len(shortest_record.seq):
        shortest_record = record

final_output = shortest_record.format("fasta")

#print(final_output)
with open("output.txt", "w") as f:
    f.write(final_output)
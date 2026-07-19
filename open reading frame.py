from Bio import SeqIO
from Bio.Seq import Seq
records =list(SeqIO.parse("rosalind_orf.txt", "fasta"))
dna_seq = records[0].seq
reverse_seq = dna_seq.reverse_complement()

valid_protein = set()
for seq in (dna_seq, reverse_seq):
    for i in range(len(seq)):
        if seq[i:i+3] == "ATG":
            protein = seq[i:].translate(to_stop= True)
            if (len(protein)+1) * 3 <= len(seq)-i:
                 valid_protein.add(str(protein))

with open("output.txt", "w") as f:
    for protein in valid_protein:
        f.write(protein + "\n")
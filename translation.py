from Bio.Seq import Seq

with open("rosalind_prot.txt", "r") as f:
    rna_sequence = f.readline().strip()

protein_sequence = Seq(rna_sequence).translate(to_stop = True)

print(protein_sequence)
with open("output.txt", "w") as f:
    f.write(str(protein_sequence)) 
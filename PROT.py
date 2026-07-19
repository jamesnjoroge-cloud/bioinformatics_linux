from Bio.Seq import Seq

with open("rosalind_prot.txt", "r") as f:
    rna = f.read().strip()

protein = Seq(rna).translate(to_stop=True)

print(protein)
with open("output.txt", "w") as f:
    f.write(str(protein))
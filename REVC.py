from Bio.Seq import Seq

with open("rosalind_revc.txt", "r") as f:
    dna = Seq(f.read().strip())

reversed = dna.reverse_complement()
print(reversed)

with open("output.txt", "w") as f:
    f.write(str(reversed))
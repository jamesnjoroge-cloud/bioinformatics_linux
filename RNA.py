from Bio.Seq import Seq
with open("rosalind_rna.txt", "r") as f:
    dna = Seq(f.read().strip())

rna = dna.transcribe()

print(rna)
with open("output.txt", "w") as f:
    f.write(str(rna))
from Bio.Seq import Seq

with open("rosalind_revc.txt", "r") as f:
    dna = Seq(f.read().strip())

rev_comp = dna.reverse_complement()

with open("output.txt", "w") as f:
    f.write(str(rev_comp))
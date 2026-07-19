from Bio.Seq import Seq
with open("rosalind_orfr.txt", "r") as f:
    dna_seq = Seq(f.read().strip())
    reverse_comp = dna_seq.reverse_complement()

valid_protein = set()
for seq in (dna_seq, reverse_comp):
    for i in range(len(seq)):
        if seq[i:i+3] == 'ATG':
            protein = seq[i:].translate(to_stop=True)
            valid_protein.add(str(protein))

maximum_protein = max(valid_protein, key=len)
print(maximum_protein)

with open("output.txt", "w") as f:
    f.write(maximum_protein)
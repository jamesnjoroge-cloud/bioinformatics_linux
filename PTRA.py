from Bio.Seq import Seq
with open("rosalind_ptra.txt", "r") as f:
    lines = f.read().split()

dna_seq =lines[0].strip()
Protein_seq = lines[1].strip()
table = [1, 2, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 15]

for i in table:
    test_protein = Seq(dna_seq).translate(table = i, to_stop=True)
    if test_protein == Protein_seq:
        id = i
        break
print(id)
with open("output.txt", "w") as f:
    f.write(str(id))
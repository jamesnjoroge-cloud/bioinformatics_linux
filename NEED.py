from Bio import SeqIO, Entrez, Align
Entrez.email = "jamesnjoroge.info@gmail.com"
with open("rosalind_need.txt", "r") as f:
    id_list = f.read().split()

hundle = Entrez.efetch(db="nucleotide", id=id_list, rettype= "fasta")
records = list(SeqIO.parse(hundle, "fasta"))    
my_aligner = Align.PairwiseAligner()
my_aligner.substitution_matrix = Align.substitution_matrices.load("NUC.4.4")
my_aligner.open_gap_score = -10
my_aligner.extend_gap_score = -1

record1 = records[0].seq
record2 = records[1].seq
final_score = my_aligner.score(record1, record2)

print(final_score)
with open("output.txt", "w") as f:
    f.write(str(final_score))

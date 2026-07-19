from Bio import SeqIO, Align

records = list(SeqIO.parse("rosalind_subo.txt", "fasta"))

seq1 = str(records[0].seq)
seq2 = str(records[1].seq)

my_aligner = Align.PairwiseAligner()
my_aligner.mode = "local"
alignments = my_aligner.align(seq1, seq2)

print(alignments[0])
repeat = "TTAGGTATTTTCCAACAAGCTACGTCCCTCTCTC"

count1 = seq1.count(repeat)
count2 = seq2.count(repeat)

print(count1)
print(count2)

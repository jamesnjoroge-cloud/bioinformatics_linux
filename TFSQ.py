from Bio import SeqIO

records = SeqIO.convert("rosalind_tfsq.txt", "fastq", "output.txt", "fasta")
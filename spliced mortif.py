from Bio import SeqIO

records = list(SeqIO.parse("rosalind_sseq.txt", "fasta"))
dna = records[0].seq
subseq = records[1].seq

j = 0
subsequence = []
for i in range(len(dna) ):
    if j < len(subseq) and dna[i] == subseq[j]:
          j += 1
          subsequence.append(i + 1)

with open("output.txt", "w") as f:
    f.write(" ".join(map(str, subsequence)))
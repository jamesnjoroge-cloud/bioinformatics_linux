from Bio import SeqIO
from collections import Counter
records = list(SeqIO.parse("rosalind_cons.txt", "fasta"))
sequences =[str(record.seq)  for record in records]

a_row = []
t_row = []
g_row = []
c_row = []
for column in zip(*sequences):
    counts = Counter(column)
    a_row.append(counts.get('A', 0))
    c_row.append(counts.get('C', 0))
    g_row.append(counts.get('G', 0))
    t_row.append(counts.get('T', 0))

consensus=""
for i in range(len(a_row)):
    position_counts={
        'A': a_row[i],
        'C': c_row[i],
        'G': g_row[i],
        'T': t_row[i]
    }
    best_position = max(position_counts, key= position_counts.get)
    consensus += best_position



consensus_str = " ".join(map(str, a_row))

a_str = " ".join(map(str, a_row))
c_str = " ".join(map(str, c_row))
g_str = " ".join(map(str, g_row))
t_str = " ".join(map(str, t_row))

with open("output.txt", "w") as f:
    f.write(consensus + "\n")
    f.write("A: " + a_str + "\n")
    f.write("C: " + c_str + "\n")
    f.write("G: " + g_str + "\n")
    f.write("T: " + t_str + "\n")
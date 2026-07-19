from Bio import SeqIO
from numpy import record
k = 3
records = list(SeqIO.parse("rosalind_grph.txt", "fasta"))

for i in range(len(records)):
    for j in range(len(records)):
        if i != j and records[i].seq[-k:] == records[j].seq[:k]:
            print(records[i].id, records[j].id)
with open("output.txt", "w") as output_file:
    for i in range(len(records)):
        for j in range(len(records)):
            if i != j and records[i].seq[-k:] == records[j].seq[:k]:
                output_file.write(records[i].id + ' ' + records[j].id + '\n')
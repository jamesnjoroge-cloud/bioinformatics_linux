from Bio import SeqIO
with open("rosalind_bphr.txt", "r") as f:
    quality_score = int( f.readline())
    records = list(SeqIO.parse(f, "fastq"))

#print(records)
master_list = []
for record in records:
    my_list = record.letter_annotations["phred_quality"]
    master_list.append(my_list)

#print(master_list)
seq_length = len(master_list[0])
bad_score = 0 

for i in range(seq_length):
    column_total = 0
    for seq in master_list:
        column_total += seq[i]
    average = column_total/(len(master_list))
    if average < quality_score:
        bad_score += 1

with open("output.txt", "w") as f:
    f.write(str(bad_score))
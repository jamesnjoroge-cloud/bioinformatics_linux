from Bio import SeqIO

with open("rosalind_phre.txt", "r") as f:
    lines = f.readline()
    cutoff = int(lines)
    records = list(SeqIO.parse(f, "fastq"))

#print(cutoff)
#print(records)
counter = 0
for record in records:
    my_list=record.letter_annotations["phred_quality"]
    average = sum(my_list)/len(my_list)
    if average < cutoff:
        counter += 1

print(counter)
with open("output.txt", "w") as f:
    f.write(str(counter))
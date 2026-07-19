from Bio import SeqIO

with open("rosalind_filt.txt", "r") as f:
    lines = f.readline().split()
    quality_threshold = int(lines[0])
    percentage_threshold = int(lines[1])
    records = list(SeqIO.parse(f, "fastq"))

counter = 0

for record in records:
    my_list = record.letter_annotations["phred_quality"]
    good_bases = 0
    for i in my_list:
        if i >= quality_threshold:
            good_bases += 1
    percentage = (good_bases/len(my_list)) * 100

    if percentage >= percentage_threshold:
        counter += 1
print(counter)
with open("output.txt", "w") as f:
    f.write(str(counter))

print(record)
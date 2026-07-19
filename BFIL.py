from Bio import SeqIO

with open("rosalind_bfil.txt", "r") as f:
    quality_score = int(f.readline())
    records = list(SeqIO.parse(f, "fastq"))
with open("output.txt", "w") as f:
    for record in records:
        my_list = record.letter_annotations["phred_quality"]
        start_index = 0
        end_index = 0
        for i in range(0, len(my_list)):
            if my_list[i] >= quality_score:
                start_index = i
                break
        for j in reversed(range(len(my_list))):
            if my_list[j] >= quality_score:
                end_index = j
                break
        fina_seq = record[start_index:end_index + 1]
        f.write(fina_seq.format("fastq"))
#print(fina_seq.format("fastq").strip())
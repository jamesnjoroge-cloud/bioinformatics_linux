from Bio import SeqIO

records = list(SeqIO.parse("rosalind_long.txt", "fasta"))
sequences = [str(record.seq) for record in records]

def overlap_length(a, b):
    max_overlap = 0
    for length in range(1, min(len(a), len(b)) + 1):
        if a[-length:] == b[:length]:
            max_overlap = length
    return max_overlap

n = len(sequences)
next_in_chain = {}
overlap_sizes = {}

for i in range(n):
    best_overlap = -1
    best_j = -1
    for j in range(n):
        if i != j:
            ov = overlap_length(sequences[i], sequences[j])
            if ov > best_overlap:
                best_overlap = ov
                best_j = j
    next_in_chain[i] = best_j
    overlap_sizes[i] = best_overlap


predecessors = set(next_in_chain.values())
all_indices = set(range(n))
start = (all_indices - predecessors).pop()

superstring = sequences[start]
current = start

for _ in range(n - 1):
    next_index = next_in_chain[current]
    overlap = overlap_sizes[current]
    next_seq = sequences[next_index]
    superstring += next_seq[overlap:]
    current = next_index

with open("output.txt", "w") as output_file:
    output_file.write(superstring)  
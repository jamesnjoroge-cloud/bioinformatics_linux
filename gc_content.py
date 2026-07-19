from Bio import SeqIO

best_id = None
best_gc_content = 0.0

for record in SeqIO.parse("rosalind_gc.txt", "fasta"):
    seq = record.seq
    gc_count = seq.count("G") + seq.count("C")
    gc_content = (gc_count / len(seq)) * 100

    if gc_content > best_gc_content:
        best_gc_content = gc_content
        best_id = record.id

with open("output.txt", "w") as f:
    f.write(f"{best_id}\n{best_gc_content:.6f}")
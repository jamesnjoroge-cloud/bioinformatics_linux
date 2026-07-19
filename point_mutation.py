with open("rosalind_hamm.txt", "r") as f:
    seq1 = f.readline().strip()
    seq2 = f.readline().strip()

count = 0

for a, b in zip(seq1, seq2):
    if a != b:
        count += 1

print(count)

with open("output.txt", "w") as f:
    f.write(str(count)) 
with open("rosalind_hamm.txt", "r") as f:
    seq = f.read().split()
s = seq[0]
t = seq[1]

total_pos = 0

for i, j in zip(s, t):
    if i != j:
        total_pos += 1
with open("output.txt", "w") as f:
    f.write(str(total_pos))
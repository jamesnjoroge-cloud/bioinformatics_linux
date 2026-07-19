with open("rosalind_subs.txt", "r") as f:
    lines = f.read().strip().splitlines()
    s = lines[0]
    t = lines[1]
positions = []
for i in range(len(s) - len(t) + 1):
    if s[i:i +len(t)] == t:
        positions.append(i+1)
with open("output.txt", "w") as f:
    f.write(" ".join(map(str, positions)))
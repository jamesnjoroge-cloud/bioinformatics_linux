import math

with open("rosalind_lia.txt", "r") as f:
    parts = f.read().split()

k = int(parts[0])
N = int(parts[1])
n = 2**k
total_prob = 0

for x in range(N, n+1):
    current_prob = math.comb(n, x) * (0.25**x) * (0.75**(n-x))
    total_prob += current_prob

print(total_prob)
with open("output.txt", "w") as f:
    f.write(str(f"{total_prob:.3f}"))
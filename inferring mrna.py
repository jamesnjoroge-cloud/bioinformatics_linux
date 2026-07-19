with open("rosalind_mrna.txt", "r") as f:
    sequence = f.read().strip()

frequencies = {
    'M': 1, 'W': 1, 
    'F': 2, 'Y': 2, 'C': 2, 'H': 2, 'Q': 2, 'N': 2, 'K': 2, 'D': 2, 'E': 2,
    'I': 3,
    'P': 4, 'T': 4, 'V': 4, 'A': 4, 'G': 4,
    'L': 6, 'S': 6, 'R': 6
}

total_prob = 3

for i in sequence:
    total_prob *= frequencies[i]
    total_prob %= 1000000

with open("output.txt", "w") as f:
    f.write(str(total_prob))
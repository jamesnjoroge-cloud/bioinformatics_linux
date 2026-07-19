import requests
import re

with open("rosalind_mprt.txt") as f:
    ids = f.read().split()

pattern = "N(?=[^P][ST][^P])"

for uid in ids:
    response = requests.get(f"https://www.uniprot.org/uniprot/{uid}.fasta")
    fasta_text = response.text
    lines = fasta_text.split("\n")
    seq = "".join(lines[1:])
    
    positions = [str(m.start() + 1) for m in re.finditer(pattern, seq)]
    
    if positions:
        print(uid)
        print(" ".join(positions))
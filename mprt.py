from Bio import SeqIO
import requests
import re
import io
with open("rosalind_mprt.txt", "r") as f:
    lines = f.read().split()

pattern = "(?=(N[^P][ST][^P]))"

with open("output.txt", "w") as f:
           
    for oid in lines:
        parts = oid.split("_")
        fasta = requests.get(f"http://www.uniprot.org/uniprot/{parts[0]}.fasta").text
        try:
            response = SeqIO.read(io.StringIO(fasta), "fasta")
            protein = str(response.seq)
            locations = []
            for match in re.finditer(pattern, protein):
                position = match.start() + 1
                locations.append(str(position))
            if locations:
                f.write(oid + "\n")
                f.write(" ".join(locations) + "\n")

        except:
            continue
from Bio import Entrez
Entrez.email = "jamesnjoroge.info@gmail.com"
with open("rosalind_gbk.txt", "r") as f:
    lines = f.read().split()
    genus = lines[0]
    start_date = lines[1]
    end_date = lines[2]
search_term = f"{genus}[Organism] AND ({start_date}[Publication Date]:{end_date}[Publication Date])"
handle = Entrez.esearch(db="nucleotide", term=search_term)
record = Entrez.read(handle)
total_count = record["Count"]
print(total_count)
with open("output.txt", "w") as f:
    f.write(total_count)
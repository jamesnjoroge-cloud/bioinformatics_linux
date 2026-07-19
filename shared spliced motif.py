from Bio import SeqIO

records = list(SeqIO.parse("rosalind_lcsq.txt", "fasta"))
seq1 = records[0].seq
seq2 = records[1].seq

rows = len(seq1) + 1
cols = len(seq2) + 1

table = [[0] * cols for _ in range(rows)]

for i in range(1, rows):
    for j in range(1,cols):
        if seq1[i-1]==seq2[j-1]:
            table[i][j]=table[i-1][j-1]+1
        else:
            table[i][j]= max(table[i-1][j], table[i][j-1])

i = len(seq1)
j = len(seq2)

result=[]

while i > 0 and j > 0:
    if seq1[i-1] == seq2[j-1]:
        result.append(seq1[i-1])
        i -= 1
        j -= 1
    else:
        if table[i-1][j] > table[i][j-1]:
            i -=1
        else:
            j -= 1
lcs= "".join(reversed(result))
print(lcs)
with open("output.txt", "w") as f:
    f.write(lcs)
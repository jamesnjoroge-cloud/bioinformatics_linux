with open("rosalind_fibd.txt", "r") as f:
    lines = f.read().strip()

parts = lines.split()
n = int( parts[0])
m = int( parts[1])
ages = [1] + [0] * (m-1)
for months in range(2, n+1):
    newborns = sum(ages[1:])
    ages = [newborns] + ages[:-1]

print(sum(ages))

with open("output.txt", "w") as r:
    r.write(str(sum(ages)))
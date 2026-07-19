with open('rosalind_subs.txt', 'r') as file:
    s = file.readline().strip()
    t = file.readline().strip()

for i in range(len(s) - len(t) + 1):
    if s[i:i+len(t)] == t:
        print(i + 1, end=' ')

with open("output.txt", "w") as output_file:
    for i in range(len(s) - len(t) + 1):
        if s[i:i+len(t)] == t:
            output_file.write(str(i + 1) + ' ')
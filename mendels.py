with open ("rosalind_iprb.txt", "r") as f:
    k, m, n = map(int, f.readline().strip().split())

total = k + m + n
case1 = (n/total) * ((n - 1) / (total - 1))
case2 = 2 * (m/total) * (n / (total - 1)) * 0.5
case3 = (m/total) * ((m - 1) / (total -1)) * 0.25

recessive_p = case1 + case2 + case3
dominant_p = 1 - recessive_p

probability = dominant_p

print(probability)

with open("output.txt", "w") as f:
    f.write(str(probability))
    
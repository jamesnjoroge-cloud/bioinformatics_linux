with open("rosalind_fib.txt", "r") as f:
    n, k = map(int, f.read().strip().split())

fib = {}
fib[1] = 1
fib[2] = 1
for i in range(3, n + 1):
    fib[i] = fib[i - 1] + k * fib[i - 2]

with open("output.txt", "w") as f:
    f.write(str(fib[i]))
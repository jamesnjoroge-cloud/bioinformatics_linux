import math
import itertools

with open("rosalind_perm.txt", "r") as f:
    line = f.read().strip()
n = int(line)

total_counter = math.factorial(n)

genes =list(range(1, n+1))

all_orders = itertools.permutations(genes)

# 1. Open your notebook to write
with open("output.txt", "w") as f:
    # 2. Write the total count first (convert it to string, add a newline)
    f.write(str(total_counter) + "\n")
    
    # 3. Indent your loop to stay inside the open file
    for current_permutation in all_orders:
        # Tool 4: Convert the numbers to strings and join them with a space
        formatted_string = " ".join(map(str, current_permutation))
        
        # Write the formatted string to the file with a newline
        f.write(formatted_string + "\n")
with open('rosalind_iev.txt', 'r') as file:
    counts = list(map(int, file.readline().strip().split()))

counts_dict = {
    'AA-AA': counts[0],
    'AA-Aa': counts[1],
    'AA-aa': counts[2],
    'Aa-Aa': counts[3],
    'Aa-aa': counts[4],
    'aa-aa': counts[5]
}

expected = (
    counts_dict['AA-AA'] *2 * 1.0 +
    counts_dict['AA-Aa'] * 2 * 1.0 +
    counts_dict['AA-aa'] *2 * 1.0 +
    counts_dict['Aa-Aa'] * 2 * 0.75 +
    counts_dict['Aa-aa'] * 2 * 0.5 +
    counts_dict['aa-aa'] * 2 * 0.0
)
print(expected)
with open("output.txt", "w") as output_file:
    output_file.write(str(round(expected, 3)))
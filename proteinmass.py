with open("rosalind_prtm.txt", "r") as file:
    protein_sequence = file.readline().strip()

with open("rosalind_prtm.txt", "r") as f:
    protein = f.read().strip()

mass_table = {
    'A': 71.03711, 'R': 156.10111, 'N': 114.04293, 'D': 115.02694,
    'C': 103.00919, 'E': 129.04259, 'Q': 128.05858, 'G': 57.02146,
    'H': 137.05891, 'I': 113.08406, 'L': 113.08406, 'K': 128.09496,
    'M': 131.04049, 'F': 147.06841, 'P': 97.05276, 'S': 87.03203,
    'T': 101.04768, 'W': 186.07931, 'Y': 163.06333, 'V': 99.06841
}
total_mass = sum(mass_table[aa] for aa in protein_sequence)
print(total_mass)

with open("output.txt", "w") as output_file:    
    output_file.write(str(round(total_mass, 3)))

from Bio.Seq import Seq

my_seq = Seq("AGTACACTGGT")
print("Sequence:", my_seq)
print("Complement:", my_seq.complement())
print("Reverse complement:", my_seq.reverse_complement())
# Amino Acid Composition Calculator

# Take protein sequence input from user
sequence = input("Enter protein sequence: ").upper()

# Total length of sequence
total_length = len(sequence)

print("\nTotal Amino Acids:", total_length)

# List of amino acids
amino_acids = "ARNDCEQGHILKMFPSTWYV"

print("\nAmino Acid Composition:\n")

# Loop through each amino acid
for aa in amino_acids:

    # Count amino acid
    count = sequence.count(aa)

    # Calculate percentage
    percentage = (count / total_length) * 100

    # Print result
    if count > 0:
        print(aa, ": Count =", count, ", Percentage =", round(percentage, 2), "%")

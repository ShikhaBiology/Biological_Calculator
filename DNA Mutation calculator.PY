sequence1 = input("Enter original DNA sequence: ").upper()
sequence2 = input("Enter mutated DNA sequence: ").upper()

if len(sequence1) != len(sequence2):

    print("Sequences must have the same length!")

else:

    mutation_count = 0

    for i in range(len(sequence1)):

        if sequence1[i] != sequence2[i]:

            mutation_count += 1

            print(f"Position {i+1}: {sequence1[i]} → {sequence2[i]}")

    print("\nTotal Mutations:", mutation_count)

def count_bird_species_and_save_difference(file1, file2, output_file):
    # Read the first file, convert species to lowercase, and store in a set
    with open(file1, 'r') as f1:
        species_file1 = set(f1.read().lower().strip().split('\n'))

    # Read the second file, convert species to lowercase, and store in a set
    with open(file2, 'r') as f2:
        species_file2 = set(f2.read().lower().strip().split('\n'))

    # Count the total number of species in each file
    total_species_file1 = len(species_file1)
    total_species_file2 = len(species_file2)

    # Find common species between the two files
    common_species = species_file1.intersection(species_file2)
    total_common_species = len(common_species)

    # Find species in file1 not present in file2
    unique_species_file1 = species_file1 - species_file2

    # Save the unique species from file1 to a new file
    with open(output_file, 'w') as f_out:
        for species in sorted(unique_species_file1):
            f_out.write(species + '\n')

    # Print the results
    print(f"Total bird species in {file1}: {total_species_file1}")
    print(f"Total bird species in {file2}: {total_species_file2}")
    print(f"Number of species both files have in common: {total_common_species}")
    print(f"List of species from {file1} not present in {file2} saved to {output_file}")


# Replace 'file1.txt' and 'file2.txt' with the actual file paths
file1_path = 'species.txt'
file2_path = 'species2.txt'
output_file_path = 'New-Birds/need_more_pics.txt'

count_bird_species_and_save_difference(file1_path, file2_path, output_file_path)

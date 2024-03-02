import os


def list_folders_to_file(start_dir, output_file):
    # Check if the starting directory exists
    if not os.path.exists(start_dir):
        print(f"The directory {start_dir} does not exist.")
        return

    with open(output_file, 'w') as f:
        # Walk through the starting directory
        for entry in os.listdir(start_dir):
            full_path = os.path.join(start_dir, entry)
            # Check if the entry is a directory
            if os.path.isdir(full_path):
                f.write(entry + '\n')

    print(f"Folder names have been written to {output_file}.")


if __name__ == "__main__":
    start_dir = input("Enter the directory to list folders from: ")
    output_file = "species.txt"
    list_folders_to_file(start_dir, output_file)

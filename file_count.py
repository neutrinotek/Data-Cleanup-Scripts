import os


def count_files_in_folders(start_dir):
    # Check if the starting directory exists
    if not os.path.exists(start_dir):
        print(f"The directory {start_dir} does not exist.")
        return

    # Walk through all directories in the starting directory
    for root, dirs, _ in os.walk(start_dir):
        for dir_name in dirs:
            full_dir_path = os.path.join(root, dir_name)
            # Count the number of files in this directory
            num_files = len(
                [name for name in os.listdir(full_dir_path) if os.path.isfile(os.path.join(full_dir_path, name))])

            # Check if the number of files is less than 5
            if num_files < 5:
                print(f"Folder '{dir_name}' contains less than 5 files: {num_files} files.")


if __name__ == "__main__":
    start_dir = input("Enter the starting directory: ")
    count_files_in_folders(start_dir)

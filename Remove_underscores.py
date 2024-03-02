import os


def rename_files_folders(start_dir):
    # Check if the starting directory exists
    if not os.path.exists(start_dir):
        print(f"The directory {start_dir} does not exist.")
        return

    # Walk through all directories and files in the starting directory
    for root, dirs, files in os.walk(start_dir, topdown=False):
        # Rename files
        for name in files:
            if '_' in name:
                new_name = name.replace('_', ' ')
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
                print(f"Renamed file {name} to {new_name}")

        # Rename directories
        for name in dirs:
            if '_' in name:
                new_name = name.replace('_', ' ')
                os.rename(os.path.join(root, name), os.path.join(root, new_name))
                print(f"Renamed directory {name} to {new_name}")


if __name__ == "__main__":
    start_dir = input("Enter the starting directory: ")
    rename_files_folders(start_dir)

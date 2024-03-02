import os

def rename_images_in_subfolders(directory_path):
    """Rename all images in each subfolder within the given directory."""
    for subdir, _, files in os.walk(directory_path):
        # Skip the root directory, only process subdirectories
        if subdir == directory_path:
            continue
        
        folder_name = os.path.basename(subdir)
        image_counter = 1
        
        for file in files:
            file_path = os.path.join(subdir, file)
            file_extension = os.path.splitext(file_path)[1]
            new_file_name = f"{folder_name}({image_counter}){file_extension}"
            new_file_path = os.path.join(subdir, new_file_name)
            
            os.rename(file_path, new_file_path)
            print(f"Renamed {file} to {new_file_name}")
            image_counter += 1

if __name__ == "__main__":
    directory_path = input("Please enter the main directory path to process: ")
    rename_images_in_subfolders(directory_path)

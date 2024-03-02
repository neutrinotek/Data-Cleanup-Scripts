from bing_image_downloader import downloader
import os
import shutil

# Path to the .txt file containing bird species names
file_path = 'need_more_pics.txt'

# Number of images you want to download for each bird species
num_images = 100  # Adjust as necessary, with the understanding of variability

with open(file_path, 'r') as file:
    bird_species = file.read().splitlines()

for bird in bird_species:
    folder_name = bird.replace(" ", "_")

    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    downloader.download(bird, limit=num_images, output_dir=folder_name, adult_filter_off=True, force_replace=False,
                        timeout=60)

    # Move files from the sub-folder to the main folder and delete the sub-folder
    sub_folder_path = os.path.join(folder_name, bird.replace(" ", "_"))
    if os.path.exists(sub_folder_path):
        for filename in os.listdir(sub_folder_path):
            shutil.move(os.path.join(sub_folder_path, filename), folder_name)
        os.rmdir(sub_folder_path)  # Remove the now empty sub-folder

    # Rename files to the desired format
    all_files = [f for f in os.listdir(folder_name) if os.path.isfile(os.path.join(folder_name, f))]
    all_files.sort()  # Sort files to maintain order
    for i, filename in enumerate(all_files, start=1):
        # Ensure the new filename is strictly in the format "001.jpg", "002.jpg", etc.
        new_filename = f'{i:03}.jpg'
        os.rename(os.path.join(folder_name, filename), os.path.join(folder_name, new_filename))

# Data-Cleanup-Scripts
A collection of short scripts to help me cleanup data for model training.

**Folder_names.py** - Outputs names of all folders within a directory to a line delimited .txt file. 

**Remove_underscores.py**- Self explanatory. Removes underscores from file names and folder names.

**Rename_Files.py** - Goes through all folders in a directory, renames files within each folder to the name of the directory followed by a number.

**Unique_Species.py** - Compares two different line delimited files to determine how many categories each list has in common, saves the names that are unique to the first file into a separate .txt file.

**file_count.py** - goes through folders in a directory, returns the names of folder with less than 5 files within them.

**image-downloader.py** - uses bing-image-downloader library to go through a .txt file and download images of the names in the file. Saves them to a folder with the same name as the category.

import os
import shutil
from tqdm import tqdm

# Set the root directory to search for mp4 files
root_dir = 'udacity computer vision'

# Set the target directory to copy the mp4 files to
target_dir = 'udacity computer vision videos'

# Create the target directory if it does not exist
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# Get the total number of mp4 files
count = 0
# Walk through all the subdirectories in the root directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    # Loop through all the filenames
    for filename in filenames:
        # Check if the file is an mp4 file
        if filename.endswith('.mp4'):
        	count = count+1

# Initialize the progress bar and the total size
pbar = tqdm(total=count, unit='files', unit_scale=True, desc='Copying files')
total_size = 0

# Walk through all the subdirectories in the root directory
for dirpath, dirnames, filenames in os.walk(root_dir):
    # Loop through all the filenames
    for filename in filenames:
        # Check if the file is an mp4 file
        if filename.endswith('.mp4'):
            # Construct the full file path
            file_path = os.path.join(dirpath, filename)
            # Copy the file to the target directory
            shutil.copy(file_path, target_dir)
            # Update the total size
            total_size += os.path.getsize(file_path)
            # Update the progress bar
            pbar.update(1)

# Convert the total size to gigabytes
total_size_gb = total_size / 1e9

# Close the progress bar and display the total size
pbar.close()
print(f'{root_dir} || {count} mp4 files || total size: {total_size_gb:.2f} GB')

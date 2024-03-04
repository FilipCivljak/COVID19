import os
import random
import shutil
from kaggle.api.kaggle_api_extended import KaggleApi

def split_data(folder_path, num_folders):
    if num_folders <= 0:
        print("Number of folders must be positive.")
        return

    # Get the names of the subfolders inside the original dataset
    subfolders = [folder for folder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, folder))]

    # Create directories for the new datasets
    for i in range(num_folders):
        new_folder_path = os.path.join('.', f'Hospital_{i + 1}')
        os.makedirs(new_folder_path, exist_ok=True)
        for subfolder in subfolders:
            os.makedirs(os.path.join(new_folder_path, subfolder), exist_ok=True)

    # Iterate over subfolders
    for subfolder in subfolders:
        subfolder_path = os.path.join(folder_path, subfolder)

        # Get the names of the subdirectories within the subfolder
        subdirectories = [dir for dir in os.listdir(subfolder_path) if os.path.isdir(os.path.join(subfolder_path, dir))]

        # Iterate over subdirectories
        for directory in subdirectories:
            directory_path = os.path.join(subfolder_path, directory)

            # Get all the image files in the subdirectory
            images = [image for image in os.listdir(directory_path) if image.endswith('.png')]
            random.shuffle(images)

            # Distribute images randomly among the datasets
            subset_size = len(images) // num_folders
            start_idx = 0
            for i in range(num_folders):
                new_folder_path = os.path.join('.', f'Hospital_{i + 1}', subfolder, directory)
                os.makedirs(new_folder_path, exist_ok=True)  # Ensure destination directory exists
                for image in images[start_idx: start_idx + subset_size]:
                    src_path = os.path.join(directory_path, image)
                    dst_path = os.path.join(new_folder_path, image)
                    shutil.copy(src_path, dst_path)
                start_idx += subset_size

if __name__ == "__main__":
    api = KaggleApi()
    api.authenticate()

    # Download dataset files
    api.dataset_download_files(dataset='tawsifurrahman/covid19-radiography-database', path='./data', unzip=True)

    print("Download finished successfully")

    folder_path = './data/COVID-19_Radiography_Dataset'
    num_folders = 3

    split_data(folder_path, num_folders)



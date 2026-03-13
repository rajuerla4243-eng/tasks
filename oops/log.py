import os
import shutil

# Folder path containing files
folder_path = r"C:\Users\rajue\OneDrive\Desktop\test files"

# Image extensions
image_extensions = ["png", "jpg", "jpeg", "gif", "bmp"]

for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):

        extension = file.split(".")[-1].lower()

        # If file is an image
        if extension in image_extensions:
            dest_folder = os.path.join(folder_path, "images")
        else:
            dest_folder = os.path.join(folder_path, extension)

        # Create folder if it does not exist
        if not os.path.exists(dest_folder):
            os.makedirs(dest_folder)

        # Move file
        shutil.move(file_path, os.path.join(dest_folder, file))

print("Files organized successfully!")
import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

def organize_files():
    folder_path = filedialog.askdirectory()

    if not folder_path:
        return

    image_extensions = ["png", "jpg", "jpeg", "gif", "bmp"]

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):

            extension = file.split(".")[-1].lower()

            # Image files
            if extension in image_extensions:
                dest_folder = os.path.join(folder_path, "images")
            else:
                dest_folder = os.path.join(folder_path, extension)

            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)

            shutil.move(file_path, os.path.join(dest_folder, file))

    messagebox.showinfo("Success", "Files organized successfully!")

# GUI window
root = tk.Tk()
root.title("File Organizer")
root.geometry("300x150")

label = tk.Label(root, text="Organize Files by Extension", font=("Arial", 12))
label.pack(pady=15)

button = tk.Button(root, text="Select Folder", command=organize_files)
button.pack(pady=10)

root.mainloop()
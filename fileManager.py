import os
from tkinter import filedialog

# Gets the file path from the user input and formats it to be used

# Gets the file types from the folder path
# Returns a set of file types
def get_file_types(folder_path):
    global file_types
    file_types = set()

    # Iterate through all files in the folder
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            file_extension = os.path.splitext(file)[1].lower()  # Get the extension
            if file_extension:
                file_types.add(file_extension)

    return file_types

# def openFile():
#     filepath = filedialog.askdirectory()

import os

def get_file_path(filePath):
    # Get the folder path from the user
    folder_path = filePath 
    file_types = get_file_types(folder_path)
    return folder_path, file_types


def get_file_types(folder_path):
    file_types = set()

    # Iterate through all files in the folder
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            file_extension = os.path.splitext(file)[1].lower()  # Get the extension
            if file_extension:
                file_types.add(file_extension)

    return file_types
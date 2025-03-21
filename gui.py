import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import os

# Function called when a checkbox is clicked
def on_checkbox_change(checkbox_value, checkbox_var):
   print(f"Checkbox {checkbox_value} is {'checked' if checkbox_var.get() else 'unchecked'}")
   
def get_file_types(folder_path):
    file_types = set()

    # Iterate through all files in the folder
    for file in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, file)):
            file_extension = os.path.splitext(file)[1].lower()  # Get the extension
            if file_extension:
                file_types.add(file_extension)

    return file_types

# def turn_set_into_list(file_types):
#     return list(file_types)



# Example usage:
folder_path = r"C:\Users\isaac\Downloads"  # Change this to your folder path
file_types = get_file_types(folder_path)

for i in file_types:
    print("filetype: ", i)
print("File types found:", file_types)

# listIntoSet = turn_set_into_list(file_types)
# print("set turned into a list: ", listIntoSet)

# function to create the checkboxes for each file type
def create_checkboxes(root, num_checkboxes):
    checkboxes = []
    rowVal = 2
    colVal = 0
    
    for i in num_checkboxes:
        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(
            root,
            text = i,
            variable = checkbox_var,
            command = lambda i=i, var = checkbox_var: on_checkbox_change(i, var)
        )
        print(checkbox)
        
        # Place checkbox in the screen
        checkbox.place(x=20 + colVal * 100, y=40 + rowVal * 30)

        # Move to the next column
        colVal += 1

        # If 5 checkboxes are placed in a row, move to the next row
        if colVal >= 5:
            colVal = 0  # Reset to first column
            rowVal += 1  # Move to the next row

        checkboxes.append(checkbox_var)
        
    return checkboxes


root = tk.Tk()
# sets the title of the window
root.title("File Manager")

# sets the size of the window
height = 600
width = 600

# sets the window to open in the center of the screen
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)

root.geometry(f'{width}x{height}+{x}+{y}')

# Display text telling the user to enter the folder path
folderPathLabel = Label(root, text="Folder Path you want orgonized", justify='left')
folderPathLabel.place(x=10, y=20)

# Text box to get the path of the users folder
getFolderPath = tk.Text(root, height=1, width=45)
getFolderPath.place(x=200, y=20)

textSelectFileExtension = Label(root, text="Select File Extension")
textSelectFileExtension.place(x=50, y=60)

checkboxes = create_checkboxes(root, file_types)

# start the main event loop, this is required for the window to appear
root.mainloop()



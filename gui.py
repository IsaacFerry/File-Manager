import tkinter as tk
from tkinter import *
from tkinter import filedialog
import os
import fileManager

# Function called when a checkbox is clicked
def on_checkbox_change(checkbox_value, checkbox_var):
   print(f"Checkbox {checkbox_value} is {'checked' if checkbox_var.get() else 'unchecked'}")
   print("test: ", checkbox_value, checkbox_var.get())
   

# function to create the checkboxes for each file type
def create_checkboxes(root, file_types):
    checkboxes = []
    rowVal = 2
    colVal = 0
    
    for file_type in file_types:
        checkbox_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(
            root,
            text=file_type,
            variable=checkbox_var,
            command=lambda ft=file_type, var=checkbox_var: on_checkbox_change(ft, var)
        )
        checkbox.place(x=20 + colVal * 100, y=40 + rowVal * 30)
        colVal += 1

        if colVal >= 5:
            colVal = 0
            rowVal += 1

        checkboxes.append((file_type, checkbox_var, checkbox))
        
    return checkboxes

# Remove checkboxes from the GUI
def delete_checkboxes(checkbox_list):
    for file_type, checkbox_var, checkbox_widget in checkbox_list:
        checkbox_widget.destroy()
    return []


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Manager")
        # sets the size of the window
        height = 600
        width = 600

        # sets the window to open in the center of the screen
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
                
        self.geometry(f'{width}x{height}+{x}+{y}')
        
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        self.selected_path = ""
        
        for i in (folderPage, orgonizePage):
            frame = i(self.container, self)
            self.frames[i] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(folderPage)
        
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        
# Function to open a file dialog and get the folder path
def openFile():
    filepath = filedialog.askdirectory()
    return filepath

def printPath():
    print(openFile())
    

# Page for the user to enter the folder path
class folderPage(tk.Frame):
    
    def __init__(self, parent, controller):
        self.controller = controller
        
        path = StringVar()
        tk.Frame.__init__(self, parent)
        
        # Display text telling the user to enter the folder path
        folderPathLabel = Label(self, text="Enter the folder path you want to orgonize", justify='left')
        folderPathLabel.place(x=20, y=20)
        

        # Text box to get the path of the users folder
        global getFolderPath
        getFolderPath = tk.Text(self, width=40, height=1)
        getFolderPath.place(x=255, y=20)
        
        print("The entered folder path: ", getFolderPath)
        
        # Orgonize page button
        button = tk.Button(self, text="Go to Organize Page", command=lambda: self.go_to_organize_page(controller))
        button.place(x=460, y=50)
        
        # Find folder button
        btnFindFolder = tk.Button(self, text="Find Folder", command= self.choose_folder)
        btnFindFolder.place(x=255, y=50)
        
    # Function to open the file dialog and set the folder path
    def choose_folder(self):
        path = openFile()
        if path:
            getFolderPath.delete("1.0", "end")
            getFolderPath.insert("end", path)
            self.controller.selected_path = path
            print(path)
            
    # Function to go to the orgonize page        
    def go_to_organize_page(self, controller):
        
        path = getFolderPath.get("1.0", "end-1c").strip().strip('"')
        if not path or not os.path.exists(path):
            print("Please select a valid folder path before continuing.")
            return
        controller.selected_path = path
        controller.frames[orgonizePage].load_checkboxes()
        controller.show_frame(orgonizePage)



# Page for the user to select the file types to orgonize           
class orgonizePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Display text telling the user to select the file extension
        textSelectFileExtension = Label(self, text="Select the file extension you want to orgonize into their respective folders")
        textSelectFileExtension.place(x=20, y=30)

        self.checkboxes = [] 
        
        # Button to go back to the folder page
        btnBack = tk.Button(self, text = "Back", command=lambda: [controller.show_frame(folderPage), self.backButton()])
        btnBack = btnBack.place(x=20, y=550)
        
        # Button to move the files to their respective folders
        btnSave = tk.Button(self, text="Save", command=self.save_selected_checkboxes)
        btnSave = btnSave.place(x=540, y=550)
        
    # Function to load the checkboxes based on the selected folder path
    def load_checkboxes(self):
        file_path = self.controller.selected_path
        if not os.path.exists(file_path):
            print("Invalid path entered.")
            return
        
        file_types = fileManager.get_file_types(file_path)
        self.checkboxes = create_checkboxes(self, file_types)
        
    # Function to save the selected checkboxes and move files
    def save_selected_checkboxes(self):
        selected_file_types = []
        for file_type, var, _ in self.checkboxes:
            if var.get():
                selected_file_types.append(file_type)

        print("Selected file types:", selected_file_types)
        if selected_file_types:
            fileManager.createFolders(self.controller.selected_path, selected_file_types)
            fileManager.moveFiles(self.controller.selected_path, selected_file_types)
           
    # Removes the checkboxes from the GUI        
    def backButton(self):
        self.checkboxes = delete_checkboxes(self.checkboxes)
        


# start the main event loop, this is required for the window to appear
app = App()
app.mainloop()



import os
import tkinter as tk

# Class to represent a file
class File():
    def __init__(self, name, type):
        self.name = name
        self.type = type

# Function to get the files in a directory
def get_dir_files(path) -> list:
    file_list = []
    folder = os.listdir(path)
    for file in folder:
        file = file.split(".")
        if len(file) < 2:
            file = [file[0]]
            file.append("folder")
        file_list.append(File(file[0], file[1]))
    return file_list

def display_files():
    # Create a new window
    window = tk.Tk()
    window.geometry("500x500")  # Set the window size

    # Create an input field
    input_field = tk.Entry(window, width=50)  # Set the width of the input field
    input_field.pack()

    # Create a table display
    table = tk.Listbox(window, width=70, height=20)  # Set the width and height of the table
    table.pack()

    # Function to update the table display
    def update_table():
        # Clear the table
        table.delete(0, tk.END)

        # Get the directory input from the input field
        dir_input = input_field.get()

        # Create a file to store the directory string
        with open("directory.txt", "w") as file:
            file.write(dir_input)

        # Get the file list
        file_list = get_dir_files(dir_input)

        # Add each file to the table
        for file in file_list:
            table.insert(tk.END, f"a {file.type} called {file.name}")

    # Create a button to trigger the update
    button = tk.Button(window, text="Update", command=update_table)
    button.pack()

    # Check if directory.txt exists
    if os.path.exists("directory.txt"):
        # Read the directory string from the file
        with open("directory.txt", "r") as file:
            dir_input = file.read().strip()
        # Insert the directory string into the input field
        input_field.insert(0, dir_input)
        # Update the table display
        update_table()

    # Run the GUI event loop
    window.mainloop()

display_files()
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

    # Check if the directory exists
    if os.path.exists(path) == False:
        return
    
    folder = os.listdir(path)
    for file in folder:
        file = file.split(".")
        if len(file) < 2:
            file = [file[0]]
            file.append("folder")
        file_list.append(File(file[0], file[1]))

    # Sort the file list so that folders are displayed first, and then the rest is sorted alphabetically
    file_list.sort(key=lambda file: (file.type != "folder", file.type))
        
    return file_list

def display_files():
    # Create a new window
    window = tk.Tk()
    window.geometry("500x500")  # Set the window size

    # Create an input field
    input_field = tk.Entry(window, width=50)  # Set the width of the input field
    input_field.pack()

    # Create a table display
    table = tk.Listbox(window, width=70, height=20, selectmode=tk.SINGLE)
    table.pack()

    # Function to display a pop-up window with a message
    def display_popup(message):
        # Create a pop-up window
        popup = tk.Toplevel(window)
        popup.title("Alert!")
        popup.geometry("300x100")

        # Create a label to display the message
        label = tk.Label(popup, text=message)
        label.pack()

        # Create a button to close the pop-up window
        close_button = tk.Button(popup, text="Close", command=popup.destroy)
        close_button.pack()

    # Function to delete the selected file
    def delete_file():
        # Get the selected file from the table
        selected_file = table.get(table.curselection())

        # Extract the file name from the selected file string
        file_name = selected_file.split(" called ")[1] + "." + selected_file.split(" called ")[0][2:]

        # Construct the file path
        file_path = os.path.join(dir_input, file_name)

        print(file_path)
        # Check if the file exists
        if os.path.exists(file_path):
            # Delete the file
            os.remove(file_path)

            # Update the table display
            update_table()
            display_popup("File deleted successfully!")
        else:
            # Display a pop-up window with an error message
            display_popup("File does not exist!")


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

        # file_list will be None if the directory does not exist
        if file_list == None:
            display_popup("Directory does not exist!")
            return

        # Add each file to the table
        for file in file_list:
            table.insert(tk.END, f"a {file.type} called {file.name}")
            


    # Create a button to trigger the update
    button = tk.Button(window, text="Update", command=update_table)
    button.pack()
    # Add a button to delete the selected file
    delete_button = tk.Button(window, text="Delete Selection", command=delete_file)
    delete_button.pack()

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
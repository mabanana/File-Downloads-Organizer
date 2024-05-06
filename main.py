import os
import tkinter as tk

# Class to represent a file
class File():
    def __init__(self, name, type):
        self.name = name
        self.type = type



def main():
    # Function to get the files in a directory
    def get_dir_files(path) -> list:
        file_list = []

        # Check if the directory exists
        if os.path.exists(path) == False:
                return
        # Check if directory is accessible
        try:
            folder = os.listdir(path)   
        except PermissionError:
            display_popup("Access to the directory is denied!")
            back()

        # Add each file to the file list  
        for file in folder:
                file = file.split(".")
                if len(file) < 2:
                    file = [file[0]]
                    file.append("folder")
                file_list.append(File(file[0], file[1]))

        # Sort the file list so that folders are displayed first, and then the rest is sorted alphabetically
        file_list.sort(key=lambda file: (file.type != "folder", file.type))

        return file_list
    
    # Returns to previous directory
    def back():
        # Get the directory input from the input field
        dir_input = input_field.get()
        # remove last value split by "/"
        dir_list = dir_input.split("/")
        if len(dir_list) == 1:
            display_popup("You are in the root directory!")
            return
        dir_list.pop()
        dir_input = "/".join(dir_list)
        # Insert the directory string into the input field
        input_field.delete(0, tk.END)
        input_field.insert(0, dir_input)
        # Update the table display
        update_table()

    # Prints to console if a double click is detected on the listbox
    def on_double_click(event):
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        if "." not in value:
            # append value to the input field
            input_field.insert(tk.END, f"/{value}")
            update_table()

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
        file_name = selected_file

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
            if file.type == "folder":
                table.insert(tk.END, f"{file.name}")
            else:
                table.insert(tk.END, f"{file.name}.{file.type}")
    
    # Create a new window
    window = tk.Tk()
    window.geometry("500x500")  # Set the window size

    # Create an input field
    input_field = tk.Entry(window, width=50)  # Set the width of the input field
    input_field.pack()

    # Create a table display
    table = tk.Listbox(window, width=70, height=20, selectmode=tk.SINGLE)
    table.pack()
    # Bind the double click event to the table
    table.bind("<Double-1>", on_double_click)

    


    # Create a frame to hold the buttons
    button_frame = tk.Frame(window)
    button_frame.pack()

    # Add a button to trigger the update
    button = tk.Button(button_frame, text="Update", command=update_table)
    button.pack(side=tk.LEFT)

    # Add a button to delete the selected file
    delete_button = tk.Button(button_frame, text="Delete Selection", command=delete_file)
    delete_button.pack(side=tk.LEFT)

    # Add a button to go to previous directory
    back_button = tk.Button(button_frame, text="Back", command=back)
    back_button.pack(side=tk.LEFT)

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

main()
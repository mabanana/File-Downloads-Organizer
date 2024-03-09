import os

class File():
    def __init__(self, name, type):
        self.name = name
        self.type = type

def get_dir_files(target_dir, relative_path = True) -> list:
    path = target_dir
    if relative_path:
        curr_dir = os.path.abspath(os.getcwd())
        path = curr_dir + target_dir
    
    file_list = []
    folder = os.listdir(path)
    for file in folder:
        file = file.split(".")
        if len(file) < 2:
            file = [file[0]]
            file.append("folder")
        file_list.append(File(file[0], file[1]))
    return file_list

def print_all_files(file_list: list) -> None:
    for file in file_list:
        print(f"a {file.type} file called {file.name}")



target_dir = "/targetDir"
dir_input = input("what directory do you want to access?\n")
is_relative_path = input("is this path relative to the current directory?\ny/n\n")
is_relative_path = True if is_relative_path.lower() == "y" else False

if dir_input:
    target_dir = dir_input

target_file_list = get_dir_files(target_dir, is_relative_path)
print_all_files(target_file_list)



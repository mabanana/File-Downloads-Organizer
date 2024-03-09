import os

class File():
    def __init__(self, name, type):
        self.name = name
        self.type = type

target_dir = "/targetDir"
curr_dir = os.path.abspath(os.getcwd())

file_list = []

folder = os.listdir(curr_dir + target_dir)
for file in folder:
    file = file.split(".")
    file_list.append(File(file[0], file[1]))

for file in file_list:
    print(f"a {file.type} file called {file.name}")

import os
new_directory = "./tmp"
print(os.path.basename)
if os.path.exists(new_directory) and os.path.isdir(new_directory):
    os.chdir(new_directory) 
    print(f"changed directory to {os.getcwd()}")
else:
    print(f"Directory '{new_directory}' does not exists")
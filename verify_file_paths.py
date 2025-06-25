import os
path_to_check_file = "my_file11.txt"
path_to_check_dir = "C:/asiri/rules"


if os.path.exists(path_to_check_file):
    print(f"'{path_to_check_file}' exists.")
else:
    print(f"'{path_to_check_file}' does not exists.")

if os.path.exists(path_to_check_dir):
    print(f"'{path_to_check_dir}' exists. ")
else:
    print(f"'{path_to_check_dir}' does not exists")
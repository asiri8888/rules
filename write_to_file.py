import os
path_to_check_file = "my_file1.txt"
path_to_check_dir = "C:/asiri/rules"

# create dummy for demonstration
with open(path_to_check_file, 'w') as f:
    f.write("Hello world cccc")
 os.makedirs(path_to_check_dir, exist_ok=True)

import os
path_component1 = "C:/asiri/"
path_component2 = "rules/"
file_name = "my_file1.txt"

full_path = os.path.join(path_component1, path_component2, file_name)
print(f"joined path : {full_path}")
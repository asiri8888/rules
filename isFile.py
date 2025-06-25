import os
path1 = "C:/asiri/rules/my_file1.txt"
path2 = "C:/asiri/rules/"
path3 = "C:/asiri3333/rules/"

print(f"{path1} is a file: {os.path.isfile(path1)}")
print(f"{path2} is a directory: {os.path.isdir(path2)}")
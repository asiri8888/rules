import os
file_to_delete = "my_temp_file.txt"
# create a dummy file
with open(file_to_delete, 'w') as f:
    f.write("This is a temp file")

try:
    os.remove(file_to_delete)
    print(f"file {file_to_delete} removed successfully")
except FileNotFoundError:
    print(f"file {file_to_delete} not exists")
except Exception as e:
    print(f"Än error occured: {e}")
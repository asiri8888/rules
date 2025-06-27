import os
folder_to_remove = "my_new_folder"
try:
    os.rmdir(folder_to_remove)
    print(f"Directory {folder_to_remove} deleted successfully")

except Exception as e:
    print(f"Än error occured when deleting the folder {folder_to_remove}: {e}")
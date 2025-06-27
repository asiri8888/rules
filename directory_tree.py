import os
import shutil
# creatrea dummy source directory tree
source_dir ="my_source_project"
os.makedirs(os.path.join(source_dir, "css"),exist_ok=True)
os.makedirs(os.path.join(source_dir, "js"), exist_ok=True)
with open(os.path.join(source_dir, "ïndex.html"), "w") as f:
    f.write("body {}")
print(f"Created dummy source directory: {source_dir}")

# ----copy the directory tree
destination_dir = "my_backup_project"
try:
    # if destination _dir already exists and not empty copytree will raise
    # to overwrite, you woluld typically remove the destination first or handle mor
    shutil.copytree(source_dir, destination_dir)
    print(f"{source_dir} copied to {destination_dir} successfully")
    print("contents of the destination direciry")
    for root, dirs, files in os.walk(destination_dir):
        level = root.replace(destination_dir, '').count(os.sep)
        indent = '' * 4 * (level + 1)
        print(f"{indent}{os.path.basename(root)}/")
        subindent = '' * 4 * (level + 1)
       

        for f in files:
            print(f"{subindent}")
except FileExistsError:
    print(f"Error: Destination dir {destination_dir} already ")
except Exception as e:
    print(f"An error occured : {e}")
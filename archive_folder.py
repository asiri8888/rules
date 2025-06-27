import shutil
import os

# create a dummy file for archive
data_folder = "my_data _folder_for _archive"
os.makedirs(os.path.join(data_folder, "docs"), exist_ok=True)
with open(os.path.join(data_folder, "ïmportant.txt"), "w") as f:
    f.write("Important data here")
with open(os.path.join(data_folder, "docs", "notes.md"), "w") as f:
    f.write("# meeting notes")
print(f"created dummy file for archiving: {data_folder}")

#   ----create a Zip archive
archive_name = "my_data_archive"
try:
    # -- create my_data_archive.zip in the current directory
    # containing the contents of my_data_for_archive
    archive_path = shutil.make_archive(archive_name, 'zip', root_dir=data_folder)
    print(f"Archive created: {archive_path}")
    print(f"Does archive exists? {os.path.exists(archive_path)}")
except Exception as e:
    print(f"An error occured : {e}")
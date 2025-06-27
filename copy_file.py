import os
import shutil
# create a dummy file source
source_file = "source_doc.txt"
with open(source_file, "w") as f:
    f.write("This is a original contnt")
print(f"created {source_file} for coping")

# --copy the filw
dectination_file = "copied_doc.txt"
try:
    shutil.copy(source_file,dectination_file)
    print(f"{source_file} copied to {dectination_file} successfully")
    print(f"content of {dectination_file} : {open(dectination_file)}")
except FileNotFoundError:
    print(f"Error: source file {source_file} not found")
except Exception as e:
    print(f"Error : {e}")

    #  ---cleanup
if os.path.exists(source_file):
    os.remove(source_file)
if os.path.exists(dectination_file):
    os.remove(dectination_file)

print("cleaned up dummy files")
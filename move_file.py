import shutil
import os
# create dummy file and target directory
file_to_move = "report.pdf"
target_dir = "ärchives"
with open(file_to_move, "w") as f:
    f.write("confidential report data")
os.makedirs(target_dir, exist_ok=True)
print(f"created {file_to_move} and {target_dir}")


#  move the file
try:
    shutil.move(file_to_move, target_dir)
    print(f"{file_to_move} moved to {target_dir} successfully")
    print(f"new path: {os.path.join(target_dir, file_to_move)}")
except FileNotFoundError:
    print(f"{file_to_move} file not found")
except Exception as e:
    print(f"An error in moving file: {e}")


## ---cleanup
if os.path.exists(target_dir):
    shutil.rmtree(target_dir) # use rmtree as target_dir now contain
print("cleaned up dummy directory")
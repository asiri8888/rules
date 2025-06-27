import os
old_name = "old_file.txt"
new_name = "new_file.txt"
'''with open(old_name, 'w') as f:
    f.write("content of old file")'''

try:
    os.rename(old_name, new_name)
    print(f"renamed {old_name} to {new_name}")
except FileNotFoundError:
    print(f"{old_name} file not exists")
except FileExistsError:
    print(f"{new_name} file already exists")
except Exception as e:
    print(f"än error occusred: {e}")
import subprocess
import sys
def execute_command(command, capture_output=True, Text=True, check=False):
    try:
        result = subprocess.run(
            command,
            capture_output=capture_output,
            text = text,
            check=check,
            shell=isinstance(command, str)
                )
    return result
except subprocess.ca as e:

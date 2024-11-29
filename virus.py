
import os

# Specify the file path
file_path = r"C:\path\to\your\file.txt"

try:
    # Delete the file
    os.remove(file_path)
    print(f"File {file_path} has been deleted.")
except FileNotFoundError:
    print(f"File {file_path} not found.")
except PermissionError:
    print(f"Permission denied: {file_path}")

import os

# Set the project root path
project_root = os.getcwd()  # Gets the current working directory

# Define directories to exclude
excluded_dirs = [".venv", ".vscode"]
exclude_entire_dirs = False  # Set to True to exclude entire directories, False to exclude only subdirectories

# Initialize the output files
raw_path_file = "raw-path.txt"
paths_file = "paths.py"

# Clear previous content in the output files
for file in [raw_path_file, paths_file]:
    if os.path.exists(file):
        os.remove(file)

# Function to check if a path should be excluded
def should_exclude(path):
    relative_path = os.path.relpath(path, project_root)  # Get the relative path from the project root
    for dir in excluded_dirs:
        if relative_path.startswith(dir):  # Check if the path starts with the excluded directory
            return True, relative_path == dir  # Return if it's excluded and if it's the main directory
    return False, False

# Generate raw-paths.txt and paths.py
paths_array = []

# Walk through the directory tree
for root, dirs, files in os.walk(project_root):
    # Process directories
    for dir_name in dirs:
        full_path = os.path.join(root, dir_name)
        excluded, is_main_dir = should_exclude(full_path)

        if not excluded:
            # Add the directory to raw-path.txt
            with open(raw_path_file, 'a', encoding='utf-8') as f:
                f.write(full_path + '\n')  # Write directory without trailing backslash
            paths_array.append(full_path)  # Add to paths array for paths.py without trailing backslash

    # Process files
    for file_name in files:
        full_path = os.path.join(root, file_name)
        excluded, _ = should_exclude(full_path)

        if not excluded:
            with open(raw_path_file, 'a', encoding='utf-8') as f:
                f.write(full_path + '\n')
            paths_array.append(full_path)  # Add to paths array for paths.py

# Write paths.py file
with open(paths_file, 'w', encoding='utf-8') as f:
    python_array = "paths = [\n"
    for path in paths_array:
        # Ensure paths are written as raw string literals (using r'')
        python_array += f"r'{path}',\n"
    python_array += "]"
    f.write(python_array)

print(f"File paths written to {paths_file}")
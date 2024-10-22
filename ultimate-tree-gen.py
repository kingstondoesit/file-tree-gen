import os

# Set the project root path
project_root = os.getcwd()  # Gets the current working directory

# Define directories to exclude
excluded_dirs = [".venv", ".vscode"]
exclude_entire_dirs = False  # Set to True to exclude entire directories, False to exclude only subdirectories

# Initialize the output files
raw_path_file = "raw-path.txt"
paths_file = "paths.py"
markdown_file = "movie-tree.md"

# Clear previous content in the output files
for file in [raw_path_file, paths_file, markdown_file]:
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
            full_path = os.path.join(root, (f'{dir_name}'+ '\\' + 'empty'))
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

# Write paths.py file without formatting for Python
with open(paths_file, 'w', encoding='utf-8') as f:
    python_array = "paths = [\n" + ",\n".join([f"'{path}'" for path in paths_array]) + "\n]"
    f.write(python_array)

# Function to build the file tree structure
def build_file_tree(paths):
    file_tree = {}
    
    for path in paths:
        # Remove the root from the path
        relative_path = path.replace(project_root, '').strip(os.sep)
        # Split the path into components (directories and files)
        parts = relative_path.split(os.sep)
        
        current = file_tree
        
        for part in parts:
            if part not in current:
                current[part] = {}
            current = current[part]

    return file_tree

# Function to write the file tree to Markdown format
def write_tree_to_md(file_tree, indent_level=0):
    output = ""
    indent = "│   " * indent_level  # Adjust the indentation for each level
    
    # Separate hidden files, non-hidden files, and directories
    hidden_files = sorted([key for key, sub_tree in file_tree.items() if key.startswith('.')])
    non_hidden_files = sorted([key for key, sub_tree in file_tree.items() if not key.startswith('.') and sub_tree == {}])
    directories = sorted([key for key, sub_tree in file_tree.items() if sub_tree != {}])
    
    # Write hidden files first
    for key in hidden_files:
        output += f"{indent}├──{key}  \n"

    # Write directories and recurse into them
    for idx, key in enumerate(directories):
        output += f"{indent}├──/{key}  \n"  # Add a backslash for directories
        output += write_tree_to_md(file_tree[key], indent_level + 1)

    # Write non-hidden files next, determining the last file in the loop
    for idx, key in enumerate(non_hidden_files):
        if idx == len(non_hidden_files) - 1:  # Check if it's the last file
            output += f"{indent}└──{key}  \n"  # Use the half vertical stick
        else:
            output += f"{indent}├──{key}  \n"  # Use the full vertical stick

    return output

def main():
    # Build the tree structure
    file_tree = build_file_tree(paths_array)
    
    # Write the tree structure to markdown
    tree_str = write_tree_to_md(file_tree)

    # Output File
    output_file = markdown_file  # Use the existing markdown file name
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"# File Tree Structure\n\n{project_root}\n\n{tree_str}\n")
    
    print(f"File tree structure written to {output_file}")

if __name__ == "__main__":
    main()
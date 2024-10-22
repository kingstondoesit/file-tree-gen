import os

# Set the project root path
project_root = os.getcwd()  # Gets the current working directory

# Load the paths from raw-path.txt
raw_path_file = "raw-path.txt"
markdown_file = "file-tree.md"

with open(raw_path_file, 'r', encoding='utf-8') as f:
    paths = [line.strip() for line in f.readlines()]

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
    file_tree = build_file_tree(paths)
    
    # Write the tree structure to markdown
    tree_str = write_tree_to_md(file_tree)

    # Output File
    with open(markdown_file, 'w', encoding='utf-8') as f:
        f.write(f"# File Tree Structure\n\n{project_root}\n\n{tree_str}\n")
    
    print(f"File tree structure written to {markdown_file}")

if __name__ == "__main__":
    main()
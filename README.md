# File Tree Generator

`ultimate-tree-gen` is a (customizable) python script that traverses a system directory and generates a structured file tree in Markdown format. It saves users looking to textually represent their project's file tree ample time and effort. The generated tree text is copiable and can be used anywhere, for any purporse.

![file-tree-gen demo](./Assets/treegen-demo.png)

## Features

- **Customizable Exclusion**: Easily configure directories to exclude from the file tree generation process, with options to exclude entire directories or just subdirectories.
- **Dynamic Path Generation**: It knows your project's root directory and crawls the directory tree to generate paths and sub-paths dynamically.
- **Markdown Output**: Outputs a neatly formatted Markdown file representing the project structure.
- **Cross-Platform Compatibility**: Works on any operating device that supports python.

<!-- - Generates a visual representation of the directory structure.
- Excludes specified directories. -->

## Requirements

- Python 3.x

## Usage

1. Clone the repository:

   ```bash
   git clone https://github.com/kingstondoesit/file-tree-gen.git
   ```

2. Navigate to the project directory:

   ``` bash
   cd file-tree-gen
   ```

3. Run the script:

   ``` bash
   python ultimate-tree-gen.py
   ```

4. The script generates a Markdown file named `file-tree.md` in the root dir with the directory location and a hierachical representation of the project's file structure.

## Customizable Options

- `excluded_dirs`: Specify directories to exclude from the file tree generation process. Separate multiple directories with commas. Default directory = `'node_modules'`.
- `exclude-entire-dirs`: Default value is `False`. Set to `True` to exclude entire directories instead of just their subdirectories.

Example:

   ``` python
   # Define directories to exclude
   excluded_dirs = ["node_modules", ".venv"]

   # Set exclusion mode
   exclude_entire_dirs = True  

   # specify output files
   raw_path_file = "raw-path.txt"
   paths_file = "paths.py"
   markdown_file = "file-tree.md"
   ```

The above configuration in `ultimate-file-tree.py` will exclude the `node_modules` and `.venv` directories entirely from the file tree generation process, instead of just their subdirectories.

You can modify the output file variables and specify your preferred output file names.

## Contributing

Contributions are welcome! If you find a bug or have a suggestion for improvement, please open an issue or submit a pull request on the GitHub repository.

1. Fork the repository.

2. Create a new branch for your changes.

   ``` bash
   git checkout -b <your-branch-name>
   ```

3. Make your changes and commit them with a commit message.

   ``` bash
   git commit -m "Added a new feature"
   ```

4. Push your changes to your forked repository

   ``` bash
   git push origin <your-branch-name>

   ```

5. Create a pull request to the main repository.

## License

This repo is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

# File Organizer

This script is designed to organize files in a directory based on their file extensions. It scans the specified directory, identifies files with matching extensions, and moves them to designated folders.

## Prerequisites

Before running the script, ensure you have the following installed:

- Python (version 3.10 or above)
- Required dependencies (e.g., `re`, `os`)

## Getting Started

1. Clone or download the repository to your local machine.
2. Open a terminal or command prompt and navigate to the project directory.

## Usage

To use the script, follow these steps:

1. Customize the script configuration:
   - Open the script file (`conf.toml`) in a text editor.
   - Modify the `conf` dictionary to define the file extensions and their corresponding folder names. For example:
   
```toml
   [files]
exclude = [

]
directrorys_to_monitor = [
"/data/data/com.termux/files/home/code/python/delete_files",
"/data/data/com.termux/files/home/",
"/data/data/com.termux/files/home/code/python/delete_files/cloud"
]

[organize]
stl = "/data/data/com.termux/files/home/code/python/delete_files/cloud/3d_print"
py = "/data/data/com.termux/files/home/code/python/delete_files/cloud/python"
txt = "/data/data/com.termux/files/home/code/python/delete_files/cloud/text"

```
   
2. Run the script:
   - In the terminal or command prompt, run the following command:
   
   ```bash
   python organize_files.py
   ```
   
   The script will start scanning the current directory for files matching the specified extensions and move them to the respective folders.
   
3. Review the output:
   - The script will display a message if a file already exists in the destination folder, indicating that it was not moved.
   - Once the script completes, check the specified destination folders to verify that the files have been organized according to their extensions.

## Notes

- The script utilizes regular expressions to match file names based on the specified extensions.
- If a file is excluded from the organization process (e.g., listed in the `EXCLUDE` variable), it will be skipped.
- Ensure that the destination folders specified in the configuration dictionary (`conf`) exist before running the script. If they don't exist, the script will attempt to create them.

## License

This project is licensed under the [MIT License](LICENSE).

---

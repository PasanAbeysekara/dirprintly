import os
import sys
from colorama import Fore, Style, init

# Initialize Colorama for color support
init(autoreset=True)

# Icons
DIRECTORY_ICON = "📁"
FILE_ICON = "📄"

def print_item(name, is_dir, depth):
    """Prints a directory or file with appropriate indentation and icons."""
    indent = "    " * depth
    icon = DIRECTORY_ICON if is_dir else FILE_ICON
    print(f"{Fore.GREEN}{indent}{icon} {name}")

def print_file_content(file_path, depth):
    """Prints the content of a file with indentation."""
    indent = "    " * (depth + 1)
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
            content = file.read().strip()
            print(f"{Fore.WHITE}{indent}{content[:100]}...")
            # Prints the first 100 characters followed by ellipsis to indicate more content
    except Exception as e:
        print(f"{Fore.RED}{indent}Error reading file: {e}")

def explore_directory_cli():
    """
    Entry point for the dirprintly console script.
    Determines the directory to explore based on command line arguments
    or defaults to the current working directory.
    """
    # Check if a directory is provided as a command-line argument.
    directory = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    explore_directory(directory)

def explore_directory(directory, depth=0):
    """Recursively explores and prints directory contents."""
    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            print_item(item, is_dir=True, depth=depth)
            explore_directory(item_path, depth + 1)
        else:
            print_item(item, is_dir=False, depth=depth)
            print_file_content(item_path, depth)

if __name__ == "__main__":
    root_directory = os.getcwd() if len(sys.argv) == 1 else sys.argv[1]
    explore_directory(root_directory)
    print(f"{Fore.CYAN}--- End of directory listing ---")

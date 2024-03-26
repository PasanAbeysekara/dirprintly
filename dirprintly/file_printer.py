import os
import sys
from colorama import Fore, Style, init

# Initialize Colorama
init(autoreset=True)

def print_header(file_path):
    header = f"\n{Fore.CYAN}{'=' * 80}\n{Style.BRIGHT}FILE: {file_path}\n{Fore.CYAN}{'=' * 80}\n"
    print(header)

def print_footer():
    footer = f"\n{Fore.YELLOW}{'-' * 80}\nEnd of file\n{Fore.YELLOW}{'-' * 80}\n"
    print(footer)

def print_directory(directory_path):
    print(f"{Fore.GREEN}DIRECTORY: {directory_path}/\n")

def print_file_contents(directory=None, print_all=False):
    if directory is None:
        directory = os.getcwd()

    for item in sorted(os.listdir(directory)):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            print_header(item_path)
            with open(item_path, 'r', encoding='utf-8', errors='ignore') as file:
                # Use Fore.WHITE for file content or another color that contrasts well with your terminal background
                print(Fore.WHITE + file.read())
            print_footer()
        elif os.path.isdir(item_path):
            if print_all:
                print_directory(item_path)
                print_file_contents(item_path, print_all=True)
            else:
                print(f"{Fore.MAGENTA}DIRECTORY: {item}/")

if __name__ == "__main__":
    print_all = False
    # Check if 'all' argument is provided
    if len(sys.argv) > 1 and sys.argv[1] == "all":
        print_all = True
    elif len(sys.argv) > 1:
        print(f"{Fore.RED}Error: Invalid argument '{sys.argv[1]}'. Only 'all' is accepted.")
        sys.exit(1)
    print_file_contents(print_all=print_all)

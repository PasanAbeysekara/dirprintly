import os

def print_header(file_path):
    header = f"\n\n{'=' * 80}\n== FILE: {file_path}\n{'=' * 80}\n"
    print(header)

def print_footer():
    footer = f"\n{'-' * 80}\nEnd of file\n{'-' * 80}\n\n"
    print(footer)

def print_file_contents(directory=None):
    if directory is None:
        directory = os.getcwd()

    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isfile(item_path):
            print_header(item_path)
            with open(item_path, 'r', encoding='utf-8', errors='ignore') as file:
                print(file.read())
            print_footer()
        elif os.path.isdir(item_path):
            print(f"Entering directory: {item_path}\n")
            print_file_contents(item_path)

if __name__ == "__main__":
    print_file_contents()

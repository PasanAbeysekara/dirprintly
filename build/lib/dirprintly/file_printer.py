import os

def print_file_contents(directory=None):
    if directory is None:
        directory = os.getcwd()
    
    # Loop through each item in the directory
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        # Check if the item is a file and print its contents
        if os.path.isfile(item_path):
            print(f"--- Contents of {item_path} ---")
            with open(item_path, 'r', encoding='utf-8', errors='ignore') as file:
                print(file.read())
                print("--------------------------------\n")
        # If the item is a directory, recursively call this function
        elif os.path.isdir(item_path):
            print(f"Entering directory: {item_path}\n")
            print_file_contents(item_path)

# This will start the process from the current working directory
if __name__ == "__main__":
    print_file_contents()

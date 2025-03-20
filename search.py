import os

def search_localhost(root_dir):
    # Walk through all files in the directory
    for dirpath, _, filenames in os.walk(root_dir):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            try:
                # Open each file and search for the keyword "localhost"
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line_number, line in enumerate(file, 1):
                        if "localhost" in line:
                            print(f"Found 'localhost' in file: {file_path}, line {line_number}")
            except (UnicodeDecodeError, PermissionError):
                # Skip files that can't be opened or read
                continue

if __name__ == "__main__":
    root_dir = input("Enter the root directory where the project is located: ")
    search_localhost(root_dir)

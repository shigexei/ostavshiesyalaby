'''import os

def list_directories_and_files(path):
    print("Directories:")
    for dir_entry in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir_entry)):
            print(dir_entry)

    print("\nFiles:")
    for file_entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_entry)):
            print(file_entry)

def list_all_directories_and_files(path):
    for root, dirs, files in os.walk(path):
        print(f"\nDirectories in {root}:")
        for dir_entry in dirs:
            print(os.path.join(root, dir_entry))

        print("\nFiles:")
        for file_entry in files:
            print(os.path.join(root, file_entry))

if __name__ == "__main__":
    path = input("Enter the path: ")

    print("\nListing Directories and Files:")
    list_directories_and_files(path)

    print("\nListing All Directories and Files:")
    list_all_directories_and_files(path)
'''
'''
def check_path_access(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return

    print(f"Path '{path}' exists.")

    if os.access(path, os.R_OK):
        print("Readable: Yes")
    else:
        print("Readable: No")

    if os.access(path, os.W_OK):
        print("Writable: Yes")
    else:
        print("Writable: No")

    if os.access(path, os.X_OK):
        print("Executable: Yes")
    else:
        print("Executable: No")

if __name__ == "__main__":
    path = input("Enter the path to check: ")
    check_path_access(path)
'''

'''import os

def test_path(path):
    if os.path.exists(path):
        print("Path exists.")

        directory, filename = os.path.split(path)
        print(f"Directory: {directory}")
        print(f"Filename: {filename}")
    else:
        print("Path does not exist.")

if __name__ == "__main__":
    path = input("Enter the path to test: ")
    test_path(path)
'''

'''
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
            print(f"Number of lines in '{file_path}': {line_count}")
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

if __name__ == "__main__":
    file_path = input("Enter the path of the text file: ")
    count_lines(file_path)
'''

'''
def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print(f"List has been written to '{file_path}' successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]  
    file_path = input("Enter the file path to write the list to: ")
    write_list_to_file(file_path, data)
'''
'''
import string

def generate_text_files():
    alphabet = string.ascii_uppercase 

    for letter in alphabet:
        file_name = letter + ".txt"
        with open(file_name, 'w') as file:
            file.write(f"This is file {file_name}\n")
        print(f"File '{file_name}' created successfully.")

if __name__ == "__main__":
    generate_text_files()
'''

'''
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print(f"Contents of '{source_file}' copied to '{destination_file}' successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    source_file = input("Enter the path of the source file: ")
    destination_file = input("Enter the path of the destination file: ")
    copy_file(source_file, destination_file)

'''

'''
import os

def delete_file(path):
    try:
        # Check if the path exists
        if not os.path.exists(path):
            print(f"The path '{path}' does not exist.")
            return

        # Check for access
        if not os.access(path, os.W_OK):
            print(f"You don't have write access to '{path}'.")
            return

        # Delete the file
        os.remove(path)
        print(f"File '{path}' deleted successfully.")
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path of the file to delete: ")
    delete_file(file_path)
'''

import os

def read_file(filename):
    with open(filename, 'r') as file:
        data = file.read()
    return data

def main():
    filename = input("Enter filename: ")
    file_contents = read_file(filename)
    print("File contents:", file_contents)

if __name__ == "__main__":
    main()
import os

path = input("Enter the directory path: ")

if os.path.isdir(path):
    contents = os.listdir(path)
    print(f"Contents of {path}:")
    for item in contents:
        print(item)
else:
    print("The path is not a valid directory.")
    # directory path=C:\Users\HP\OneDrive\Documents
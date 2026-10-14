import os
# Using the input function
path = input("Enter the directory path: ")

# using If else condition to check if the path is a valid directory or not

if os.path.isdir(path):
    contents = os.listdir(path)
    print(f"Contents of {path}:")
    for item in contents:
        print(item)
else:
    print("The path is not a valid directory.")
    # this program will check if the path is a valid directory or not and if it is valid it will print the contents of the directory otherwise it will print that the path is not a valid directory.
    # this program is just to practice comments.
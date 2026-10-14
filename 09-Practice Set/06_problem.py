with open("log.txt") as f:
    c = f.read()

if ("python" in c):
    print("yes,python is present in file.")
else:
    print("no,python is not present in file.")

with open("notcopy.txt") as f:
    content1 = f.read()
with open("yes_copy.txt") as f:
    content2 = f.read()
if content1 == content2:
    print("yes these two files are identical")
else:
    print("no these two files are not identical")

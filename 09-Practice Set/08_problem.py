with open("notcopy.txt") as f:
    content = f.read()
with open("yes_copy.txt","w") as f:
    f.write(content)
with open("poem.txt") as f:
    c = f.read()
    if ("twinkle" in c):
        print("twinke is present in the content.")
    else:
        print("twinke is not present in the content.")
            
    
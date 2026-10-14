n = int(input("enter a number: "))
l = [n*i for i in range(1,11)]
with open("tables.txt","a") as f:
    f.write(f"the table of {n}: {str(l)}\n")
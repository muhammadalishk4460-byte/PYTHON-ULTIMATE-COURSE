p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

comment = input("enter a comment: ")
if (p1 in comment) or (p2 in comment) or (p3 in comment) or (p4 in comment):
    print("it's a spam comment")
else:
    print("it is not a spam comment")
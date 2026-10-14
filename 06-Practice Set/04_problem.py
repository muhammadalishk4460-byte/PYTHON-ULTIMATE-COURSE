username = input("enter user-name: ")

if(len(username)<10):
    print("The username contains less than 10 characters.")
elif(len(username)==10):
    print("the username contains 10 characters.")
else:
    print("the username contains more than 10 characters.")
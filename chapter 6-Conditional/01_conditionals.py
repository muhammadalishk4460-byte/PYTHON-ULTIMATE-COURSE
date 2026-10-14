a = int(input("enter youe age: "))
    #if elif else ladder
if(a>=18):
    print("you are above the age of consent")
elif(a<0):
    print("you are entering an invalid age")
elif(a==0):
    print("you are entering 0 age which is not valid")
else:
    print("you are below the age of consent")
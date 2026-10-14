a = int(input("enter youe age: "))
    # if statement no:1

if(a%2==0):
    print("age is even")
else:
    print("age is odd")
#the end of if statement no:1
    #if statement no 2:
if(a>=18):
    print("you are above the age of consent")
elif(a<0):
    print("you are entering an invalid age")
elif(a==0):
    print("you are entering 0 age which is not valid")
else:
    print("you are below the age of consent")
#the end of if statement no2:

print("end of the program")
print("thank you!")
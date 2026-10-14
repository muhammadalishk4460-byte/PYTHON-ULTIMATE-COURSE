a1 = int(input("enter number 1: "))
a2 = int(input("enter number 2: "))
a3 = int(input("enter number 3: "))
a4 = int(input("enter number 4: "))
if(a1>a2 and a1>a3 and a1>a4):
    print("the gratest number is: ",a1)
elif(a2>a1 and a2>a3 and a2>a4):
    print("the gratest number is: ",a2)
if(a3>a2 and a3>a1 and a3>a4):
    print("the gratest number is: ",a3)
else:
    print("the gratest number is: ",a4)
print("Thank you!")
# we can also use omly elif
# even the elif is not used
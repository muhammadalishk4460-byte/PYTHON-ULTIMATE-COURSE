def avg():
    a = int(input("enter number 1: "))
    b = int(input("enter number 2: "))
    c = int(input("enter number 3: "))
    average = (a + b+ c)/3
    return average
#return statement is used to send the value back to the caller

a = avg()
print(a)
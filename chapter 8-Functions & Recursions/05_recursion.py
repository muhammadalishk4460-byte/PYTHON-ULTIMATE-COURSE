def factorial(n):
    if(n==1 or n==0):   #base case
        return 1
    return n* factorial(n-1)    #recursive call
n = int(input("enter the number: "))
print(f"the factorial of the number is: {factorial(n)}")
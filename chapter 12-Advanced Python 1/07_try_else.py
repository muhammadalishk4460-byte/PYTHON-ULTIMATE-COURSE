try:
    a = int(input("enter a number: "))
    print(a)
except Exception as e:
    print(e)
else:
    print("i am in else block")
#the else block runs when try runs otherwise i will not run
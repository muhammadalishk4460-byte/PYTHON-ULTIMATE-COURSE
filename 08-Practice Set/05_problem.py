def inch_to_cm(inch):
    return inch*2.45
n = int(input("enter the number: "))
c = inch_to_cm(n)
print(f"the corresponding value in cms is: {round(c,2)}")
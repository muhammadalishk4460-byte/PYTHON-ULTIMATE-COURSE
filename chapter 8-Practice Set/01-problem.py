def greatest():
    numbers = [
        int(input("enter number 1: ")),
        int(input("enter number 2: ")),
        int(input("enter number 3: "))
    ]
    return max(numbers)
print(greatest())
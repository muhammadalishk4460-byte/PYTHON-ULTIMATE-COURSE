def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
i = int(input("enter the number: "))
c = sum(i)
print(f"the sum of first {i} numbers is: {c}")
    
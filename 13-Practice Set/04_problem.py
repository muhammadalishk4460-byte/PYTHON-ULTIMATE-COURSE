def divisible5(n):
    if(n%5==0):
        return True
    return False
a = [5,23,10,1555,45,2435,44]
f = (list(filter(divisible5,a)))
print(f)
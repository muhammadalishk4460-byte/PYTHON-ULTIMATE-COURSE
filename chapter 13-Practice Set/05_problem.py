from functools import reduce
a = [5,23,10,1555,45,2435,44]
def greater(a,b):
    if(a>b):
        return a
    return b
print(reduce(greater,a))

class employee:
    def __init__(self):
        print("constructor of employee class")
    a = 1
class programmer(employee):
    def __init__(self):
          print("constructor of programmer class")
    b = 2
class manager(programmer, employee):
    def __init__(self):
            super().__init__()
            print("constructor of manager class")
    c = 3
# o = employee()
# print(o.a)  # print the a attribute
# o = programmer()
# print(o.a,o.b)  # print the a and b attribute
o = manager()
print(o.a,o.b,o.c)  # print the a, b and c attribute
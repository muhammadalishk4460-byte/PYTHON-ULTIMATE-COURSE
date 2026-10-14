class employee:
    a = 1
class programmer(employee):
    b = 2
class manager(programmer):
    c = 3
o = employee()
print(o.a)  # print the a attribute
o = programmer()
print(o.a,o.b)  # print the a and b attribute
o = manager()
print(o.a,o.b,o.c)  # print the a, b and c attribute
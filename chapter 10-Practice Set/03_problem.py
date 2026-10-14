class demo:
    a = 4
o = demo()  #print the class attribute because instance attribute is not given
print(o.a)
o.a = 0  #modify the instance attribute#instance attribute is set
print(o.a)  #prints the instance attribute because it is present
print(demo.a)   #prints the class attribute
class programmers:
    company = "microsoft"

    def __init__(self,name,age,salary,pin):
        self.name = name
        self.age = age
        self.salary = salary
        self.pin = pin

a = programmers("ali",18,10000000,1234)
b = programmers("ahmed",20,20000000,5678)
print(a.name,a.age,a.salary,a.pin,a.company,end = "\n")
print(b.name,b.age,b.salary,b.pin,b.company,end = "\n")
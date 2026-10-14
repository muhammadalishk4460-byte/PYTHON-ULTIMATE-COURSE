class employee:
    language = "python"  #this is a class attribute
    salary = 100000

    def __init__(self,name,language,salary):
        self.name = name
        self.language = language
        self.salary = salary
        print("hello i am a constructor")

    def getinfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}")
    @staticmethod
    def greet():
        print("assalamualaikum")
harry = employee("ali","java",13000000000)
print(harry.name,harry.language,harry.salary)
harry.getinfo()
harry.greet()

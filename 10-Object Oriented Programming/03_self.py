class employee:
    language = "python"  #this is a class attribute
    salary = 100000

    def getinfo(self):
        print(f"the language is {self.language} and the salary is {self.salary}")
    @staticmethod
    def greet():
        print("assalamualaikum")
harry = employee()
harry.salary = 10000000
harry.getinfo()
harry.greet()

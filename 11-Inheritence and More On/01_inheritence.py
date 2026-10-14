class employee():
    company = "google"
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is self.salary")

class programmer(employee):
    company = "youtube"
    def showlanguage(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")
a = employee()
b = programmer()
print(a.company,b.company)
class employee:
    company = "google"
    name = "unknown"
    def show(self):
        print(f"the name of the employee is {self.name} and the company is {self.company}")

class coder:
    language = "python"
    def showlanguage(self):
        print(f"the language of the coder is {self.language}")
class programmer(employee, coder):
    company = "youtube"
    name = "known"
    def shown(self):
        print(f"the name of the employee is {self.name} and the company is {self.company}")
a = employee()
b = programmer()

b.show()
b.showlanguage()
b.shown()
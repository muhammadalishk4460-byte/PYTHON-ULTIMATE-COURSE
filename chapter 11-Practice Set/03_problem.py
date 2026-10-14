class employee:
    def __init__(self,salary,increment):
        self.salary = salary
        self.increment = increment

    @property
    def salary_after_increment(self):
            return self.salary+(self.salary*self.increment/100)
    @salary_after_increment.setter
    def salary_after_increment(self,new_salary):
            self.increment = ((new_salary-self.salary)/self.salary)*100

emp = employee(30000,10)
print(f"the salary of the employee after increment is: {emp.salary_after_increment}")

emp.salary_after_increment = 33000
print(f"the increment added to the employees salary is: {emp.increment}")
        
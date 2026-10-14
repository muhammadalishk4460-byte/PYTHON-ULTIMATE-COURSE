class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"the class atribute of a is: {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]
e = employee()
e.a = 34
e.name = "ali hamza"
print(e.fname)
e.show()
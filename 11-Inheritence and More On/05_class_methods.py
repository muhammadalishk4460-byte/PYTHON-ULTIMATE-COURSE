class employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"the class atribute of a is: {cls.a}")
p = employee()
p.a = 34
p.show()
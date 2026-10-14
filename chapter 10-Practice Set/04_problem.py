class calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"the square is:  {self.n**2}")

    def cube(self):
        print(f"the cube is: {self.n**3}")

    def squareroot(self):
        print(f"the square root is: {self.n**0.5}")
    @staticmethod
    def greet():
        print("assalam o alikum")
n = int(input("enter a number: "))
calc = calculator(n)
calc.square()
calc.cube()
calc.squareroot()
calc.greet()
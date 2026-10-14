class complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i
    def __add__(self,c2):
        return complex(self.r + c2.r,self.i + c2.i)
    def __str__(self):
        return f"{self.r} + {self.r}i"
    def __mul__(self, c2):
        real = self.r * c2.r - self.i * c2.i
        imaginary = self.r * c2.i + self.i * c2.r
        return complex(real, imaginary)
    def __str__(self):
        return f"{self.r} + {self.i}i"
a = complex(1,3)
b = complex(2,4)
print(f"the addition of these two vectors: {a+b}")
print(f"the multiplication of two vectors becomes: {a*b}")
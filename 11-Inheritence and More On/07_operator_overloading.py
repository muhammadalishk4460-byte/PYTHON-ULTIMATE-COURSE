class student:
    def __init__(self,marks):
        self.marks = marks
    def __add__(self,other):
        return self.marks + other.marks
s1 = student(25)
s2 = student(32)
print(s1+s2)
'''
__add__      # +
__sub__      # -
__mul__      # *
__truediv__  # /
__eq__       # ==
__lt__       # <
__str__      # str() / print()
'''
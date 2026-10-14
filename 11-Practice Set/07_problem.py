class vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self,other):
        result = vector(self.x + other.x, self.y +other.y , self.z + other.z)
        return result
    def __mul__(self,other):
        result = self.x*other.x + self.y*other.y + self.z*other.z 
        return result
    def __str__(self):
        return f"vector({self.x},{self.y},{self.z})"
    def __len__(self):
        return 3
v1 = vector(1,4,6)
v2 = vector(2,5,7)
v3 = vector(3,9,1)
print(v1 + v3)
print(v1 * v2)
print(v2*v3)
print(len(v1))
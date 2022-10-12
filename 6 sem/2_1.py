class Vector():
    

    def __init__(self, x = 0, y = 0, z = 0):
        self.x = x
        self.y = y
        self.z = z
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __str__(self):
        return (f"({self.x}, {self.y}, {self.z})")
    
    def __sub__(self, other):
        return Vector((self.x - other.x),(other.y - self.y))

    def __mul__(self, other):
        return Vector((self.y * other.z - self.z * other.y),(self.x * other.z - self.z * other.x),(self.x* other.y - self.y * other.x))

    @classmethod
    def constructor(cls, a_text):
        return cls(*a_text.split(','))

A = Vector("1, 2, 1")
B = Vector("3, 4, 1")
C = A + B
print(C)
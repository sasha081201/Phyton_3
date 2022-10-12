import math


class Complex:
    def __init__(self, real, imag):
        self.x = real
        self.y = imag
        ###z = str(real + "i"+ imag)

    def __add__(self, other):
        return Complex((self.x + other.x),(other.y + self.y))

    def __str__(self):
        return (f"{self.x} + {self.y}i")
    
    def __sub__(self, other):
        return Complex((self.x - other.x),(other.y - self.y))

    def __mul__(self, other):
        return Complex((self.x * other.x - self.y * other.y),(self.y * other.x - self.x * other.y))

    def __abs__(self):
        return math.sqrt((self.x)**2 + (self.y)**2)
    

a = Complex(1, 1)
b = Complex(1, 2)
c = a + b
print(abs(a))
print(c)

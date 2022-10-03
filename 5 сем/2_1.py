
class Shape():
    
    def __init__(self, hight_, wight_):
        self.hight = hight_
        self.wight = wight_
    
    def get_hight(self):
        return self.hight
    
    def get_wight(self):
        return self.wight


class Triangle(Shape):
    def area(self):
        return 0.5 * self.hight * self.wight

class Rectangle(Shape):
    def area(self):
        return self.hight * self.wight


new_triangle = Triangle(2, 2)
new_rectangle = Rectangle(2, 2)
s1 = new_triangle.area()
s2 = new_rectangle.area()
print(s1)
print(s2)
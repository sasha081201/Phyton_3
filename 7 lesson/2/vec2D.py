import math

class Vec2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self, x):
        return x

    def get_y(self, y):
        return y
        
    def __str__(self):
        return f"Vector:Vec2d({self.x}, {self.y})"
# =======================================================================================
# Функции для работы с векторами
# =======================================================================================
    def _sub_(self, other):
    #возвращает разность двух векторов
        return Vec2d(self.x - other.x, self.y - other.y)


    def _add_(self, other):
    #возвращает сумму двух векторов
        return Vec2d(self.x + other.x, self.y + other.y)


    def _len_(self):
    #возвращает длину вектора
        return math.sqrt(pow(self.x) + pow(self.y))


    def _mul_(self, k):
    #возвращает произведение вектора на число
        return Vec2d(self.x * k, self.y * k)

    def _int_pair(self):
    #возвращает кортеж из двух чисел (текушие координаты вектора)
        return self.x, self.y
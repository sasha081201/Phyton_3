class Anymals():
    name = None
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def set_age(self):
        age = self._age
    def set_name(self):
        name = self._name
    def get_name(self):
        return self._name

    def get_age(self):
        return self._age
    def area(self):
        return ("averywere")
    

class Zebra(Anymals):
    def __init__(self, name, age):
        super().__init__(name, age)
        
        self.class_of_animal = "mammal"

    def class_of_animal(self):
        return self.class_of_animal
    
class Dolphin(Anymals):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.class_of_animal = "mammal"
    def area(self):
        return ("water")


d = Dolphin("g", 12)
print(d.area())
print(d.class_of_animal)
z = Zebra("ghy", 5)
print(z.get_age())
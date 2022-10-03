class Mother():
    surname = None
    def __init__(self, name, surname, age):
        self._name = name
        self._age = age
        self._surname = surname
    

    def get_name(self):
        return self._name
    
    def get_surname(self):
        return self._surname

    def get_age(self):
        return self._age
    

class Daughter(Mother):
    def __init__(self, name, surname, age):
        super().__init__(name, surname, age)
        self._age =self._age - 20

mother = Mother("A", "gggg", 50)
daughter = Daughter("F", "gggg", 50)
print (mother.get_age())
print(daughter.get_age())
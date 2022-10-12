class Student:
    def __init__(self, _name, _surname, _studak):
        self.name =_name
        self.surname = _surname
        self.studak = _studak
    
    def __eq__(self, other):
        if self.studak == other.studak:
            return True
    def __hash__(self):
        return hash(self.studak)
    def __str__(self):
        return (f"{self.name}, {self.surname} - {self.studak}")
    def __repr__(self):
        return self.name
p = Student("Петя", "ngjh", 2383488843288820)
v = Student("Вася","vnghjf", 4304893489043999)
k = Student("Коля", "vnfhfj", 2383488843288820)
print(v)
print(set([p, v, k]))
print(p==k)
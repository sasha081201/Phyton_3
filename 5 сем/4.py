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



class Mammals(Anymals):
    pass


class Burds(Anymals):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.wings = [Webbed() for _ in range(2)]

    def can_fly(self):
        if self.wings != 0:
            return True

    def have_wings(self):
        return True

class FlyerMixin():

    def can_fly(self):
        for i in range (len(self.wings)): 
            self.wings[i].movement()

class Insects(Anymals, FlyerMixin):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.q = int(input())
        self.wings = [Wings() for _ in range(self.q)]
    

class Cheiromtera(Anymals):
    pass

class Zebra(Mammals):
    def __init__(self, name, age):
        super().__init__(name, age)
        
    def Info(self):
        return self._name, self.set_age

    def can_sweam(self):
        return False


    
class Dolphin(Mammals):
    def __init__(self, name, age):
        super().__init__(name, age)

    def area(self):
        return ("water")
    def can_sweam(self):
        return True


class Wings:
     def movement(self):
        print("Flap")


class Webbed(Wings):
    def _init_(self):
        self.amount = 2
   


class Feather(Wings):
    pass



class Bats(Cheiromtera):
    
    def can_fly(self):
        return True
    
    def can_sweam(self):
        return False
    
    def have_wings(self):
        return super().have_wings()



d = Insects("g", 12)
d.fly()
###z = Zebra("ghy", 5)
###print(z.can_sweam())
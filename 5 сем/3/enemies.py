# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list

class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

    def question(self):
        pass

class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'
    
    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon():
     def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'черный'

     def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest
#FIXME здесь также должны быть описаны классы RedDragon и BlackDragon
# красный дракон учит вычитанию, а чёрный -- умножению.

class Troll(Enemy):
    def __init__(self):
        self._health = 100
        self._attack = 20
        self._color = None
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

class first_Troll(Troll):
     def __init__(self):
        super().__init__(self)
        self._color = 'pink'
     def question(self):
         x = randint(2,100)
         self.__quest = "угадай число от 1 до 5"
         self.set_answer(x)
         return self.__quest
class second_Troll(Troll):
    def __init__(self):
        super().__init__(self)
        self._color = 'green'
    
    def is_prime_number(a):
        for i in range(2, int(a ** 0.5) + 1):
            if a % i == 0:
                return False
            return True

    def question(self):
         x = randint(2,100)
         self.__quest = "угадай, простое ли число"
         self.set_answer(self.is_prime_number(x))
         return self.__quest

class Third_Troll(Troll):
    def __init__(self):
            super().__init__(self)
            self._color = 'green'
        
    def div(a):
        d = []
        for i in range(1, a // 2):
            if a % i == 0:
                d.append(i)
            return d.sort()

    def question(self):
        x = randint(2,100)
        self.__quest = "Разложит число на множители"
        self.set_answer(self.div(x))
        return self.__quest
enemy_types = [GreenDragon, RedDragon, BlackDragon, first_Troll, second_Troll, Third_Troll]

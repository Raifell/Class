from datetime import date


class Person:
    def __init__(self, age, name):
        self.age = age
        self.name = name

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)

    @staticmethod
    def isAdult(age):
        return age > 18


pers1 = Person('name-1', 21)
pers2 = Person.fromBirthYear('name-2', 1996)

# print(pers1.age)
# print(pers2.age)
#
# print(Person.isAdult(22))


class Man:
    ins_count = 0

    def __init__(self, name):
        self.name = name
        Man.ins_count += 1

    @staticmethod
    def counter():
        return Man.ins_count


a = Man('a')
b = Man('aa')
# c = Man('aaa')

# print(Man.counter())


class Point:
    ins_count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.get = self.get_ins(self.ins_count)

        Point.ins_count += 1

    def __str__(self):
        return 'Point-2D ({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Point(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            self.x += other
            self.y += other
            return self
        else:
            raise TypeError("Can't add {1} to {0}".format(self.__class__, type(other)))

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Point(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            self.x -= other
            self.y -= other
            return self
        else:
            raise TypeError("Can't add {1} to {0}".format(self.__class__, type(other)))

    @staticmethod
    def get_ins(ins):
        return ins


aes = Point(1, 2)
sea = Point(2, 3)
eas = Point(1, 2)

cu = aes + sea - eas

print(cu)
print(cu.get)
print(type(None))

i = 0
while i < 10:
    print(i < 10)
    i += 1

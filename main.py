class Main:
    def __str__(self):
        return 'Hello World!'


a = Main()
print(a)


class Example:
    def __init__(self, num):
        self.num = num
        self.string = self.find(num)

    def __str__(self):
        return self.string

    @staticmethod
    def find(num):
        return 'More than 10' if num > 10 else 'Low than 10'


ex = Example(9)
print(ex)
# print(Example.find(9))


class Font:
    @staticmethod
    def rectangle(x, y):
        d = 3.14 * x ** 2/4
        b = 3.14 * x * y
        return round(d*2 + b, 2)

    def __init__(self, di, hi):
        self.di = di
        self.hi = hi
        self.area = self.rectangle(di, hi)


a = Font(1, 2)
print(a.area)

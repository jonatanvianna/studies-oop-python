import math, random

class Circle():
    '''Construtor que recebe um valor para o radius'''
    def __init__(self, radius):
        if radius == 0:
            self.radius = random.uniform(1.1,9.5)
        else:
            self.radius = radius

    def caclCircunference(self):
        return math.pi * 2 * self.radius

    def calcDiameter(self):
        return self.radius * 2

    def calcArea(self):
        return math.pi * (self.radius ** 2) # ** is square

circles = []
for i in range(0,10):
    c = Circle(5.5)
    circles.append(c)

for c in circles:
    print("Radius:", c.radius,\
            "circumference", c.caclCircunference(), \
            "Diameter:", c.calcDiameter(), \
            "Area:", c.calcArea())

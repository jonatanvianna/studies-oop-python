from __future__ import print_function
import math

def caclCircunference(radius):
    return math.pi * 2 * radius

class Circle():
    pass

# Criação de um objeto concreto
circle1 = Circle()

# atribuindo um valor diretamente a este obejto específco
circle1.radius = 4.2 #long o float?

print(circle1.radius)

circle2 = Circle()
# aqui não tem radius, pois radius não é um campo da classe
circle2.radius = 3.9

print(circle2.radius)

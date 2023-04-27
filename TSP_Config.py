import math

# coordinates class
import random


class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def distanceTo(self, secondPoint):
        distance = (((self.x - secondPoint.x) ** 2 + (self.y - secondPoint.y) ** 2)) ** 0.5
        return distance

    def print(self):
        print(str(self.id)+" X: "+str(self.x)+" Y: "+str(self.y));

# coordinates class
class Path:

    fitnessRate = 10000

    def __init__(self, points, startPoint):
        self.id = random.randint(0,100)
        self.points = points    #without first and last city
        self.startPoint = startPoint

    def print(self):
        print(self.startPoint.id, end=" ")
        for point in self.points:
            print(point.id, end=" ")
        print(self.startPoint.id, end="\n ")

    def length(self):
        length = 0
        size = len(self.points)
        for i in range(size-1):
            length += self.points[i].distanceTo(self.points[i+1])
        length += self.points[size-1].distanceTo(self.startPoint)
        length += self.points[0].distanceTo(self.startPoint)
        return length

    def fitness(self):
        return self.fitnessRate/self.length()

# printing function
def printPath(path):
    for city in path:
        print(str(city.id) + " ", end="")

def importDataFrom(file):
    # opening file
    plik = open(file, "r")
    amount = int(plik.readline().strip())

    # creating points in cities array
    cities = []
    for linia in plik:
        data = linia.split()
        city = Point(int(data[0]), float(data[1]), float(data[2]))
        cities.append(city)

    return [cities, amount]
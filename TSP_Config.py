import math

# coordinates class
class Point:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y

    def distanceTo(self, secondPoint):
        distance = ((self.x - secondPoint.x) ** 2 + (self.y - secondPoint.y) ** 2) ** 0.5
        return distance

# printing function
def printPath(path):
    for city in path:
        print(str(city.id) + " ", end="")

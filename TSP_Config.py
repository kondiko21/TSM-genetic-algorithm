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

def importDataFrom(file):
    # opening file
    plik = open(file, "r")
    amount = int(plik.readline().strip())

    # creating points in cities array
    cities = []
    for linia in plik:
        data = linia.split()
        city = Point(int(data[0]), int(data[1]), int(data[2]))
        cities.append(city)

    return [cities, amount]
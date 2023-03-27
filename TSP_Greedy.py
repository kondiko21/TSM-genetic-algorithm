import random
import TSP_Config as tsp

# opening file
plik = open("instancja.txt", "r")
amount = int(plik.readline().strip())

# creating points in cities array
cities = []
for linia in plik:
    data = linia.split()
    city = tsp.Point(int(data[0]), int(data[1]), int(data[2]))
    cities.append(city)

# greedy algorithm
unvisited = cities
visited = []
distance = 0
current = cities[random.randint(0, amount)]
visited.append(current)
unvisited.remove(current)


for _ in range(amount-1):
    printPath(unvisited)
    minValue = current.distanceTo(random.choice(unvisited))
    for city in unvisited:
        currentDistance = current.distanceTo(city)
        if currentDistance <= minValue:
            minValue = currentDistance
            minCity = city
    distance += minValue
    visited.append(minCity)
    unvisited.remove(minCity)
    current = minCity

visited.append(visited[0])
distance += current.distanceTo(visited[0])

printPath(visited)
print("\nDistance is: " + str(distance))


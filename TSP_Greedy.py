import random
import TSP_Config as tsp

imp = tsp.importDataFrom("import.txt")
cities = imp[0]
amount = imp[1]

# greedy algorithm
unvisited = cities
visited = []
distance = 0
current = cities[random.randint(0, amount)]
visited.append(current)
unvisited.remove(current)


for _ in range(amount-1):
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

tsp.printPath(visited)
print("\nDistance is: " + str(distance))


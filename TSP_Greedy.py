import random
import TSP_Config as tsp

def greedyAlgorithm(file):
    imp = tsp.importDataFrom(file+".txt")
    cities = imp[0]
    amount = imp[1]

    # greedy algorithm
    unvisited = cities
    visited = []
    distance = 0
    current = cities[0]
    visited.append(current)
    unvisited.remove(current)
    results = open("results.txt", "a")

    for _ in range(amount-1):
        minValue = current.distanceTo(unvisited[0])
        minCity = unvisited[0]
        for city in unvisited:
            currentDistance = current.distanceTo(city)
            if currentDistance < minValue:
                minValue = currentDistance
                minCity = city
        distance += minValue
        # print(minValue)
        visited.append(minCity)
        unvisited.remove(minCity)
        current = minCity

    visited.append(visited[0])
    distance += current.distanceTo(visited[0])

    print("Path: ", end="")
    tsp.printPath(visited)
    print("\nDistance is: " + str(distance))
    results.write(file + " "+str(distance)+"\n")


import TSP_Config as tsp
import numpy as np

file = 'import'


#CONFIGURATION PARAMETERS:
populationSize = 10                 #Size of population

#USED VARIABLES:
citiesList = []
citiesAmount = 0
population = []
populationFitness = []

#TEMPORAIRLY:
imp = tsp.importDataFrom(file + ".txt")
citiesList = imp[0]
citiesAmount = imp[1]

def printPopulation():
    for i in range(populationSize):
        print('P'+str(i+1), end=' ')
        for j in range(citiesAmount+1):
            print(population[i][j].id, end=" ")
        print("")

def generatePopulation():
    pop = []
    for _ in range(populationSize):
        path = list(np.random.permutation(citiesList))
        path.append(path[0])
        population.append(path)

def pathLength(path):
    length = 0
    for i in range(citiesAmount):
        length += path[i].distanceTo(path[i+1])
    return  length

def fittness():
    populationFitness.clear
    for path in population:
        populationFitness.append(pathLength(path))

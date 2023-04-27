import random

import TSP_Config as tsp
import numpy as np

#CONFIGURATION PARAMETERS:
populationSize = 45           #Size of population S
mutationRate = 0.35          #Probability of mutation M
crossoverRate = 0.9            #Probability of crossover C
stoppingPoint = 100000          #Iteration limit I

class GeneticAlgorithm:

    def __init__(self, file):
        self.file = file

    #USED VARIABLES:
    citiesList = []
    citiesAmount = 0
    population = []
    populationFitness = []
    offsets = []
    best = 0

    #TEMPORAIRLY:
    def importCities(self):
         imp = tsp.importDataFrom(self.file + ".txt")
         self.citiesList = imp[0]
         self.citiesAmount = imp[1]

    def printPopulation(self):
        for i in range(len(self.population)):
            print('P' + str(i + 1), end=' ')
            self.population[i].print()
            print(self.population[i].length())

    def generatePopulation(self):
        for i in range(populationSize):
            path = list(np.random.permutation(self.citiesList))
            startCity = path.pop(0)
            self.population.append(tsp.Path(path, startCity)) #create object Path type
            self.best = self.population[0].length()

    def fitness(self):
        self.populationFitness.clear()
        for path in self.population:
            self.populationFitness.append(path.fitness())

    def roulette(self, amount):
        self.fitness()
        suma = sum(self.populationFitness)
        selectedPopulation = []
        i = 0
        while i < amount:
            n = 0
            partSum = 0
            selection = self.population[0]
            rand = round(random.uniform(0, suma), 3)
            while partSum < rand and n <= populationSize-1:
                partSum += self.populationFitness[n]
                selection = self.population[n]
                n += 1
            if selection in selectedPopulation:
                i -= 1
            else:
                selectedPopulation.append(selection)
            i += 1

        return selectedPopulation

    def crossover(self):
        parents = self.roulette(2)
        self.offsets.clear()
        rand = random.random()
        if rand < crossoverRate:
            parentsCrossOver = []
            for parent in parents:
                p = []
                p.append(parent.startPoint)
                p = p + parent.points
                parentsCrossOver.append(p)

            crossPoints = random.sample(range(0, self.citiesAmount), 2)
            crossPoints.sort()
            print(crossPoints)
            cutOffs = []
            for i in range(2):
                cutOffs.append([])
                cutOffs[i].append(parentsCrossOver[i][0:crossPoints[0]])
                cutOffs[i].append(parentsCrossOver[i][crossPoints[0]:crossPoints[1]])
                cutOffs[i].append(parentsCrossOver[i][crossPoints[1]:len(parentsCrossOver[i])])
                cutOffs[i].append(cutOffs[i][0]+cutOffs[i][2])

            robocze = [[],[]]
            for p in parentsCrossOver[0]:
                if p in cutOffs[1][3]:
                    robocze[0].append(p)

            for p in parentsCrossOver[1]:
                if p in cutOffs[0][3]:
                    robocze[1].append(p)

            cutOffs[0][1], cutOffs[1][1] = cutOffs[1][1], cutOffs[0][1]

            for i in range(2):
                path = []
                path = path + robocze[i][0:crossPoints[0]]
                del robocze[i][0:crossPoints[0]]
                path = path + cutOffs[i][1]
                path = path + robocze[i]
                startPoint = path.pop(0)
                offset = tsp.Path(path, startPoint)
                self.offsets.append(offset)
        else:
            self.offsets = parents

    def mutation(self):
        for i in range(2):
            rand = random.random()
            if rand < mutationRate:
                mutationPoints = random.sample(range(0, self.citiesAmount-1), 2)
                self.offsets[i].points[mutationPoints[0]], self.offsets[i].points[mutationPoints[1]] = self.offsets[i].points[mutationPoints[1]], self.offsets[i].points[mutationPoints[0]]


    def run(self):
        self.importCities()
        self.generatePopulation()
        for i in range(stoppingPoint):
            self.crossover()
            self.mutation()
            self.population = self.population + self.offsets
            self.population.sort(key=lambda x: x.length(), reverse=False)
            self.population.pop(len(self.population)-1)
            self.population.pop(len(self.population)-1)
            # self.printPopulation()
            if self.population[0].length() < self.best:
                print('BEST: ', end=' ')
                print(self.population[0].length())
                self.best = self.population[0].length()




import random


import TSP_Config as tsp
import numpy as np

#CONFIGURATION PARAMETERS:
populationSize = 200           #Size of population S
mutationRate = 0.25         #Probability of mutation M
eliteSize = 30
stoppingPoint = 3000          #Iteration limit I

class GeneticAlgorithm:
    def __init__(self, file):
        self.file = file

    #USED VARIABLES:
    citiesList = []
    citiesAmount = 0
    population = []
    populationFitness = []
    best = 0
    suma = 0

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

        selectedPopulation = []
        i = 0
        while i < amount:
            n = 0
            partSum = 0
            selection = self.population[0]
            rand = round(random.uniform(0, self.suma), 3)
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

        offsets = []
        parents = self.roulette(2)
        parentsCrossOver = []
        for parent in parents:
            p = []
            p.append(parent.startPoint)
            p = p + parent.points
            parentsCrossOver.append(p)

        crossPoints = random.sample(range(0, self.citiesAmount), 2)
        crossPoints.sort()
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
            offsets.append(offset)
        return offsets


    def mutation(self, offsets):
        new = []
        for offset in offsets:
            o = []
            o.append(offset.startPoint)
            o = o + offset.points
            cp = random.sample(range(0, self.citiesAmount), 2)
            cp.sort()
            o[cp[0]:cp[1]] = reversed(o[cp[0]:cp[1]])
            startPoint = o.pop(0)
            new.append(tsp.Path(o, startPoint))
        return new

    # def mutation(self, offsets):
    #     for i in range(2):
    #         rand = random.random()
    #         if rand < mutationRate:
    #             mutationPoints = random.sample(range(0, self.citiesAmount), 2)
    #             if self.citiesAmount-1 not in mutationPoints:
    #                 offsets[i].points[mutationPoints[0]], offsets[i].points[mutationPoints[1]] = offsets[i].points[mutationPoints[1]], offsets[i].points[mutationPoints[0]]
    #             else:
    #                 mutationPoints.remove(self.citiesAmount-1)
    #                 offsets[i].points[mutationPoints[0]], offsets[i].startPoint = offsets[i].startPoint, offsets[i].points[mutationPoints[0]]
    #     return offsets

    def nextGeneration(self):
        newPopulation = []
        elite = self.population[:2*eliteSize]
        for i in range(int((populationSize)/2)-eliteSize):
            offset = self.crossover()
            mutatedOffset = self.mutation(offset)
            newPopulation = newPopulation + mutatedOffset
        return (newPopulation + elite)


    def run(self):
        last = 1
        self.importCities()
        self.generatePopulation()
        tsp.displayPath(self.population[0], "o")
        self.fitness()
        self.suma = sum(self.populationFitness)
        for i in range(stoppingPoint):
            self.population = self.nextGeneration();
            self.population.sort(key=lambda x: x.length(), reverse=False)
            self.fitness()
            self.suma = sum(self.populationFitness)
            # for p in self.population:
            #     print(p.length(), end=" ")
            # print("")
            if i in [stoppingPoint/3, (stoppingPoint/3)*2, stoppingPoint-1]:
                tsp.displayPath(self.population[0], "-")
            # if self.population[0].length() != self.best:
            #     self.best = self.population[0].length()
            #     print('BEST: ', end=' ')
            #     print(self.population[0].length())

            if i%10==0:
                print(i, end=': ')
                print(self.population[0].length())


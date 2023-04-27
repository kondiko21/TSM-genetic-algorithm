import math
import random
import instanceGenerator
import TSP_Greedy as greedy
import TSP_GA as ga


# instanceGenerator.preparareTestingSet("testset/set", 10)
# instanceGenerator.generateInstances("instancjam", 20, 40)
# instanceGenerator.generateInstances("instancja5000", 5000, 500)
# greedy.greedyAlgorithm("bier127")
# greedy.greedyAlgorithm("tsp250")
# greedy.greedyAlgorithm("XD/instancja2")
#
# ga.generatePopulation()
# ga.printPopulation()
# ga.fitness()
# ga.crossover()


tspSolver = ga.GeneticAlgorithm('tsp250')
tspSolver.run()
# tspSolver.importCities()
# tspSolver.generatePopulation()
# tspSolver.crossover()
# tspSolver.mutation()
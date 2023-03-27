import math
import random
import numpy as np

list = []

def preparareTestingSet(name, amount):
    counter = 0
    values = np.logspace(1, 3, 200, endpoint = True)
    for val in values:
        generateInstances(name+str(counter), round(val))
        print(round(val))


def generateInstances(toFile, size):
    list = []
    file = open(toFile+".txt\n", "w")
    file.write(str(size)+"\n")
    for i in range(size):
        # mapSize = round(math.log(size)*100)
        mapSize = 100
        X = random.randint(0, mapSize)
        Y = random.randint(0, mapSize)
        coords = (X,Y)
        if coords not in list:
            list.append(coords)
            file.write(str(i+1)+" "+str(X)+" "+str(Y)+"\n")

        # print(str(X)+" "+str(Y))




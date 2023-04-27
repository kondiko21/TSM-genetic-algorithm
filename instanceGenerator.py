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


def generateInstances(toFile, size, mapSize):
    list = []
    file = open(toFile+".txt", "w+")
    file.write(str(size)+"\n")
    i = 0
    while i < size:
        # mapSize = round(math.log(size)*100)
        X = random.randint(0, mapSize)
        Y = random.randint(0, mapSize)
        coords = (X,Y)
        if coords not in list:
            list.append(coords)
            file.write(str(i+1)+" "+str(X)+" "+str(Y)+"\n")
        else:
            i -= 1
        i += 1

        # print(str(X)+" "+str(Y))




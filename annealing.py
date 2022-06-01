import random
from copy import copy
import math

from graph import *

#Generate a start path on n vertices
def generateInitial(n):
    nodes = [i for i in range(n)]
    random.shuffle(nodes)
    return nodes

#Generate the successor of path on n vertices
def generateSuccessor(path, n):
    i = random.randint(0, n-1)
    j = i
    while i == j:
        j = random.randint(0, n-1)

    out = copy(path)

    temp = out[i]
    out[i] = out[j]
    out[j] = temp

    return out

#Choose a path from two candidate paths on a graph, given a temperature
def which(graph, temp, oldPath, newPath, report):
    h = graph.heuristic(oldPath)
    h2 = graph.heuristic(newPath)

    if h == graph.n-1:
        raise Exception()

    if report:
        print("h(p) = ", h, ", T = ", temp)

    if h2 >= h:
        return newPath
    
    prob = math.exp( (h2-h) / temp )

    if random.random() <= prob:
        return newPath

    return oldPath

#The cooling schedule for our graph
def coolingSchedule(temp):
    return temp * 0.9999

#Run simulated annealing
def anneal(graph, maxiters, startTemp):
    #Initialise n, starting candidate path and temperature
    n = graph.n
    currentState = generateInitial(n)
    temp = startTemp

    iterations = 0

    while True:
        #Randomly generate a successor
        newState = generateSuccessor(currentState, n)
        
        #Pick a new state

        try:
            currentState = which(graph, temp, currentState, newState, iterations % 500 == 0)
        except:
            return currentState

        #Cool down
        temp = coolingSchedule(temp)

        #Stop if running for too long and return the current candidate
        iterations += 1
        if iterations > maxiters:
            return currentState
        

if __name__ == "__main__":
    #Generate a digraph and insert some edges randomly
    g = MatrixGraph(100)
    for i in range(2500):
        g.connect(random.randint(0, 99), random.randint(0, 99))

    #Find number of edges and degree of a sample vertex
    print("|E| = ", g.countEdges())
    print("∃v : deg(v) = ", g.getDegree(random.randint(0, 99)), "\n")
    
    #Run simulated annealing
    path = anneal(g, 100000, 1)

    #Present the best path found
    print("\nPath:")
    print(path[0], end = '')
    for p in path[1:]:
        print(' ->', p, end = '')
    print('\n\nh(p) = ', g.heuristic(path))


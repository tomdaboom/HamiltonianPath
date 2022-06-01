from typing import List, Dict

#n vertices represented as numbers 0, 1, ..., n-1

#Object to represent graph as an adjacency matrix 
#O(1) adjacency testing
class MatrixGraph:
    #Constructor
    def __init__(self, n : int):
        #Declare adj matrix size and save |V|
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    #Connect two given vertices
    def connect(self, x : int, y : int):
        self.matrix[x][y] = 1
        #self.matrix[y][x] = 1

    #Test if two vertices are connected
    def connected(self, x : int, y : int) -> int:
        return self.matrix[x][y]

    #Compute the heuristic function of a given path
    def heuristic(self, path : List[int]) -> int:
        heuristic = 0
        for i in range(len(path)-1):
            heuristic += self.connected(path[i], path[i+1])
        return heuristic

    #Find |E|
    def countEdges(self) -> int:
        edges = 0
        for i in range(self.n):
            for j in range(self.n):
                edges += self.matrix[i][j]
        return edges


    def getDegree(self, i : int) -> int:
        deg = 0
        for j in range(self.n):
            deg += self.matrix[i][j]
        return deg

#Take a graph represented as an adjacency list 
#and turn into an AdjMatrix rep
def toMatrixGraph(adjlist : Dict[int, int]) -> MatrixGraph:
    out = MatrixGraph(len(adjlist.keys()))

    for u in adjlist.keys():
        for v in adjlist[u]:
            out.connect(u, v)

    return out

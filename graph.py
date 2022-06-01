import math

#n vertices represented as numbers 0, 1, ..., n-1

#Object to represent graph as an adjacency matrix 
#O(1) adjacency testing
class MatrixGraph:
    def __init__(self, n):
        self.matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.n = n

    def connect(self, x, y):
        self.matrix[x][y] = 1
        #self.matrix[y][x] = 1

    def connected(self, x, y):
        return self.matrix[x][y]

    def heuristic(self, path):
        heuristic = 0
        for i in range(len(path)-1):
            heuristic += self.connected(path[i], path[i+1])
        return heuristic

    def countEdges(self):
        edges = 0
        for i in range(self.n):
            for j in range(self.n):
                edges += self.matrix[i][j]
        return edges

    def getDegree(self, i):
        deg = 0
        for j in range(self.n):
            deg += self.matrix[i][j]
        return deg

#Take a graph represented as an adjacency list of type Dict<Integer, [Integer]> 
#and turn into an AdjMatrix rep
def toMatrixGraph(adjlist):
    out = MatrixGraph(len(adjlist.keys()))

    for u in adjlist.keys():
        for v in adjlist[u]:
            out.connect(u, v)

    return out

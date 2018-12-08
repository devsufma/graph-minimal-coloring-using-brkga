import numpy as np

class Graph:
    def __init__(self, numVert, numEdges):
        self.numVertices = numVert
        self.numEdges = numEdges
        self.numColors = numVert
        self.edges = [[0 for x in range(numVert)] for y in range(numVert)]
        self.colors = []


    def addEdge(self, v1, v2):
        if (v1 >= 0 and v2>=0):
            if (v1 != v2):
                self.edges[v1][v2] = 1

    def getEdge(self):
        return self.edges

    def getNumColors(self):
        return self.numColors

    def getColors(self):
        return self.colors

    def setColors(self, colors):
        self.colors = colors

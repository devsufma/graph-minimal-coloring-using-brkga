import numpy as np
import graph as gf

class GraphManager:
    def __init__(self, grafo, numVert, numEdges):
        self.grafo = gf.Graph(numVert, numEdges)

    def numColors(self):
        return self.grafo.numColors

    def numVertice(self):
        return self.grafo.numVertice

    def edges(self):
        return self.grafo.edges

for i in range(0,0):
    print("foi")

print("aa")

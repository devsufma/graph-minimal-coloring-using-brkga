import numpy as np
import graph as gf

class GraphManager:
    def __init__(self, grafo, numVert):
        self.grafo = gf.Graph(numVert)

    def numColors(self):
        return self.grafo.numColors

    def numVertice(self):
        return self.grafo.numVertice

    def edges(self):
        return self.grafo.edges

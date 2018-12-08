import numpy as np
import individuo as ind
from random import randint

class Population:
	def __init__(self, tamPopulacao, inicializar, numVert, numCor, gArestas):
		self.coloring = []
		self.tamPopulacao = tamPopulacao
		self.gArestas = gArestas

		if inicializar == True:
			for i in range(self.tamPopulacao):
				self.Individual = ind.Individuo(numVert, numCor)
				self.Individual.generateIndividual()
				self.Individual.correctGenome(self.gArestas)
				self.saveColoring(self.Individual)

	def saveColoring(self, individual):
		self.coloring.append(individual)

	def getColoring(self, index):
		return self.coloring[index]

	def getEliteFromFitness(self, taxaSobrevivencia):
		elite = []
		tempElite1 = self.getColoring(0)
		aux = 0
		for i in range(1, self.tamPopulacao):
			if tempElite1.getFitness() <= self.getColoring(i).getFitness():
				tempElite1 = self.getColoring(i)
				aux = i

		elite.append(tempElite1)
		taxa = int(taxaSobrevivencia*(self.tamPopulacao-1))
		for i in range(taxa):
			p = randint(0, (self.tamPopulacao-1))
			if p != aux:
				elite.append(self.getColoring(p))
		return elite

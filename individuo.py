from random import randint
from random import shuffle

class Individuo:
    def __init__(self, numVert, numColor):
        self.numVert = numVert
        self.chromosome = [-99999 for x in range(numVert)]
        self.maxColors = numColor
        self.fitness = 0
        self.colors = 0

    def setChromosome(self, cromossomo):
        self.chromosome = cromossomo

    def setColorChromosome(self, index, cor):
        self.chromosome[index] = cor
        self.fitness = 0
        self.colors = 0

    def generateIndividual(self):
        for i in range(self.numVert):
            self.setColorChromosome(i, randint(0, self.maxColors))
        chromosome = self.chromosome
        shuffle(chromosome)
        self.setChromosome(chromosome)

    def getColorChromosome(self, index):
        return self.chromosome[index]

    def getColors(self):
        tempColors = []
        length = len(self.chromosome)
        tempColors.append(self.getColorChromosome(0))
        for i in range(length):
            flag = True
            for j in range(len(tempColors)):
                if tempColors[j] == self.getColorChromosome(i):
                    flag = False
                    break
            if flag:
                tempColors.append(self.getColorChromosome(i))
        self.colors = len(tempColors)
        return self.colors

    def getFitness(self):
        if self.fitness == 0:
            self.fitness = self.getColors()
        return self.fitness

    def correctGenome(self, edges):
        for i in range(self.numVert):
            for j in range(self.numVert):
                if edges[i][j] == 1:
                    color1 = self.getColorChromosome(i)
                    color2 = self.getColorChromosome(j)

                    if color1 == color2:
                        greaterColor = color2
                        lowerColor = color2
                        for k in range(self.numVert):
                            if edges[j][k] == 1:
                                if greaterColor < self.getColorChromosome(k):
                                    tmp = greaterColor
                                    greaterColor = self.getColorChromosome(k)
                                    lowerColor = tmp

                        if lowerColor > 0:
                            color2 = lowerColor - 1
                            self.setColorChromosome(j, color2)
                        else:
                            color2 = greaterColor + 1
                            self.setColorChromosome(j, color2)

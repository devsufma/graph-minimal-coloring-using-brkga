from random import randint
import populacao as pp
class BRKGA:
    taxaCruzamento = 0.8
    taxaMutacao = 0.2
    taxaSobrevivencia = 0.4
    ELITISM = True
    elite = []
    n_VERT = 0

    def Evoluir(self, Populacao, tamPopulacao, numVert, numColor, edges):
        n_VERT = numVert
        n_COLOR = numColor
        novaPopulacao = pp.Population(tamPopulacao, True, numVert, numColor, edges)
        sobrevive = 0
        if (self.ELITISM):
            elite = novaPopulacao.getEliteFromFitness(self.taxaSobrevivencia)

            for i in range(len(elite)):
                novaPopulacao.coloring[i] = elite[i]
                sobrevive += 1

        for i in range(sobrevive, len(Populacao.coloring)):
            taxa = int(100*self.taxaCruzamento)
            if randint(0, 100) < taxa:
                positPai = randint(0, (len(elite)-1))
                ind1 = elite[positPai]
                ind2 = Populacao.getColoring(i)
                filho = self.crossover(ind1, ind2)

                novaPopulacao.saveColoring(filho)

        for i in range(sobrevive, novaPopulacao.tamPopulacao):
            taxa = int(100*self.taxaMutacao)
            if randint(0, 100) < taxa:
                self.mutacao(novaPopulacao.getColoring(i), n_COLOR)

        return novaPopulacao

    def mutacao(self, ind, n_COLOR):
        for i in range(len(ind.chromosome)):
            taxa = int(100*self.taxaMutacao)
            if randint(0, 100) < taxa:
                color = randint(0, n_COLOR-1)
                ind.setColorChromosome(i, color)

    def crossover(self, ind1, ind2):
        filho = ind1
        for i in range(len(ind1.chromosome)):
            if i%2 == 0:
                filho.setColorChromosome(i, ind2.chromosome[i])
        return filho

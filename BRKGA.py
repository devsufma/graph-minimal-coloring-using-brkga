import random
import populacao as pp
class BRKGA:
    taxaCruzamento = 0.7
    taxaMutacao = 0.21
    taxaSobrevivencia = 0.2
    ELITISM = True
    elite = []
    n_VERT = 0
    n_COLOR = 0
    tamPopulacao = 5

    def Evoluir(self, Poulacao, numVert, numColor, edges):
        n_VERT = numVert
        n_COLOR = numColor
        novaPopulacao = pp.Population(tamPopulacao, True, numVert, numColor, edges)
        sobrevive = 0
        if (ELITISM):
            elite = novaPopulacao.getEliteFromFitness(taxaSobrevivencia)

            for i in range(len(elite)):
                novaPopulacao.coloring[i] = elite[i]
                sobrevive += 1
        for i in range(sobrevive, novaPopulacao.tamPopulacao):
            taxa = int(100*taxaCruzamento)
            if randint(0, 100) < taxa:
                positPai = randint(0, len(elite))
                filho = self.crossover(elite[positPai], Populacao.getColoring(i))
                novaPopulacao.saveColoring(novaPopulacao)

        for i in range(sobrevive, novaPopulacao.tamPopulacao):
            taxa = int(100*taxaMutacao)
            if randint(0, 100) < taxa:
                self.mutacao(novaPopulacao.getColoring(i))

        return novaPopulacao

    def mutacao(ind):
        for i in range(len(ind.chromosome)):
            taxa = int(100*taxaMutacao)
            if randint(0, 100) < taxa:
                self.mutacao(novaPopulacao.getColoring(i))
                color = randint(0, n_COLOR)
                ind.setColorChromosome(i, color)

    def crossover(ind1, ind2):
        filho = ind1
        for i in range(len(ind1.chromosome)):
            if i%2 == 0:
                filho.setColorChromosome(i, ind2.chromosome[i])
x = BRKGA()
print(type(x))

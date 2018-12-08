import BRKGA
import graph as gr
import individuo as ind
import populacao as pp
import time

if __name__ == "__main__":

    tempoLimite = 0.5 #tempo em minutos
    tempo = time.time()
    grafo = gr.Graph(5)
    Populacao = pp.Population(10, True, grafo.numVert, grafo.numColor, grafo.edges)
    TAXA = BRKGA.BRKGA()
    print()
    geracoes = 0
    while (int(time.time()- tempo)/60) < tempoLimite:
        Populacao = TAXA.Evoluir(Populacao, Populacao.tamPopulacao, grafo.numVert, grafo.numColor, grafo.edges)
        geracoes += 1

    elite = Populacao.getEliteFromFitness(TAXA.taxaSobrevivencia)
    coresUsadas  = elite[0].colors
    print("Total de cores usadas => ", coresUsadas)
    print("Total de gerações -> ", geracoes)

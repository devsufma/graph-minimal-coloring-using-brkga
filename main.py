import BRKGA
import graph as gr
import individuo as ind
import populacao as pp
import time
import glob

if __name__ == "__main__":

    path = "C:/Documents"

    for file in glob.glob(path + '/*.txt'):

        fileg = open(file, 'r')
        first = 0

        tempoLimite = 0.5 #tempo em minutos
        tempo = time.time()

        for line in fileg:

            if first == 0:
                line1 = line.split(" ")
                tam = int(line1[2])
                first = 1
                grafo = gr.Graph(tam)
                #print("N de vertices: ", tam)
            else:
                lineE = line.split(" ")
                v1 = int(lineE[1]) - 1
                v2 = int(lineE[2]) - 1
                grafo.addEdge(v1, v2)
                #print("Vertice 1: " + v1 + " Vertice 2: " + v2
                
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

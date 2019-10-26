class Grafo(object):
    def __init__(self):
        self.vertices = list()
        self.vizinho = dict()


class Vertic(object):
    def __init__(self, cod):
        self.cod = cod
        self.vizinhos = list()


def dijkstra(grafo, inicial, final):
    controle = {}
    distAtual = {}
    noAtual = {}
    naoVisitados = []
    atual = inicial
    noAtual[atual] = 0

    for vertice in grafo.vertices:
        naoVisitados.append(vertice)
        distAtual[vertice] = float('inf')
    
    distAtual[atual] = 0
    naoVisitados.remove(atual)

    while naoVisitados:
        for vizinho, peso in grafo.vizinho:
            pesoTotal = peso + noAtual[atual]
            if distAtual[vizinho] == float('inf') or distAtual[vizinho] > pesoCalc:
                distAtual[vizinho] = pesoCalc
                controle[vizinho] = distAtual[vizinho]
        
        if controle == {} : break
        minVizinho = min(controle.items(), key = lambda x: x[1])
        atual = minVizinho[0]
        noAtual[atual] = minVizinho[1]
        naoVisitados.remove(atual)
        del controle[atual]

    print(distanciaAtual[fim][0])


if __name__ == '__main__':
    
from collections import defaultdict
from math import inf


class Aresta:
    def __init__(self, vertPart, vertDest, peso):
        self.vertPart = vertPart
        self.vertDest = vertDest
        self.peso = peso


class Vertice:
    def __init__(self, listAresta, name):
        self.name = name


    def addAresta(self, a):
        self.listAresta.append(a)


class Grafo:
    def __init__(self, listVertices, listaAresta):
        self.listVertices = listVertices
        self.listAresta = listAresta


    def addVertice(self, v):
        self.listVertices.append(v)

    def custoDireto(self, verticeP, verticeD):
        peso = float("inf")
        for v in self.listVertices:
            for a in self.listAresta:
                # print(a.vertPart)
                # print(verticeP.name)
                if a.vertPart == verticeP.name and a.vertDest == verticeD.name:
                    peso = a.peso
                    break
        return peso
    

    def prim(self):
        vertex = [self.listVertices[0]]
        listEdges = []
        pesoTotal = 0

        vLinha = self.listVertices
        vLinha.remove(self.listVertices[0])

        for i in range(len(vLinha)):
            custo_min = float("inf")
            va = None
            vb = None
            for v1 in vertex:
                for v2 in vLinha:
                    custo = self.custoDireto(v1, v2)
                    if custo < custo_min:
                        va = v1
                        vb = v2
                        custo_min = custo
            
            if custo_min < float("inf"):
                listEdges.append((va, vb, custo_min))
                vertex.append(vb)
                vLinha.remove(vb)
                pesoTotal = pesoTotal + custo_min
        
        print(pesoTotal)


if __name__ == "__main__":
    i = 1           # inicia nomes dos vertices
    g = Grafo([])   # inicia o grafo
    
    # inicia leitura de 
    inp = input().strip().split(' ')
    N = int(inp[0])
    M = int(inp[1])
    
    # inicia o conjunto de vertices
    for v in range(N):
        v = Vertice([], i)
        i = i + 1
        g.addVertice(v)

    for j in range(M):
        inpArestas = input().strip().split(' ')
        Part = int(inpArestas[0])           # indica o vertice de partida
        Dest = int(inpArestas[1])           # indica o vertice de destino
        Cust = int(inpArestas[2])           # indica o custo da aresta
        aresta = Aresta(Part, Dest, Cust)   # inicia a aresta com as infos
        for v in g.listVertices:
            if j == v.name:    
                vertice.addAresta(aresta)   # inclui a aresta na lista de vertices

    # chama a funcao prim que printa o valor do peso total
    g.prim()
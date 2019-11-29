class Aresta:
    def __init__(self, vertPart, vertDest, peso):
        self.vertPart = vertPart
        self.vertDest = vertDest
        self.peso = peso


class Grafo:
    def __init__(self, listVertices, listAresta):
        self.listVertices = listVertices
        self.listAresta = listAresta


    def addVertice(self, v):
        self.listVertices.append(v)


    def addAresta(self, a):
        self.listAresta.append(a)


    def custoDireto(self, verticeP, verticeD):
        peso = float("inf")
        for a in self.listAresta:
            if (a.vertPart == verticeP and a.vertDest == verticeD) or (a.vertPart == verticeD and a.vertDest == verticeP):
                peso = a.peso
                break
        return peso


    def prim(self):
        vertex = [self.listVertices[0]]
        listEdges = []
        pesoTotal = 0

        vLinha = self.listVertices
        # print(vLinha)
        vLinha.remove(self.listVertices[0])
        # print(vLinha)

        for i in range(len(vLinha)):
            custo_min = float("inf")
            va = None
            vb = None
            # print(vertex)
            # print(vLinha)
            for v1 in vertex:
                for v2 in vLinha:
                    custo = self.custoDireto(v1, v2)
                    if custo < custo_min:
                        va = v1
                        vb = v2
                        custo_min = custo
                        # print(va)
                        # print(vb)

            if custo_min < float("inf"):
                listEdges.append((va, vb, custo_min))
                vertex.append(vb)
                vLinha.remove(vb)
                pesoTotal += custo_min
        # print(listEdges)
        # print(vertex)
        # print(vLinha)
        print(pesoTotal)


if __name__ == "__main__":
    g = Grafo([], [])   # inicia o grafo

    # inicia leitura de 
    inp = input().strip().split(' ')
    N = int(inp[0])
    M = int(inp[1])

    # inicia o conjunto de vertices
    for v in range(1,N + 1):
        g.addVertice(v)

    for j in range(M):
        inpArestas = input().strip().split(' ')
        Part = int(inpArestas[0])           # indica o vertice de partida
        Dest = int(inpArestas[1])           # indica o vertice de destino
        Cust = int(inpArestas[2])           # indica o custo da aresta
        aresta = Aresta(Part, Dest, Cust)   # inicia a aresta com as infos
        g.addAresta(aresta)                 # inclui a aresta na lista de arestas

    # chama a funcao prim que printa o valor do peso total
    g.prim()
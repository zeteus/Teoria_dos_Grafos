class Grafo(object):
    def __init__(self):
        self.vertices = list()


    def complete(self, n):
        for i in range(n):
            self.vertices.append(vertex(i+1))
    
    
    def print_grafo(self):
        for i in self.vertices:
            i.print_vertice()


    def add_arestas(self, name, name2, p):
        if p == 1:
            for i in self.vertices:
                if i.name == name:
                    if not bool(i.vizinhos):
                        i.vizinhos.append(name2)
                    else:
                        if (name not in i.vizinhos):
                            i.vizinhos.append(name2)
        else:
            for i in self.vertices:
                if i.name == name:
                    if not bool(i.vizinhos):      
                        i.vizinhos.append(name2)
                    else:
                        if (name2 not in i.vizinhos):
                            i.vizinhos.append(name2)
                        
            for i in self.vertices:
                if i.name == name2:
                    if not bool(i.vizinhos):      
                        i.vizinhos.append(name)
                    else:
                        if (name not in i.vizinhos):
                            i.vizinhos.append(name)



class vertex(object):
    def __init__(self, name):
        self.name = name
        self.vizinhos = list()


    def print_vertice(self):
        print("Nome: {}".format(self.name))
        print("Vizinhos: {}".format(self.vizinhos))


def ir_vir(vert, grafo):
    if grafo.vertices[vert].vizinhos == []:
        return 0
    if len(grafo.vertices[vert].vizinhos) == len(grafo.vertices) - 1:
        return 1
    else:
        grafo.vertices[vert].vizinhos = grafo.vertices[vert].vizinhos + grafo.vertices[vert + 1].vizinhos
        vert = vert +1
        return ir_vir(vert, grafo)


def retira_repetidos(lista):
    if lista[0] == 0:
        return []
    elif lista[0] in lista[1:]:
        return retira_repetidos(lista[1:])
    else:
        return [lista[0]] + retira_repetidos(lista[1:])


if __name__ == '__main__':
    N, M = 1,1
    resp = []
    i = 0
    while (N, M) != (0, 0):
        N, M = [int(x) for x in input().split()]
        grafo = Grafo()
        grafo.complete(N)
        i = 0
        while i < M:
            V, W, P = [int(y) for y in input().split()]
            grafo.add_arestas(V,W,P)
            i += 1
        resp = resp + [ir_vir(0, grafo)]
    while(i < len(resp)):
        print(resp[i])
        i = i + 1
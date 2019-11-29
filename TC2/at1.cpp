#include <iostream>
#include <list>

class Aresta {
    public:
        int vertPart;
        int vertDest;
        int peso;

        Aresta(int vp, int vd, int p) {
            this->vertPart = vp;
            this->vertDest = vd;
            this->peso = p;
        }

        ~Aresta() {}
};

class Grafo {
    public:
        std::list<int> vertices;
        std::list<Aresta> arestas;
    
        Grafo() {// list<int> vertices = new list<int>();
        }

        ~Grafo() {
            // delete(this->arestas);
        }

        void addV(int v) {vertices.push_back(v);}
        
        void addA(Aresta* a) {arestas.push_back(*a);}
        
        int custoDireto(int vP, int vD) {
            int peso = __INT_MAX__;
            for(Aresta a: this->arestas) {
                if((a.vertPart == vP && a.vertDest == vD) || (a.vertPart == vD && a.vertDest == vP)) {
                    peso = a.peso;
                    break;
                }
            }
            return peso;
        }

        void prim() {
            int pesoT = 0;
            std::list<int> vertex;
            vertex.push_back(this->vertices.front());
            std::list<int> vLinha = this->vertices;
            vLinha.remove(this->vertices.front());
            
            std::list<int> l;
            for(int i = 0; i < vLinha.size(); i++){
	        	l.push_back(i);
	        }
            
            for(int i: l) {
                int custo_min = __INT_MAX__;
                int va = -1;
                int vb = -1;
                for(int v1: vertex) {
                    for(int v2: vLinha) {
                        int custo = this->custoDireto(v1, v2);
                        if(custo < custo_min) {
                            va = v1;
                            vb = v2;
                            custo_min = custo;
                        }
                    }
                }
                if(custo_min < __INT_MAX__) {
                    vertex.push_back(vb);
                    vLinha.remove(vb);
                    pesoT += custo_min;
                }
            }

            std::cout << pesoT << std::endl;
        }
};

int main() {
    Grafo* g = new Grafo();
    int N, M;
    std::cin >> N;
    std::cin >> M;

    for(int i = 1; i < N + 1; i++) {
        g->addV(i);
    }
    for(int i = 0; i < M; i++) {
        int p, d, c;
        std::cin >> p;
        std::cin >> d;
        std::cin >> c;
        Aresta* arest = new Aresta(p, d, c);
        g->addA(arest);
    }
    g->prim();
    
    delete(g);
}
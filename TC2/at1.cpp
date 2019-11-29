#include <iostream>
#include <list>
#include <vector>

class Grafo {
    public:
        // std::list<Aresta> arestas;
        std::list<int> vertices;
        std::vector<std::vector<int> > pesos;
    
        Grafo(int nV) {
            this->pesos = std::vector<std::vector<int> >(nV);
            for(int i = 0; i < nV; i++) {
                this->pesos[i] = std::vector<int>(nV);
                for(int j = 0; j < nV; j++) {
                    this->pesos[i][j] = __INT_MAX__;
                }
            }
            for(int i = 1; i < nV + 1; i++) {
               this->vertices.push_back(i);
            }
        }

        ~Grafo() {}
        
        int custoDireto(int vP, int vD) {
            return this->pesos[vP - 1][vD - 1];
        }

        void atualizaEstaPoha(int p, int d, int c) {
            this->pesos[p][d] = c;
            this->pesos[d][p] = c;
        }

        void prim() {
            int i = 0;
            int pesoT = 0;
            std::list<int> vertex;
            vertex.push_back(this->vertices.front());
            std::list<int> vLinha = this->vertices;
            vLinha.remove(this->vertices.front());
            int tam = vLinha.size();
            
            while(i < tam) {
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
                i++;
            }

            std::cout << pesoT << std::endl;
        }
};

int main() {
    int N, M;
    std::cin >> N;
    std::cin >> M;

    Grafo* g = new Grafo(N);
    
    for(int i = 0; i < M; i++) {
        int p, d, c;
        std::cin >> p;
        std::cin >> d;
        std::cin >> c;
        g->atualizaEstaPoha(p - 1, d - 1, c);
    }
    g->prim();
    delete(g);

    return 0;
}
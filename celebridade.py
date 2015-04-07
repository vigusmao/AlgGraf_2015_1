# Grafos nao-direcionados

import random
from time import time

N = 20000000
M = 0
#M = int(0.5 * N * (N-1) / 2)


def inicializar_grafo_MA(n_vertices):

# Comentando a maneira correta (tempo quadratico) de se inicializar uma 
# matriz de adjacencias zerada...
#
#    matriz_adj = [None] * n_vertices
#    for i in range(n_vertices):
#        linha = [False] * n_vertices
#        matriz_adj[i] = linha

# Hackeando a criacao de uma matriz de adjacencias de um grafo vazio.
# Dessa maneira, a matriz eh criada em tempo linear.
# Ela nao poderah ser modificada celula-a-celula, no entanto, pois
# todas as suas linhas sao referencias para uma mesma lista de celulas.

    matriz_adj = [[False] * n_vertices] * n_vertices


    return matriz_adj

def adicionar_aresta_MA(aresta, grafo):
    v1 = aresta[0]
    v2 = aresta[1]
    grafo[v1][v2] = True
    # grafo[v2][v1] = True

def adicionar_arestas_aleatorias_MA(n_arestas, grafo):
    n_vertices = len(grafo)
    todas_arestas = []
    for i in range(0, n_vertices):
        for j in range(0, n_vertices):
            if j == i:
                continue
            todas_arestas += [(i, j)]

    random.shuffle(todas_arestas)

    for i in range(n_arestas):
        adicionar_aresta(todas_arestas[i], grafo)

def mostrar_grafo_MA(grafo):
    for linha in grafo:
        print(linha)

def grau_saida_MA(vertice, grafo):
    grau = 0
    for celula in grafo[vertice]:
        if celula:
            grau += 1
    return grau

def grau_entrada_MA(vertice, grafo):
    n_vertices = len(grafo)
    grau = 0
    for i in range(0, n_vertices):
        celula = grafo[i][vertice]
        if celula:
            grau += 1
    return grau



def inicializar_grafo_hashing(n_vertices):
    return {i: [set(), set()] for i in range(0, n_vertices)}

def adicionar_aresta_hashing(aresta, grafo):
    v1 = aresta[0]
    v2 = aresta[1]
    vizinhos_saida_v1 = grafo.get(v1)[0]
    vizinhos_saida_v1.add(v2)
    vizinhos_entrada_v2 = grafo.get(v2)[1]
    vizinhos_entrada_v2.add(v1)
    

def celebridade_quadratico(grafo):
    n_vertices = len(grafo)
    for vertice in range(0, n_vertices):
       if grau_saida(vertice, grafo) == 0 and \
          grau_entrada(vertice, grafo) == n_vertices - 1:
           print("Vertice %d eh celebridade!" % vertice)
           return
    print("Nao ha celebridades!")


def celebridade_linear(grafo):
    n_vertices = len(grafo)
    candidato = 0
    # primeira rodada de perguntas (n-1 perguntas)
    for outro_vertice in range(1, n_vertices):
        if grafo[candidato][outro_vertice]:
            candidato = outro_vertice
            
    if grau_saida(candidato, grafo) == 0 and \
          grau_entrada(candidato, grafo) == n_vertices - 1:
           print("Vertice %d eh celebridade!" % candidato)
           return
    print("Nao ha celebridades!")

    
            

## main

start = time()
print("Gerando grafo...")
grafo = inicializar_grafo_MA(N)
#adicionar_arestas_aleatorias(M, grafo)
print("Tempo = %.4f segundos" % (time() - start))

start = time()
print("Rodando algoritmo linear da celebridade...")
celebridade_linear(grafo)
print("Tempo = %.4f segundos" % (time() - start))

#start = time()
#print("Rodando algoritmo quadratico da celebridade...")
#celebridade_quadratico(grafo)
#print("Tempo = %.4f segundos" % (time() - start))



        
    

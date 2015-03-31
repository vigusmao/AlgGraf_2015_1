# Grafos nao-direcionados

import random


N = 6
M = 3
#M = int(0.5 * N * (N-1) / 2)


def inicializar_grafo(n_vertices):
    matriz_adj = [None] * n_vertices
    for i in range(n_vertices):
        linha = [False] * n_vertices
        matriz_adj[i] = linha
    return matriz_adj


def adicionar_aresta(aresta, grafo):
    v1 = aresta[0]
    v2 = aresta[1]
    grafo[v1][v2] = True
    grafo[v2][v1] = True


def mostrar_grafo(grafo):
    for linha in grafo:
        print(linha)


def grau(vertice, grafo):
    grau = 0
    for celula in grafo[vertice]:
        if celula:
            grau += 1
    return grau


## main

grafo = inicializar_grafo(N)

todas_arestas = []
for i in range(0, N):
    for j in range(i + 1, N):
        todas_arestas += [(i, j)]

random.shuffle(todas_arestas)

for i in range(M):
    adicionar_aresta(todas_arestas[i], grafo)



        
    

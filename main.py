import random

def criar_labirinto(n_linhas, n_colunas, valor):
    if n_linhas > 0 and n_colunas > 0:
        matriz = []
        for i in range(n_linhas):
            linha = []
            for j in range(n_colunas):
                linha.append(valor)
            matriz.append(linha)
        return matriz

def imprimir_labirinto(matriz):
   for i in range(len(matriz)):
       print("")
       for j in range(len(matriz[0])):
           print(matriz[i][j], end = " ")


def inserir_wumpus(matriz):
    posicao_wumpus = random.randint(1, len(matriz)-1), random.randint(1, len(matriz[0])-1)
    return posicao_wumpus

def inserir_ouro(matriz, posicao_wumpus):
    posicao_ouro =  random.randint(1, len(matriz)-1), random.randint(1, len(matriz[0])-1)
    while posicao_ouro == posicao_wumpus:
        posicao_ouro = random.randint(1, len(matriz)-1), random.randint(1, len(matriz[0])-1)
    return posicao_ouro


def inserir_pocos(matriz):
    pass

def inserir_percepcao(matriz):
    pass

tm_matriz = int(input("Qual o tamanho da matriz?  "))
matriz = criar_labirinto(tm_matriz, tm_matriz, "?")
posicao_wumpus = inserir_wumpus(matriz)
posicao_ouro = inserir_ouro(matriz, posicao_wumpus)


matriz[posicao_ouro[0]][posicao_ouro[1]] = "O"
matriz[posicao_wumpus[0]][posicao_wumpus[1]] = 'W'
imprimir_labirinto(matriz)
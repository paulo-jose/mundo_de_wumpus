import random

def criar_labirinto(n_linhas, n_colunas, valor):
    matriz = []
    for i in range(n_linhas):
        linha = []
        for j in range(n_colunas):
            linha += [valor]
        matriz += [valor]
    return matriz

def imprimir_labirinto(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    for i in range(linhas):
        for j in range(colunas):
            print("%d" % matriz[i][j], end="")
            if (j == colunas - 1):
                print("%d" % matriz[i][j], end="")

        print()


tm_matriz = int(input("Qual o tamanho da matriz?  "))
matriz = criar_labirinto(tm_matriz, tm_matriz, "P")
imprimir_labirinto(matriz)
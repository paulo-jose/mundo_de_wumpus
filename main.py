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

def imprimir_labirinto_jogador(matriz):
    pass


def inserir_wumpus(matriz):
    posicao_wumpus = random.randint(0, len(matriz)-1), random.randint(0, len(matriz[0])-1)
    while posicao_wumpus == (0,0):
        posicao_wumpus = random.randint(0, len(matriz) - 1), random.randint(0, len(matriz[0]) - 1)
    return posicao_wumpus

def inserir_ouro(matriz, posicao_wumpus):
    posicao_ouro = random.randint(0, len(matriz)-1), random.randint(0, len(matriz[0])-1)
    while (posicao_ouro == posicao_wumpus) or (posicao_ouro == (0,0)):
        posicao_ouro = random.randint(0, len(matriz)-1), random.randint(0, len(matriz[0])-1)
    return posicao_ouro


def inserir_pocos(matriz, posicao_wumpus, posicao_ouro):
    numero_pocos = int((len(matriz) * len(matriz)) * 0.20) #porcetagem de poços
    for i in range(numero_pocos):
        posicao_poco = random.randint(0, len(matriz)-1), random.randint(0, len(matriz[0])-1)
        while ((posicao_poco == posicao_wumpus) or (posicao_poco == posicao_ouro) or (posicao_poco == (0,0)) or matriz[posicao_poco[0]][posicao_poco[1]] == "P"):
            posicao_poco = random.randint(0, len(matriz) - 1), random.randint(0, len(matriz[0]) - 1)
        matriz[posicao_poco[0]][posicao_poco[1]] = "P"
    return matriz

def inserir_percepcao(matriz):
    tamanho_matriz = len(matriz)
    percepcoes = [[[] for _ in range(tamanho_matriz)] for _ in range(tamanho_matriz)]

    def adjacentes(x, y):
        adj = []
        if x > 0:
            adj.append((x - 1, y))
        if x < tamanho_matriz - 1:
            adj.append((x + 1, y))
        if y > 0:
            adj.append((x, y - 1))
        if y < tamanho_matriz - 1:
            adj.append((x, y + 1))
        return adj

    for i in range(tamanho_matriz):
        for j in range(tamanho_matriz):
            if matriz[i][j] == "W":
                for (x, y) in adjacentes(i, j):
                    if(matriz[x][y] == "O"):
                        matriz[x][y] = "OF"
                    elif(matriz[x][y] == "P"):
                        matriz[x][y] = "P"
                    else:
                        matriz[x][y] = "F"
            elif matriz[i][j] == "P":
                for (x, y) in adjacentes(i, j):
                    if(matriz[x][y] == "F"):
                        matriz[x][y] = "FB"
                    elif(matriz[x][y] == "O"):
                        matriz[x][y] = "OB"
                    elif (matriz[x][y] == "W"):
                        matriz[x][y] = "W"
                    elif (matriz[x][y] == "P"):
                        matriz[x][y] = "P"
                    else:
                        matriz[x][y] = "B"
    return percepcoes

def movimento_jogador(matriz, movimento):
    pass


def play_game(matriz):
    # inserir jogador
    matriz[0][0] = "J"
    while True:
        print("Labirinto atual ...")
        print(imprimir_labirinto_jogador(matriz))
        movimento = input("Para onde desja mover (cima, baixo, esquerda, direita): ").lower()
        movimento_jogador(matriz, movimento)




tm_matriz = int(input("Qual o tamanho da matriz?  "))
matriz = criar_labirinto(tm_matriz, tm_matriz, "?")
posicao_wumpus = inserir_wumpus(matriz)
posicao_ouro = inserir_ouro(matriz, posicao_wumpus)
imprimir_labirinto(matriz)

matriz[posicao_ouro[0]][posicao_ouro[1]] = "O"
matriz[posicao_wumpus[0]][posicao_wumpus[1]] = 'W'
inserir_pocos(matriz, posicao_wumpus, posicao_ouro)
print()
imprimir_labirinto(matriz)
print()
inserir_percepcao(matriz)
print()
imprimir_labirinto(matriz)


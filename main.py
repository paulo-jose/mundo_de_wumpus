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
                    elif (matriz[x][y] == "B"):
                        matriz[x][y] = "FB"
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
    return matriz

def movimento_automatico(matriz):
    direcoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # movimento do agente cima, baixo, esquerda, direita
    visitado = set()
    jogo_terminado = False

    def buscar_caminho(x, y):
        nonlocal jogo_terminado
        if jogo_terminado:
            return False
        if (x, y) in visitado:
            return False
        visitado.add((x, y))
        
        # Verificando o que tem na posição atual
        if matriz[x][y] == "W":
            print("Agente foi devorado pelo Wumpus! Fim de jogo.")
            jogo_terminado = True
            return False
        elif matriz[x][y] == "P":
            print("Agente caiu em um poço! Fim de jogo.")
            jogo_terminado = True
            return False
        elif matriz[x][y] == "O":
            print("Agente encontrou o ouro! Você ganhou!")
            jogo_terminado = True
            return True
        
        # Marcando as posições do agente na matriz
        matriz[x][y] = "J"
        imprimir_labirinto(matriz)
        print()
        
        # Explorando as direções possíveis
        for dx, dy in direcoes:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]):
                if buscar_caminho(nx, ny):
                    return True
        
        # Se não encontrou, desmarca a posição do agente (backtracking)
        matriz[x][y] = " "
        return False

    return buscar_caminho(0, 0)


# def movimento_jogador(matriz, movimento): // Novo teste para movimento implementado
#     pass


def play(matriz):
    # inserir jogador
    matriz[0][0] = "J"
    sucesso = movimento_automatico(matriz)
    if sucesso:
        print("Parabéns, o ouro foi encontrado!")
    else:
        print("Infelizmente, o ouro não foi encontrado. Tente novamente!")
    
    
    # inserindo novo código para movimento, preciso validar se o movimento é valido

    # while True:
    #     print("Labirinto atual ...")
    #     print(imprimir_labirinto_jogador(matriz))
    #     movimento = input("Para onde deseja mover (cima, baixo, esquerda, direita): ").lower()
    #     movimento_jogador(matriz, movimento)




tm_matriz = int(input("Qual o tamanho da matriz?  "))
matriz = criar_labirinto(tm_matriz, tm_matriz, "?")
posicao_wumpus = inserir_wumpus(matriz)
posicao_ouro = inserir_ouro(matriz, posicao_wumpus)
imprimir_labirinto(matriz)

matriz[posicao_ouro[0]][posicao_ouro[1]] = "O"
matriz[posicao_wumpus[0]][posicao_wumpus[1]] = 'W'
inserir_pocos(matriz, posicao_wumpus, posicao_ouro)
print()

# imprimir_labirinto(matriz) Estou removendo por bug de duplicação de matriz no código! 

print()
inserir_percepcao(matriz)
print()
imprimir_labirinto(matriz)

#chamando o a função de movimento automático do agente e inicio de jogo
play(matriz)


import random
import Agente

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
    posicao_wumpus = random.randint(0, len(matriz)-1), random.randint(0, len(matriz[0])-1)
    while posicao_wumpus == (0,0):
        posicao_wumpus = random.randint(0, len(matriz) - 1), random.randint(0, len(matriz[0]) - 1)
    return posicao_wumpus

def inserir_ouro(matriz, posicao_wumpus):
    posicao_ouro = random.randint(0, len(matriz)-1), random.randint(0, len(matriz[0])-1)
    while (posicao_ouro == posicao_wumpus) or (posicao_ouro == (0,0)):
        posicao_ouro = random.randint(0, len(matriz)-1), random.randint(0, len(matriz[0])-1)
    return posicao_ouro

def adjacentes(x, y, matriz):
    tamanho_matriz = len(matriz)
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

def movimento_jogador(campo_jogador, movimento):
    posicao_jogador_x, posicao_jogador_y = buscar_jogador(campo_jogador)
    tm_matriz = len(campo_jogador)
    if posicao_jogador_x is None or posicao_jogador_y is None:
        return

    if movimento == "cima" and posicao_jogador_x > 0:
        campo_jogador[posicao_jogador_x][posicao_jogador_y], campo_jogador[posicao_jogador_x - 1][posicao_jogador_y] = campo_jogador[posicao_jogador_x - 1][posicao_jogador_y], campo_jogador[posicao_jogador_x][posicao_jogador_y]
    elif movimento == "baixo" and posicao_jogador_x < tm_matriz- 1:
        campo_jogador[posicao_jogador_x][posicao_jogador_y], campo_jogador[posicao_jogador_x + 1][posicao_jogador_y] = campo_jogador[posicao_jogador_x + 1][posicao_jogador_y], campo_jogador[posicao_jogador_x][posicao_jogador_y]
    elif movimento == "esquerda" and posicao_jogador_y > 0:
        campo_jogador[posicao_jogador_x][posicao_jogador_y], campo_jogador[posicao_jogador_x][posicao_jogador_y - 1] = campo_jogador[posicao_jogador_x][posicao_jogador_y - 1], campo_jogador[posicao_jogador_x][posicao_jogador_y]
    elif movimento == "direita" and posicao_jogador_y < tm_matriz - 1:
        campo_jogador[posicao_jogador_x][posicao_jogador_y], campo_jogador[posicao_jogador_x][posicao_jogador_y + 1] = campo_jogador[posicao_jogador_x][posicao_jogador_y + 1], campo_jogador[posicao_jogador_x][posicao_jogador_y]
    else:
        print("Bateu na parede, faça outro movimento!")


def buscar_jogador(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == "J":
                return i, j
    return None, None

def verificar_percepcao(matriz, x, y):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            if matriz[i][j] == "B" and x == i and y==j:
                return ("O jogador está sentindo brisa")
            elif matriz[i][j] == "F" and x == i and y==j:
                return ("O jogador está sentindo fedor")
            elif matriz[i][j] == "FB" and x == i and y==j:
                return ("O jogador está sentindo fedor e brisa")
            elif matriz[i][j] == "OB" and x == i and y==j:
                return ("Parabéns o você pegou o ouro, mas está sentido brisa")
            elif matriz[i][j] == "OF" and x == i and y==j:
                return ("Parabéns você pegou o ouro, mas está sentido fedor")
            elif matriz[i][j] == "P" and x == i and y==j:
                return ("Você caiu no poço, fim de Jogo! :(")
            elif matriz[i][j] == "W" and x == i and y==j:
                return ("Você foi devorado pelo Wumpus, fim de Jogo! :(")


def play_jogador(matriz):
    # inserir jogador
    campo_jogador = criar_labirinto(len(matriz), len(matriz), "?")
    campo_jogador[0][0] = "J"
    while True:

        print("\nLabirinto atual ... \n")
        print(imprimir_labirinto(campo_jogador))
        posicao_jogador_x, posicao_jogador_y = buscar_jogador(campo_jogador)
        print(f"Posicao do jogador eh: {posicao_jogador_x} , {posicao_jogador_y} ")
        jogada = verificar_percepcao(matriz, posicao_jogador_x, posicao_jogador_y)
        print("\n")
        if(jogada != None):
            if(jogada == "Você caiu no poço, fim de Jogo! :("):
                print(jogada)
                break
            elif(jogada == "Você foi devorado pelo Wumpus, fim de Jogo! :("):
                print(jogada)
                break
            print(jogada, "\n")
        movimento = input("Para onde deseja mover (cima, baixo, esquerda, direita): ").lower()
        movimento_jogador(campo_jogador, movimento)


def play_agente(matriz):
    # inserir jogador
    matriz[0][0] = "J"
    sucesso = movimento_automatico(matriz)
    if sucesso:
        print("Parabéns, o ouro foi encontrado!")
    else:
        print("Infelizmente, o ouro não foi encontrado. Tente novamente!")



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
play_agente(matriz)
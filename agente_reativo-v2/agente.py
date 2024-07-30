import random


class Agente:

    def __init__(self, mundo, caderno):
        self.mundo = mundo
        self.caderno = caderno
        self.ultima_posicao = (0,0)
        self.posicao_atual = (0,0)
        self.valor_original = "0"
        self.ouro_encontrado = False
        self.wumpus_morto = False
        self.acoes = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        self.memoria = [["." for _ in range(self.mundo.tamanho_colunas)] for _ in range(self.mundo.tamanho_linhas)] # Matriz de memória
        self.crencas = [["." for _ in range(self.mundo.tamanho_colunas)] for _ in range(self.mundo.tamanho_linhas)] # Matriz de crenças do agente (Beliefs)
        self.probabi = [[0.01 for _ in range(self.mundo.tamanho_colunas)] for _ in range(self.mundo.tamanho_linhas)] # Matriz de probabilidade
        self.flechas = 1 # Quantidade de flechas do agente

    def sensor(self):
            
            px, py = self.posicao_atual #Guarda a posição atual do agente

            if "W" in self.mundo.matriz[px][py]:
                print("O agente foi morto pelo Wumpus!")
                exit()
            if "P" in self.mundo.matriz[px][py]:
                print("O agente caiu em um poço!")
                exit()
            
            self.memoria[px][py] = "V"
            self.crencas[px][py] = "S"
            self.probabi[px][py] = 0.0

            if self.posicao_ouro(px, py):
                return
            
            #verifica se a posição atual está no caderno 
            analise = self.caderno.verificar_caderno(self.posicao_atual)
            if analise != False:
                
                #Atualiza a probabilidade das posições adjacentes
                for pos in analise:
                    pos_x, pos_y = pos
                    self.probabi[pos_x][pos_y] += round(1 / len(analise), 2)
                    #Normalizar as probabilidades
                    if self.probabi[px][py] > 1.0:
                        self.probabi[px][py] = 1.0


            self.valor_original = self.mundo.matriz[self.posicao_atual[0]][self.posicao_atual[1]] #Guarda o valor original da posição antes de mover
            self.atualizar_memoria(px, py) #Atualiza a memória do agente
    
    def posicao_ouro(self, pos_ox, pos_oy): #Posição do ouro em X e Y

        if "O" in self.mundo.matriz[pos_ox][pos_oy]:
            
            self.ouro_encontrado = True

            if len(self.mundo.matriz[pos_ox][pos_oy]) > 1 and "O" in self.mundo.matriz[pos_ox][pos_oy]:
                self.mundo.matriz[pos_ox][pos_oy] = self.mundo.matriz[pos_ox][pos_oy].replace("O", "")
            else:
                self.mundo.matriz[pos_ox][pos_oy] = "0"

            print("Ouro encontrado!")

            caminho = self.a_estrela(self.posicao_atual, (0, 0))
            if caminho is not None:
                for nova_pos in caminho:
                    if self.posicao_atual == nova_pos:
                        continue

                    self.mundo.atualizacao_matriz(self.valor_original, self.posicao_atual, nova_pos, "A")
                    self.posicao_atual = nova_pos
                    self.mundo.imprimir_matriz(self)

            return self.ouro_encontrado

        return False

    def mover(self):

        pos_escolhida = []
        pos_escolhida = self.explorar_pos_seguras()

        if  not pos_escolhida: #verificar esse erro de index!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            pos_escolhida = self.explorar_menor_probabilidade()

        pos_escolhida = random.choice(pos_escolhida)
        
        caminho = self.a_estrela(self.posicao_atual, pos_escolhida)

        if caminho is not None:
            for nova_pos in caminho:

                self.mundo.atualizacao_matriz(self.valor_original, self.posicao_atual, nova_pos, "A")
                self.posicao_atual = nova_pos
                self.mundo.imprimir_matriz(self)
                self.sensor()

    
    #Posições seguras antes de arriscar
    def explorar_pos_seguras(self):

        pos_explorar = []

        for i in range(len(self.memoria)):
            for j in range(len(self.memoria[0])):
                if self.memoria[i][j] == "." and self.probabi[i][j] == 0.0:
                    pos_explorar.append((i, j))
        
        if len(pos_explorar) == 0:
            return False
        else:
            return pos_explorar
    
    # Sem posições seguras não visitadas então explorar a menor probabilidade 
    def explorar_menor_probabilidade(self):

        menor_prob = 1.0
        pos_menor_prob = []
        
        # Verificando as posições da crença
        for i in range(len(self.crencas)):
            for j in range(len(self.crencas[0])):
                if self.crencas[i][j] == ".":
                    continue
                else:
                    pos_menor_prob.append((i, j))

        # Verificando as posições da probabilidade com menor probabilidade de perigo
        for x, y in pos_menor_prob:
            menor_prob = min(menor_prob, self.probabi[x][y])
        
        return pos_menor_prob
        
    def atualizar_memoria(self, mx, my): # MX(Memoria posição X) = linha, MY (Memoria posição Y) = coluna

        percepcoes = self.mundo.matriz[mx][my]

        if "B" not in percepcoes and "F" not in percepcoes:
            # self.memoria[mx][my] = "V" # Marcar a posição atual como visitada

            if self.crencas[mx][my] == "." and self.probabi[mx][my] == 0.01:
                self.crencas[mx][my] = "S"
                self.probabi[mx][my] = 0.0

            self.atualizar_crencas(mx, my, "S") # Atualizar células adjacentes como seguras

        elif "B" in percepcoes:  # Brisa
            # self.memoria[mx][my] = "V"
            self.atualizar_crencas(mx, my, "P") # Atualizar células adjacentes como inseguras

        elif "F" in percepcoes:  # Fedor
            # self.memoria[mx][my] = "V"
            self.atualizar_crencas(mx, my, "W") # Atualizar células adjacentes como Inseguras


    #Matriz de estado - As crenças do agente sobre o mundo (Beliefs)
    def atualizar_crencas(self, x, y, crenca):

        pos_crencas = self.obter_posicoes_adjacentes(x, y)
        pos_crenca_copia = pos_crencas.copy() # Copia da lista de posições de crenças para iterar sobre ela

        for pos_crenca in pos_crenca_copia:
                cx, cy = pos_crenca

                if self.crencas[cx][cy] == "S": # Se a posição já foi marcada como segura
                    pos_crencas.remove(pos_crenca)
                    continue

                elif self.crencas[cx][cy] == ".":
                    self.crencas[cx][cy] = crenca
        

        self.caderno.adicionar_anotacao(self.posicao_atual, pos_crencas) #Adicionar anotação no caderno das posições com probabilidade de perigo
        self.atualizar_probabilidade(pos_crencas)    
                    
    # As probabilidades estão medindo em porcetagem a chance de ter perigo em uma célula adjacente
    def atualizar_probabilidade(self, pos_probs):
        
        pos_probs = pos_probs
        if len(pos_probs) == 0:
            return
        
        for pos_prob in pos_probs: # Para posição da probabilidade nas lista de posições de probabilidades
            px, py = pos_prob
            if self.crencas[px][py] == "S":
                self.probabi[px][py] = 0.0 #Probabilidade de Perigo
            else:
                if self.probabi[px][py] >=1.0:
                    continue
                self.probabi[px][py] += round(1 / len(pos_probs), 2) #Probabilidade de Perigo

                #Normalizar as probabilidades
                if self.probabi[px][py] > 1.0:
                    self.probabi[px][py] = 1.0

    
    def h(self, pos, objetivo):

        return abs(pos[0] - objetivo[0]) + abs(pos[1] - objetivo[1])

    def a_estrela(self, inicio, objetivo):

        abertos = set([inicio])
        fechados = set()
        g = {inicio: 0}
        f = {inicio: self.h(inicio, objetivo)}
        pais = {inicio: inicio}

        while len(abertos) > 0:
            atual = None
            for pos in abertos:
                if atual is None or f[pos] < f[atual]:
                    atual = pos

            if atual == objetivo:
                caminho = []
                while pais[atual] != atual:
                    caminho.append(atual)
                    atual = pais[atual]
                caminho.append(inicio)
                caminho.reverse()

                if self.posicao_atual in caminho:
                    caminho.remove(self.posicao_atual)
                    return caminho

            abertos.remove(atual)
            fechados.add(atual)

            for dx, dy in self.acoes:
                vizinho = (atual[0] + dx, atual[1] + dy)
                if 0 <= vizinho[0] < len(self.memoria) and 0 <= vizinho[1] < len(self.memoria[0]):
                    if vizinho in fechados:
                        continue
                    custo_g_temp = g[atual] + 1  # assumindo custo constante de 1 para qualquer movimento

                    if vizinho not in abertos:
                        abertos.add(vizinho)
                    elif custo_g_temp >= g[vizinho]:
                        continue

                    pais[vizinho] = atual
                    g[vizinho] = custo_g_temp
                    f[vizinho] = g[vizinho] + self.h(vizinho, objetivo)

        return None
                    
    def obter_posicoes_adjacentes(self, x, y):

        # Gerar uma lista de posições possíveis a partir da posição atual
        adjacentes = []
        for dx, dy in self.acoes:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(self.memoria) and 0 <= ny < len(self.memoria[0]):
                adjacentes.append((nx, ny))
        return adjacentes


    def atirar_flecha(self):

        if self.flechas > 0:
            mx, my = self.posicao_atual
            # Verificar células adjacentes para possíveis Wumpus
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = mx + dx, my + dy
                if 0 <= nx < len(self.memoria) and 0 <= ny < len(self.memoria[0]) and "W?" in self.memoria[nx][ny]:
                    # Decidir atirar na direção do Wumpus
                    print(f"Atirando flecha na direção: ({dx}, {dy})")
                    self.flechas -= 1
                    # Verificar se o Wumpus foi atingido
                    if "W" in self.mundo.matriz[nx][ny]:
                        print("Wumpus atingido!")
                        self.mundo.matriz[nx][ny] = self.mundo.matriz[nx][ny].replace("W", "")
                        self.memoria[nx][ny] = self.memoria[nx][ny].replace("W?", "S")  # Marcar como seguro após atingir
                    else:
                        print("Flecha desperdiçada.")
                    break  # Sair após atirar uma flecha


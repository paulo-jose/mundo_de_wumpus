import random

class Agente:
    def __init__(self, mundo):
        self.mundo = mundo
        self.posicao_atual = (0,0)
        self.valor_original = "0"
        self.ouro_encontrado = False
        self.memoria = [["." for _ in range(self.mundo.tamanho_colunas)] for _ in range(self.mundo.tamanho_linhas)] # Matriz de memória
        self.flecha = 1 # Quantidade de flechas do agente

    
    def mover(self):
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Lista de movimentos possíveis: Direita, Esquerda, Baixo, Cima
        direcao = random.choice(direcoes)
        dx, dy = direcao
        nx, ny = self.posicao_atual[0] + dx, self.posicao_atual[1] + dy # NX = Nova posição X, NY = Nova posição Y
    
        if 0 <= nx < len(self.mundo.matriz) and 0 <= ny < len(self.mundo.matriz[0]):
            
            self.valor_original = self.mundo.matriz[self.posicao_atual[0]][self.posicao_atual[1]] #Guarda o valor original da posição antes de mover
            self.sensor(self.posicao_atual[0], self.posicao_atual[1])

            if self.mundo.matriz[nx][ny] == "0":

                self.mundo.matriz[self.posicao_atual[0]][self.posicao_atual[1]] = self.valor_original #Removendo o agente da posição atual e seguindo para a proxima posição
                
                if len(self.valor_original) > 1 and "A" in self.valor_original:
                    self.mundo.matriz[self.posicao_atual[0]][self.posicao_atual[1]] = self.valor_original.replace("A", "") #Removendo o agente da posição antiga
                else:
                    self.mundo.matriz[self.posicao_atual[0]][self.posicao_atual[1]] = "0"

                self.mundo.matriz[nx][ny] = "A" #A - movido para próxima posição 
                self.posicao_atual = (nx, ny) # Atualizando posição agente com a nova posição
                self.mundo.imprimir_matriz(self)
            else:
                # Verificando o que tem na posição atual e se é uma percepção ou end-game(W ou P)
                
                if len(self.valor_original) > 1 and "A" in self.valor_original:
                    self.mundo.matriz[self.posicao_atual[0]][self.posicao_atual[1]] = self.valor_original.replace("A", "") #Removendo o agente da posição antiga
                else:
                    self.mundo.matriz[self.posicao_atual[0]][self.posicao_atual[1]] = "0"

                self.mundo.matriz[nx][ny] += "A"
                
                self.posicao_atual = (nx, ny)
                self.posicao_ouro(nx, ny)
                self.mundo.imprimir_matriz(self)
        else:
            self.mover()
            # print("Posição inválida")

        self.verificar_objetivo()


    def posicao_ouro(self, pos_ox, pos_oy): #Posição do ouro em X e Y
        if "O" in self.mundo.matriz[pos_ox][pos_oy]:

            if len(self.mundo.matriz[pos_ox][pos_oy]) > 1 and "O" in self.mundo.matriz[pos_ox][pos_oy]:
                self.mundo.matriz[pos_ox][pos_oy] = self.mundo.matriz[pos_ox][pos_oy].replace("O", "")
            else:
                self.mundo.matriz[pos_ox][pos_oy] = "0"

            print("Ouro encontrado!")
            self.ouro_encontrado = True
    
    def verificar_objetivo(self):
        if self.ouro_encontrado and self.posicao_atual == (0, 0):
            return True
        return False

    
    def sensor(self, pos_x, pos_y): # Pos_x = linha, Pos_y = coluna - Verificando o que tem na posição atual para tomada de decisão ou consequências de fim de jogo (P ou W)

        if "F" in self.mundo.matriz[pos_x][pos_y] or self.mundo.matriz[pos_x][pos_y] == "F":
            if self.flecha != 0:
                self.atirar_flecha()

        if "W" in self.mundo.matriz[pos_x][pos_y] and self.mundo.wumpus.esta_vivo():
            print("O agente foi devorado pelo Wumpus! Fim de jogo")
            exit()
        elif "W" in self.mundo.matriz[pos_x][pos_y] and not self.mundo.wumpus.esta_vivo():
            print("O agente encontrou o Wumpus morto!") #Mensagem de teste para verificar o código!
            pass
        if "P" in self.mundo.matriz[pos_x][pos_y]:
            print("O agente caiu em um Poço! Fim de jogo")
            exit()

    def atirar_flecha(self):
        direcoes_f = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Lista de movimentos possíveis: Direita, Esquerda, Baixo, Cima para a flecha
        direcao = random.choice(direcoes_f)
        dfx, dfy = direcao
        nfx, nfy = self.posicao_atual[0] + dfx, self.posicao_atual[1] + dfy # NFX e NFY = Direção Flecha X e Y
    
        if 0 <= nfx < len(self.mundo.matriz) and 0 <= nfy < len(self.mundo.matriz[0]): # Verificando se a posição escolhida para a flecha vai esta dentro dos limites do mundo
            
            self.flecha = 0
            # Colocar a flecha na posição selecionada aleatoriamente
            if self.mundo.matriz[nfx][nfy] == "0":
                self.mundo.matriz[nfx][nfy] = "1"
            else:
                self.mundo.matriz[nfx][nfy] += "1"

            if "W" in self.mundo.matriz[nfx][nfy]:
                print("O agente matou o wumpus! hehe")
                self.mundo.ecoar_gritos_wumpus() # Ecoar os gritos do wumpus pela matriz
                self.mundo.imprimir_matriz(self) # Imprimir o mundo atualizado
                self.mundo.wumpus.vivo = False # Wumpus morto
                
                self.mundo.atualizacao_matriz()
                self.valor_original = self.mundo.matriz[self.posicao_atual[0]][self.posicao_atual[1]] # Teste de atualização valor original

        else:
            self.atirar_flecha()

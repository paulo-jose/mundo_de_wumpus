import random

class Agente:
    def __init__(self, mundo):
        self.mundo = mundo
        self.posicao_atual = (0, 0)
        self.valor_original = "0"
        self.ouro_encontrado = False
    
    def mover(self):
        direcoes = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Lista de posições: Direita, Esquerda, Baixo, Cima
        direcao = random.choice(direcoes)
        dx, dy = direcao
        nx, ny = self.posicao_atual[0] + dx, self.posicao_atual[1] + dy
        # print("Nova posição agente", nx, ny)
    
        if 0 <= nx < len(self.mundo.matriz) and 0 <= ny < len(self.mundo.matriz[0]):
            self.mundo.matriz[self.posicao_atual[0]][self.posicao_atual[1]] = self.valor_original # Adciona o valor original gerado pelo mundo de wumpus na posição em que o agente esta para só então realizar próximo movimento
            if self.mundo.matriz[nx][ny] == "0":
                self.valor_original = "0"
                self.mundo.matriz[nx][ny] = "A"
                self.posicao_atual = (nx, ny)
                self.mundo.imprimir_matriz()
            else:
                self.valor_original = self.mundo.matriz[nx][ny]
                self.mundo.matriz[nx][ny] += "A"
                self.posicao_ouro(nx, ny)
                self.posicao_atual = (nx, ny)
                self.mundo.imprimir_matriz()
        else:
            pass
            # print("Posição inválida")

        self.verificar_objetivo()

    def posicao_ouro(self, nx, ny):
        if "O" in self.mundo.matriz[nx][ny]:
            print("Ouro encontrado! Fim")
            self.ouro_encontrado = True
    
    def verificar_objetivo(self):
        if self.ouro_encontrado and self.posicao_atual == (0, 0):
            return True

        return False
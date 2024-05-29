import random


class Agente:
    def __init__(self, memoria, pontos, qtd_flecha):
        self.memoria = memoria
        self.pontos = pontos
        self.qtd_flecha = qtd_flecha
        self.posicaoX = 0
        self.posicaoY = 0
        self.direcao = None


    def percepcao(self, fedor,brisa, reflexo,grito):
        movimento = random.randint(0, 3)
        if(fedor == True):
            if(movimento == 0):
                self.direcao = "direita"
            elif(movimento == 1):
                self.direcao = "esquerda"
            elif (movimento == 2):
                self.direcao = "cima"
            elif (movimento == 3):
                self.direcao = "baixo"
        elif(brisa == True):
            if (movimento == 0):
                self.direcao = "direita"
            elif (movimento == 1):
                self.direcao = "esquerda"
            elif (movimento == 2):
                self.direcao = "cima"
            elif (movimento == 3):
                self.direcao = "baixo"
        elif (reflexo == True):
            if (movimento == 0):
                self.direcao = "direita"
            elif (movimento == 1):
                self.direcao = "esquerda"
            elif (movimento == 2):
                self.direcao = "cima"
            elif (movimento == 3):
                self.direcao = "baixo"
        else:
            if (movimento == 0):
                self.direcao = "direita"
            elif (movimento == 1):
                self.direcao = "esquerda"
            elif (movimento == 2):
                self.direcao = "cima"
            elif (movimento == 3):
                self.direcao = "baixo"



    def atualizar_pontos(self, ponto):
        self.pontos += ponto
        if(self.pontos == 0):
            return "Fim de Jogo!"

    def fazer_jogada(self):
        pass



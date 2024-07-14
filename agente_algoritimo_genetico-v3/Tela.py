import time

import pygame
import numpy as np
import sys
import random

class Tela:
    def __init__(self, linhas, colunas):
        self.largura_janela = 500 + (colunas*linhas)*10
        self.altura_janela = 300 + (colunas*linhas)*10
        self.tamanho_celula = 100
        self.linhas = linhas
        self.colunas = colunas
        self.branco = (255, 255, 255)
        self.preto = (0, 0, 0)
        self.verde = (0, 255, 0)
        self.vermelho = (255, 0, 0)
        self.azul = (0, 0, 255)
        self.pygame = pygame
        self.pygame.init()
        # Criando a janela
        self.janela = self.pygame.display.set_mode((self.largura_janela, self.altura_janela))
        self.pygame.display.set_caption("Mundo de Wumpus")


# Função para inicializar o tabuleiro do jogo
    def inicializar_tabuleiro(self, labirinto):
        tabuleiro = np.zeros((self.linhas, self.colunas), dtype=int)
        pocos_pos = []
        for i in range(len(labirinto)):
            for j in range(len(labirinto)):
                if "A" in labirinto[i][j] or tabuleiro[i][j] == 1:
                    jogador_pos = (i, j)
                elif "O" in labirinto[i][j]:
                    ouro_pos = (i, j)
                elif labirinto[i][j] == "W":
                    wumpus_pos = (i, j)
                elif labirinto[i][j] == "P":
                    pocos_pos.append((i, j))

        # Atualizar o tabuleiro com os objetos
        tabuleiro[jogador_pos] = 1
        tabuleiro[ouro_pos] = 2
        tabuleiro[wumpus_pos] = 3
        for poco in pocos_pos:
            tabuleiro[poco] = 4

        return tabuleiro, jogador_pos, ouro_pos, wumpus_pos, pocos_pos


# Função para desenhar o tabuleiro
    def desenhar_tabuleiro(self, tabuleiro, sprite_agente, sprite_ouro, sprite_wumpus):

        # Calcular origem para centralizar o tabuleiro
        largura_tabuleiro = self.colunas * self.tamanho_celula
        altura_tabuleiro = self.linhas * self.tamanho_celula
        origem_x = (self.largura_janela - largura_tabuleiro) // 2
        origem_y = (self.altura_janela - altura_tabuleiro) // 2

        for i in range(self.linhas):
            for j in range(self.colunas):
                x = origem_x + j * self.tamanho_celula
                y = origem_y +i * self.tamanho_celula
                rect = self.pygame.Rect(x, y, self.tamanho_celula, self.tamanho_celula)
                self.pygame.draw.rect(self.janela, self.preto, rect, 2)

                valor = tabuleiro[i, j]
                if valor == 1:
                    self.janela.blit(sprite_agente, (x, y))
                elif valor == 2:
                    self.janela.blit(sprite_ouro, (x, y))
                elif valor == 3 or valor == 5:
                    self.janela.blit(sprite_wumpus, (x, y))
                elif valor == 4:
                    self.pygame.draw.rect(self.janela, self.preto, (
                        x + self.tamanho_celula // 4, y + self.tamanho_celula // 4, self.tamanho_celula // 2, self.tamanho_celula // 2))



# Função principal
    def jogar(self, labirinto, individuo):
        tabuleiro, jogador_pos, ouro_pos, wumpus_pos, poços_pos = self.inicializar_tabuleiro(labirinto)
        rodando = True
        venceu = False
        perdeu = False

        # Carregar sprites
        sprite_agente = pygame.image.load("G:/Meu Drive/Mestrado/2024.1/IA/mundo_de_wumpus/agente_algoritimo_genetico-v3/sprites/agente3.gif")
        sprite_ouro = pygame.image.load("G:/Meu Drive/Mestrado/2024.1/IA/mundo_de_wumpus/agente_algoritimo_genetico-v3/sprites/ouro.png")
        sprite_wumpus = pygame.image.load('G:/Meu Drive/Mestrado/2024.1/IA/mundo_de_wumpus/agente_algoritimo_genetico-v3/sprites/wumpus.gif')
        sprite_wumpus_morto = pygame.image.load('G:/Meu Drive/Mestrado/2024.1/IA/mundo_de_wumpus/agente_algoritimo_genetico-v3/sprites/wumpus_morto.png')
        sprite_mumia = pygame.image.load('G:/Meu Drive/Mestrado/2024.1/IA/mundo_de_wumpus/agente_algoritimo_genetico-v3/sprites/mumia.png')
        sprite_vencedor = pygame.image.load('G:/Meu Drive/Mestrado/2024.1/IA/mundo_de_wumpus/agente_algoritimo_genetico-v3/sprites/vencedo.png')
        #sprite_poco = pygame.image.load("poco.png")

        sprite_agente = pygame.transform.scale(sprite_agente, (self.tamanho_celula, self.tamanho_celula))
        sprite_ouro = pygame.transform.scale(sprite_ouro, (self.tamanho_celula, self.tamanho_celula))
        sprite_wumpus = pygame.transform.scale(sprite_wumpus, (self.tamanho_celula, self.tamanho_celula))
        sprite_wumpus_morto = pygame.transform.scale(sprite_wumpus_morto, (self.tamanho_celula, self.tamanho_celula))
        sprite_mumia = pygame.transform.scale(sprite_mumia, (self.tamanho_celula, self.tamanho_celula))
        sprite_vencedor = pygame.transform.scale(sprite_vencedor, (self.tamanho_celula, self.tamanho_celula))
        #sprite_poco = pygame.transform.scale(sprite_poco, (tamanho_celula, tamanho_celula))

        count = 0
        ouro = False
        wumpus_morto = False

        while rodando:
            for event in self.pygame.event.get():
                if event.type == self.pygame.QUIT:
                    rodando = False

            if count < len(individuo.genoma):
                if individuo.genoma[count] == 'L' and jogador_pos[1] > 0:
                    nova_pos = (jogador_pos[0], jogador_pos[1] - 1)
                elif individuo.genoma[count] == 'O' and jogador_pos[1] < self.colunas - 1:
                    nova_pos = (jogador_pos[0], jogador_pos[1] + 1)
                elif individuo.genoma[count] == 'S' and jogador_pos[0] > 0:
                    nova_pos = (jogador_pos[0] - 1, jogador_pos[1])
                elif individuo.genoma[count] == 'N' and jogador_pos[0] < self.linhas - 1:
                    nova_pos = (jogador_pos[0] + 1, jogador_pos[1])
                elif individuo.genoma[count] == 'ATN' and wumpus_morto == False:
                    if wumpus_pos == (jogador_pos[0]+1, jogador_pos[1]):
                        wumpus_morto = True
                        print(jogador_pos)
                elif individuo.genoma[count] == 'ATS' and wumpus_morto == False:
                    if wumpus_pos == (jogador_pos[0]-1, jogador_pos[1]):
                        wumpus_morto = True
                        print(jogador_pos)
                elif individuo.genoma[count] == 'ATO' and wumpus_morto == False:
                    if wumpus_pos == (jogador_pos[0], jogador_pos[1]+1):
                        wumpus_morto = True
                        print(jogador_pos)
                elif individuo.genoma[count] == 'ATL' and wumpus_morto == False:
                    if wumpus_pos == (jogador_pos[0], jogador_pos[1]-1):
                        wumpus_morto = True
                        print(jogador_pos)
                else:
                    nova_pos = jogador_pos
            if nova_pos != jogador_pos:
                tabuleiro[jogador_pos] = 0
                jogador_pos = nova_pos
                tabuleiro[jogador_pos] = 1
                if jogador_pos == ouro_pos:
                    ouro = True
                elif jogador_pos == (0,0) and ouro == True:
                    venceu = True
                    count = len(individuo.genoma)
                elif jogador_pos in poços_pos:
                    perdeu = True
                    count = len(individuo.genoma)
                elif jogador_pos == wumpus_pos  and wumpus_morto == False:
                    perdeu = True
                    count = len(individuo.genoma)
            elif wumpus_morto:
                tabuleiro[wumpus_pos] = 5

            self.janela.fill(self.branco)

            if perdeu:
                self.desenhar_tabuleiro(tabuleiro, sprite_mumia, sprite_ouro, sprite_wumpus)
            elif venceu and wumpus_morto:
                self.desenhar_tabuleiro(tabuleiro, sprite_vencedor, sprite_ouro, sprite_wumpus_morto)
            elif venceu:
                self.desenhar_tabuleiro(tabuleiro, sprite_vencedor, sprite_ouro, sprite_wumpus)
            elif wumpus_morto:
                self.desenhar_tabuleiro(tabuleiro, sprite_agente, sprite_ouro, sprite_wumpus_morto)
            else:
                self.desenhar_tabuleiro(tabuleiro, sprite_agente, sprite_ouro, sprite_wumpus)

            if individuo.vencedor and count > len(individuo.genoma):
                fonte = self.pygame.font.Font(None, 50)
                texto = fonte.render("Agente pegou o Ouro e Escapou!", True, self.verde)
                self.janela.blit(texto, (self.largura_janela // 2 - texto.get_width() // 2, self.altura_janela // 2 - texto.get_height() // 2))
            elif perdeu and count > len(individuo.genoma):
                fonte = self.pygame.font.Font(None, 50)
                texto = fonte.render("Agente Morreu!", True, self.vermelho)
                self.janela.blit(texto, (self.largura_janela // 2 - texto.get_width() // 2, self.altura_janela // 2 - texto.get_height() // 2))
            elif count > len(individuo.genoma):
                fonte = self.pygame.font.Font(None, 50)
                texto = fonte.render("Falha na missão, tente novamente!", True, self.vermelho)
                self.janela.blit(texto, (self.largura_janela // 2 - texto.get_width() // 2, self.altura_janela // 2 - texto.get_height() // 2))

            self.pygame.display.flip()
            time.sleep(0.5)
            count += 1

        self.pygame.quit()
        sys.exit()


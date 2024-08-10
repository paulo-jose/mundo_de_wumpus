import random
import os
import time

class Mundo:

    def __init__(self, tamanho_linhas, tamanho_colunas, wumpus):

        self.tamanho_linhas = tamanho_linhas
        self.tamanho_colunas = tamanho_colunas
        self.wumpus = wumpus
        self.matriz = []
        self.posicao_pocos = []

    def gerar_mundo(self):
        self.matriz = [["0" for _ in range(self.tamanho_colunas)] for _ in range(self.tamanho_linhas)]

    def inserir_elemento(self, elemento):

        while True:
            posicao_elemento = random.randint(0, self.tamanho_linhas - 1), random.randint(0, self.tamanho_colunas - 1)

            if posicao_elemento != (0, 0):
                item_atual = self.matriz[posicao_elemento[0]][posicao_elemento[1]]
                if elemento == "P":
                    if "P" not in item_atual and "W" not in item_atual and "O" not in item_atual and "B" not in item_atual:
                        if item_atual == "0":
                            self.matriz[posicao_elemento[0]][posicao_elemento[1]] = elemento
                            self.posicao_pocos = posicao_elemento  # Para ter a posição dos pocos
                        else:
                            self.matriz[posicao_elemento[0]][posicao_elemento[1]] += elemento
                        self.inserir_elementos_adjacentes("B", posicao_elemento)
                        break
                elif elemento == "W":
                    if "P" not in item_atual:
                        if item_atual == "0":
                            self.matriz[posicao_elemento[0]][posicao_elemento[1]] = elemento
                        else:
                            self.matriz[posicao_elemento[0]][posicao_elemento[1]] += elemento
                        self.posicao_wumpus = posicao_elemento

                        self.inserir_elementos_adjacentes("F", posicao_elemento)
                        break
                elif elemento == "O":
                    if "P" not in item_atual:
                        if item_atual == "0":
                            self.matriz[posicao_elemento[0]][posicao_elemento[1]] = elemento
                        else:
                            self.matriz[posicao_elemento[0]][posicao_elemento[1]] += elemento
                        self.posicao_ouro = posicao_elemento
                        break

    def inserir_elementos_adjacentes(self, tipo_de_item, posicao):
        linhas, colunas = self.tamanho_linhas, self.tamanho_colunas
        l, c = posicao
        adjacentes = [(l - 1, c), (l + 1, c), (l, c - 1), (l, c + 1)]

        for adj in adjacentes:
            if 0 <= adj[0] < linhas and 0 <= adj[1] < colunas:
                posicao_atual = self.matriz[adj[0]][adj[1]]
                if "P" in posicao_atual:
                    continue
                if tipo_de_item in posicao_atual:
                    continue
                if posicao_atual == "0":
                    self.matriz[adj[0]][adj[1]] = tipo_de_item
                else:
                    self.matriz[adj[0]][adj[1]] += tipo_de_item

    def inserir_pocos(self):
        numero_pocos = int((self.tamanho_linhas * self.tamanho_colunas) * 0.15)
        for _ in range(numero_pocos):
            self.inserir_elemento("P")

    def inserir_wumpus(self):
        self.inserir_elemento("W")

    def inserir_ouro(self):
        self.inserir_elemento("O")

    def inserir_agente(self):

        if self.matriz[0][0] != "0":
            self.matriz[0][0] += "A"
        else:
            self.matriz[0][0] = "A"

    def atualizacao_matriz(self, valor_orig_pos, pos_atual_agente, nova_pos, agente):
  
        if len(valor_orig_pos) > 1 and "A" in valor_orig_pos:

            self.matriz[pos_atual_agente[0]][pos_atual_agente[1]] = valor_orig_pos.replace("A", "")

            if self.matriz[nova_pos[0]][nova_pos[1]] == "0":
                self.matriz[nova_pos[0]][nova_pos[1]] = agente
            else:
                self.matriz[nova_pos[0]][nova_pos[1]] += agente
        else:
            self.matriz[pos_atual_agente[0]][pos_atual_agente[1]] = "0"

            if self.matriz[nova_pos[0]][nova_pos[1]] == "0":
                self.matriz[nova_pos[0]][nova_pos[1]] = agente
            else:
                self.matriz[nova_pos[0]][nova_pos[1]] += agente


    def ecoar_gritos_wumpus(self):

        for i in range(self.tamanho_linhas):
            for j in range(self.tamanho_colunas):
                if self.matriz[i][j] == "0":
                    self.matriz[i][j] = "G"
                else:
                    self.matriz[i][j] += "G"

    def imprimir_matriz(self, agente):

        for linha in self.matriz:
            nova_linha = []
            for elemento in linha:
                elemento_formatado = str(elemento).ljust(4)
                if "O" in elemento:
                    elemento_formatado = elemento_formatado.replace("O", "\033[1;33mO\033[0m")
                if "W" in elemento:
                    elemento_formatado = elemento_formatado.replace("W", "\033[1;35mW\033[0m")
                if "F" in elemento:
                    elemento_formatado = elemento_formatado.replace("F", "\033[1;32mF\033[0m")
                if "P" in elemento:
                    elemento_formatado = elemento_formatado.replace("P", "\033[1;31mP\033[0m")
                if "B" in elemento:
                    elemento_formatado = elemento_formatado.replace("B", "\033[1;34mB\033[0m")
                if "G" in elemento:
                    elemento_formatado = elemento_formatado.replace("G", "\033[5;38;5;46mG\033[0m")

                # Agente coletando ouro e mudando a cor para amarelo
                if "A" in elemento and agente.ouro_encontrado == False:
                    elemento_formatado = elemento_formatado.replace("A", "\033[1;36mA\033[0m")
                elif "A" in elemento and agente.ouro_encontrado == True:
                    elemento_formatado = elemento_formatado.replace("A", "\033[1;33mA\033[0m")

                nova_linha.append(elemento_formatado)
            print(" ".join(nova_linha))
        print("__________________________")
        time.sleep(1)
        os.system('clear')
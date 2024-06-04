import random
import os
import time


class Mundo:
    def __init__(self, tamanho_linhas, tamanho_colunas):
        self.tamanho_linhas = tamanho_linhas
        self.tamanho_colunas = tamanho_colunas
        self.matriz = []
        self.posicao_ouro = None
        self.posicao_wumpus = None


    def gerar_mundo(self):
        self.matriz = [["0" for _ in range(self.tamanho_colunas)] for _ in range(self.tamanho_linhas)]
        self.matriz[0][0] = "A"  # Posição inicial do agente

    def inserir_elemento(self, elemento):
        while True:
            posicao = random.randint(0, self.tamanho_linhas - 1), random.randint(0, self.tamanho_colunas - 1)

            if posicao != (0, 0):
                item_atual = self.matriz[posicao[0]][posicao[1]]
                if elemento == "P":
                    if "P" not in item_atual and "W" not in item_atual and "O" not in item_atual and "B" not in item_atual:
                        if item_atual == "0":
                            self.matriz[posicao[0]][posicao[1]] = elemento
                        else:
                            self.matriz[posicao[0]][posicao[1]] += elemento
                        self.inserir_elementos_adjacentes("B", posicao)
                        break
                elif elemento == "W":
                    if "P" not in item_atual:
                        if item_atual == "0":
                            self.matriz[posicao[0]][posicao[1]] = elemento
                        else:
                            self.matriz[posicao[0]][posicao[1]] += elemento
                        self.posicao_wumpus = posicao
                        self.inserir_elementos_adjacentes("F", posicao)
                        break
                elif elemento == "O":
                    if "P" not in item_atual:
                        if item_atual == "0":
                            self.matriz[posicao[0]][posicao[1]] = elemento
                        else:
                            self.matriz[posicao[0]][posicao[1]] += elemento
                        self.posicao_ouro = posicao
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
        numero_pocos = int((self.tamanho_linhas * self.tamanho_colunas) * 0.20)
        for _ in range(numero_pocos):
            self.inserir_elemento("P")

    def inserir_wumpus(self):
        self.inserir_elemento("W")
    
    def inserir_ouro(self):
        self.inserir_elemento("O")

    def imprimir_matriz(self):
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
                if "A" in elemento:
                    elemento_formatado = elemento_formatado.replace("A", "\033[1;36mA\033[0m")

                nova_linha.append(elemento_formatado)
            print(" ".join(nova_linha))
        time.sleep(0.3)
        os.system('clear')
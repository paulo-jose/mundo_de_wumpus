import os
import random
import time

class Labirinto:
    def __init__(self):
        self.tamanho = 0
        self.labirinto = None

    def criar_labirinto(self, tamanho):
        self.tamanho = tamanho
        if (tamanho > 0):
            self.labirinto = []
            for i in range(tamanho):
                linha = []
                for j in range(tamanho):
                    linha.append("?")
                self.labirinto.append(linha)
            return "Labirinto criado com sucesso"
        else:
            return "Tamanho do Labirinto tem que ser maior que 0"

    # def imprimir_labirinto(self):
    #     for i in range(len(self.labirinto)):
    #         print("")
    #         for j in range(len(self.labirinto[0])):
    #             print(self.labirinto[i][j], end=" ")


    def inserir_elementos(self):
        #inserir Agente


        #inserir Wumpus
        posicao_wumpus = random.randint(0, len(self.labirinto) - 1), random.randint(0, len(self.labirinto[0]) - 1)
        while posicao_wumpus == (0, 0):
            posicao_wumpus = random.randint(0, len(self.labirinto) - 1), random.randint(0, len(self.labirinto[0]) - 1)
        self.labirinto[posicao_wumpus[0]][posicao_wumpus[1]] = "W"

        #inserir Ouro
        posicao_ouro = random.randint(0, len(self.labirinto) - 1), random.randint(0, len(self.labirinto[0]) - 1)
        while (posicao_ouro == posicao_wumpus) or (posicao_ouro == (0, 0)):
            posicao_ouro = random.randint(0, len(self.labirinto) - 1), random.randint(0, len(self.labirinto[0]) - 1)
        self.labirinto[posicao_ouro[0]][posicao_ouro[1]] = "O"

        #inserir Poços
        numero_pocos = int((len(self.labirinto) * len(self.labirinto)) * 0.20)  # porcetagem de poços
        for i in range(numero_pocos):
            posicao_poco = random.randint(0, len(self.labirinto) - 1), random.randint(0, len(self.labirinto[0]) - 1)
            while ((posicao_poco == posicao_wumpus) or (posicao_poco == posicao_ouro) or (posicao_poco == (0, 0)) or
                   self.labirinto[posicao_poco[0]][posicao_poco[1]] == "P"):
                posicao_poco = random.randint(0, len(self.labirinto) - 1), random.randint(0, len(self.labirinto[0]) - 1)
            self.labirinto[posicao_poco[0]][posicao_poco[1]] = "P"



    def inserir_percepcao(self):
        tamanho_labirinto = len(self.labirinto)

        def adjacentes(x, y):
            adj = []
            if x > 0:
                adj.append((x - 1, y))
            if x < tamanho_labirinto - 1:
                adj.append((x + 1, y))
            if y > 0:
                adj.append((x, y - 1))
            if y < tamanho_labirinto - 1:
                adj.append((x, y + 1))
            return adj

        for i in range(tamanho_labirinto):
            for j in range(tamanho_labirinto):
                if self.labirinto[i][j] == "W":
                    for (x, y) in adjacentes(i, j):
                        if (self.labirinto[x][y] == "O"):
                            self.labirinto[x][y] = "OF"
                        elif (self.labirinto[x][y] == "P"):
                            self.labirinto[x][y] = "P"
                        elif (self.labirinto[x][y] == "OB"):
                            self.labirinto[x][y] = "OFB"
                        elif (self.labirinto[x][y] == "B"):
                            self.labirinto[x][y] = "FB"
                        else:
                            self.labirinto[x][y] = "F"
                elif self.labirinto[i][j] == "P":
                    for (x, y) in adjacentes(i, j):
                        if (self.labirinto[x][y] == "F"):
                            self.labirinto[x][y] = "FB"
                        elif (self.labirinto[x][y] == "O"):
                            self.labirinto[x][y] = "OB"
                        elif (self.labirinto[x][y] == "OF"):
                            self.labirinto[x][y] = "OFB"
                        elif (self.labirinto[x][y] == "W"):
                            self.labirinto[x][y] = "W"
                        elif (self.labirinto[x][y] == "P"):
                            self.labirinto[x][y] = "P"
                        else:
                            self.labirinto[x][y] = "B"


    def executar_genoma(self, genoma):
        x, y = self.encontrar_agente()

        ouro = False
        posicao_inicial = False
        print(f"Executar genoma...: {genoma} ")


        for direcao in genoma:
            if direcao == 'S' and x > 0:
                if x == 0 and y == 0 and self.labirinto[x][y] in "A":
                    self.labirinto[x][y] = self.labirinto[x][y].replace('A', "v")
                    x -= 1
                    self.labirinto[x][y] += "A"
                elif "?" in self.labirinto[x][y]:
                    self.labirinto[x][y] = self.labirinto[x][y].replace('?', "v")
                    self.labirinto[x][y] = self.labirinto[x][y].replace('A', "")
                    x -= 1
                    self.labirinto[x][y] += "A"
                else:
                    self.labirinto[x][y] = self.labirinto[x][y].replace('A', "")
                    x -= 1
                    self.labirinto[x][y] += "A"
            elif direcao == 'N' and x < len(self.labirinto) - 1:
                if x == 0 and y == 0 and self.labirinto[x][y] in "A":
                    self.labirinto[x][y] = self.labirinto[x][y].replace('A', "v")
                    x += 1
                    self.labirinto[x][y] += "A"
                elif "?" in self.labirinto[x][y]:
                    self.labirinto[x][y] = self.labirinto[x][y].replace('?', "v")
                    self.labirinto[x][y] = self.labirinto[x][y].replace('A', "")
                    x += 1
                    self.labirinto[x][y] += "A"
                else:
                    self.labirinto[x][y] = self.labirinto[x][y].replace('A', "")
                    x += 1
                    self.labirinto[x][y] += "A"
            elif direcao == 'L' and y > 0:
                if "?" in self.labirinto[x][y]:
                    self.labirinto[x][y] = self.labirinto[x][y].replace('?', "v")
                    self.labirinto[x][y] = self.labirinto[x][y].replace('A', "")
                    y -= 1
                    self.labirinto[x][y] += "A"
                else:
                    self.labirinto[x][y] = self.labirinto[x][y].replace('A', "")
                    y -= 1
                    self.labirinto[x][y] += "A"
            elif direcao == 'O' and y < len(self.labirinto) - 1:
                if x == 0 and y == 0 and self.labirinto[x][y] == "A":
                    self.labirinto[x][y] = self.labirinto[x][y].replace('A', "v")
                    y += 1
                    self.labirinto[x][y] += "A"
                elif "?" in self.labirinto[x][y]:
                    self.labirinto[x][y] = self.labirinto[x][y].replace('?', "v")
                    self.labirinto[x][y] = self.labirinto[x][y].replace('A', "")
                    y += 1
                    self.labirinto[x][y] += "A"
                else:
                    self.labirinto[x][y] = self.labirinto[x][y].replace('A', "")
                    y += 1
                    self.labirinto[x][y] += "A"

            self.imprimir_labirinto()

    def imprimir_labirinto(self):
        for linha in self.labirinto:
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
                if "R" in elemento:
                    elemento_formatado = elemento_formatado.replace("R", "\033[1;33mR\033[0m")
                else:
                    elemento_formatado = elemento_formatado.replace("?", "?")

                nova_linha.append(elemento_formatado)
            print(" ".join(nova_linha))
        time.sleep(0.3)
        print()


    def inserir_agente(self):
        # inserir agente
        if (self.labirinto[0][0] == "?"):
            self.labirinto[0][0] = "A"
        else:
            self.labirinto[0][0] += "A"

    def encontrar_agente(self):
        for i in range(len(self.labirinto)):
            for j in range(len(self.labirinto)):
                if "A" in self.labirinto[i][j]:
                    return i, j
        return None, None
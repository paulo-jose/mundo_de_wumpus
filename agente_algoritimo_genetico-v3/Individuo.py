import random
import copy
class Individuo:

    def __init__(self, genoma):
        self.id = None
        self.geracao = 0
        self.genoma = genoma
        self.pontuacao = 0
        self.flecha = 0
        self.wumpus_morto = False
        self.ouro = False
        self.vencedor = False
        self.perdedor = False
        self.campo = None


    def fitness(self, labirinto):

        x, y = labirinto.encontrar_agente()

        campo = copy.deepcopy(labirinto.labirinto)
        auxgenoma = copy.deepcopy(self.genoma)
        escape = False
        self.wumpus_morto = False
        self.flecha = 1
        count = 0
        posicao = 0

        for direcao in self.genoma:
            #verificar a percepeção de fendor
            if "F" in campo[x][y] and self.wumpus_morto == False and self.flecha > 0:
                # escolhe a direção da flecha
                if x == 0 and y == 0:
                    alvo = random.choice(["O", "N"])
                elif x == len(campo) - 1 and y == 0:
                    alvo = random.choice(["O", "S"])
                elif x == 0 and y == len(campo) - 1:
                    alvo = random.choice(["N", "L"])
                elif x == len(campo) - 1 and y == len(campo) - 1:
                    alvo = random.choice(["S", "L"])
                elif x == 0:
                    alvo = random.choice(["N", "L", "O"])
                elif x == len(campo) - 1:
                    alvo = random.choice(["N", "O", "L"])
                elif y == 0:
                    alvo = random.choice(["S", "L", "N"])
                else:
                    alvo = random.choice(["N", "S", "L", "O"])

                # verificar se acertou a flecha
                if alvo == 'N' and x > len(campo) - 1 and self.flecha > 0:
                    if campo[x + 1][y] == 'W':
                        self.wumpus_morto = True
                        auxgenoma.insert(count, "ATN")
                        self.pontuacao += 900
                        campo[x + 1][y] = 'Wm'
                    else:
                        auxgenoma.insert(count, "ATN")
                        self.pontuacao -= 10
                elif alvo == 'S':
                    if campo[x - 1][y] == 'W':
                        self.wumpus_morto = True
                        auxgenoma.insert(count, "ATS")
                        self.pontuacao += 900
                        campo[x - 1][y] = 'Wm'
                    else:
                        auxgenoma.insert(count, "ATS")
                        self.pontuacao -= 10
                elif alvo == 'O' and y > len(campo) - 1:
                    if campo[x][y + 1] == 'W':
                        self.wumpus_morto = True
                        auxgenoma.insert(count, "ATO")
                        self.pontuacao += 900
                        campo[x][y + 1] = 'Wm'
                    else:
                        auxgenoma.insert(count, "ATO")
                        self.pontuacao -= 10
                elif alvo == 'L':
                    if campo[x][y - 1] == 'W':
                        self.wumpus_morto = True
                        auxgenoma.insert(count, "ATL")
                        campo[x][y - 1] = 'Wm'
                        self.pontuacao += 900
                    else:
                        auxgenoma.insert(count, "ATL")
                        self.pontuacao -= 10

                self.flecha = 0



            if direcao == 'S' and x > 0:
                x -= 1
                self.pontuacao -= 1

            elif direcao == 'N' and x < len(campo) - 1:
                x += 1
                self.pontuacao -= 1

            elif direcao == 'L' and y > 0:
                y -= 1
                self.pontuacao -= 1

            elif direcao == 'O' and y < len(campo) - 1:
                y += 1
                self.pontuacao -= 1


            # penalidade por mover fora do mapa
            elif direcao == 'S' and x < 0:
                self.pontuacao -= 2
            elif direcao == 'N' and x > len(campo) - 1:
                self.pontuacao -= 2
            elif direcao == 'L' and y < 0:
                self.pontuacao -= 2
            elif direcao == 'O' and y > len(campo) - 1:
                self.pontuacao -= 2

            if ("O" in campo[x][y]) and self.ouro == False:
                self.pontuacao += 1000  # encontrou o ouro
                self.ouro = True

            elif campo[x][y] == "W" or "P" in campo[x][y]:
                self.pontuacao -= 1000  # caiu no poco ou devorado pelo wumpus
                self.perdedor = True
                break

            elif (x == 0 and y == 0) and self.ouro:
                self.pontuacao += 1000
                self.vencedor = True
                break

            if self.perdedor:
                break

            count +=1
        self.genoma = auxgenoma
        self.campo = campo





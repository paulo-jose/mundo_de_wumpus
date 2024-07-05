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
        self.vencedor = False
        self.perdedor = False

    def fitness(self, labirinto):

        x, y = labirinto.encontrar_agente()
        campo = copy.deepcopy(labirinto.labirinto)
        ouro = False
        escape = False
        self.wumpus_morto = False
        self.flecha = 1
        count = 0
        posicao = 0

        for direcao in self.genoma:
            #verificar a percepeção de vendor
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
                        self.genoma.insert(count, "ATN")
                        self.pontuacao += 1000
                        campo[x + 1][y] = 'Wm'
                    else:
                        self.genoma.insert(count, "ATN")
                        self.pontuacao -= 10
                elif alvo == 'S':
                    if campo[x - 1][y] == 'W':
                        self.wumpus_morto = True
                        self.genoma.insert(count, "ATS")
                        self.pontuacao += 1000
                        campo[x - 1][y] = 'Wm'
                    else:
                        self.genoma.insert(count, "ATS")
                        self.pontuacao -= 10
                elif alvo == 'O' and y > len(campo) - 1:
                    if campo[x][y + 1] == 'W':
                        self.wumpus_morto = True
                        self.genoma.insert(count, "ATO")
                        self.pontuacao += 1000
                        campo[x][y + 1] = 'Wm'
                    else:
                        self.genoma.insert(count, "ATO")
                        self.pontuacao -= 10
                elif alvo == 'L':
                    if campo[x][y - 1] == 'W':
                        self.genoma.insert(count, "ATL")
                        self.wumpus_morto = True
                        campo[x][y - 1] = 'Wm'
                        self.pontuacao += 1000
                    else:
                        self.genoma.insert(count, "ATL")
                        self.pontuacao -= 10

                self.flecha = 0



            if direcao == 'S' and x > 0:
                x -= 1
                self.pontuacao += 1
            elif direcao == 'N' and x < len(campo) - 1:
                x += 1
                self.pontuacao += 1
            elif direcao == 'L' and y > 0:
                y -= 1
                self.pontuacao += 1
            elif direcao == 'O' and y < len(campo) - 1:
                y += 1
                self.pontuacao += 1

            # penalidade por mover fora do mapa
            elif direcao == 'S' and x < 0:
                self.pontuacao -= 1
            elif direcao == 'N' and x > len(campo) - 1:
                self.pontuacao -= 1
            elif direcao == 'L' and y < 0:
                self.pontuacao -= 1
            elif direcao == 'O' and y > len(campo) - 1:
                self.pontuacao -= 1

            if ("O" in campo[x][y]) and ouro == False:
                self.pontuacao += 1000  # encontrou o ouro
                ouro = True

            elif campo[x][y] == "W" or campo[x][y] == "P":
                self.pontuacao -= 1000  # caiu no poco ou devorado pelo wumpus
                self.perdedor = True

            elif (x == 0 and y == 0) and ouro:
                self.pontuacao += 100
                self.vencedor = True
                break

            count +=1







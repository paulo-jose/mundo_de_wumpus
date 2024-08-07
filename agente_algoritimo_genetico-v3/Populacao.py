import random
from Individuo import Individuo


class Populacao:
    def __init__(self, tm_populacao, tm_genoma):
        self.tm_populacao = tm_populacao
        self.tm_genoma = tm_genoma
        self.individuos = []
        self.melhor_individuo = None

    def criar_genoma(self):
        return [random.choice(["S", "N", "L", "O"]) for _ in range(random.randint(16, self.tm_genoma+1))]

    def criar_individuos(self, labirinto):
        cout = 0
        while len(self.individuos) < self.tm_populacao:
            individuo = Individuo(self.criar_genoma())
            individuo.fitness(labirinto)
            if individuo.pontuacao >= 0:
                individuo.id = cout
                individuo.geracao = 1
                self.individuos.append(individuo)
            cout += 1
        return self.individuos

    def add_individuos(self, genoma, id, geracao):
        ind = Individuo(genoma)
        ind.id = id
        ind.geracao = geracao
        self.individuos.append(ind)

    def melhor_genoma(self):
        self.melhor_individuo = self.individuos[0]
        maior = self.individuos[0].pontuacao
        for individuo in self.individuos:
            if maior < individuo.pontuacao:
                maior = individuo.pontuacao
                self.melhor_individuo = individuo

        return self.melhor_individuo

    def pior_genoma(self):
        pior_individuo = self.individuos[0]
        menor = self.individuos[0].pontuacao
        for individuo in self.individuos:
            if menor > individuo.pontuacao:
                menor = individuo.pontuacao
                pior_individuo = individuo

        return pior_individuo

    def media_genoma(self):
        pontuacoes = []
        for i in self.individuos:
            pontuacoes.append(i.pontuacao)
        soma = sum(pontuacoes)
        qtd = len(self.individuos)
        media = soma/qtd
        return media





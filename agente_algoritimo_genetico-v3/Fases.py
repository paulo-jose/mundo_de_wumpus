import random
from Individuo import Individuo


class Fases:

    @staticmethod
    def selecao_pares(populacao, pontuacoes):
        return random.choices(populacao.individuos, weights=None, k=2)

    @staticmethod
    def cruzamento(pai1, pai2, tm_genoma, geracao):

        ponto = random.randint(1, tm_genoma - 1)
        filho1 = Individuo(pai1.genoma[:ponto] + pai2.genoma[ponto:])
        filho2 = Individuo(pai2.genoma[:ponto] + pai1.genoma[ponto:])
        filho1.id = f'{pai1.id}.{geracao}'
        filho2.id = f'{pai2.id}.{geracao}'
        filho1.geracao = geracao
        filho2.geracao = geracao
        return filho1, filho2

    @staticmethod
    def crossover(pai1, pai2, n_cortes, tm_genoma,  geracao):

        if n_cortes < 2:
            n_cortes = 2
        if n_cortes > tm_genoma - 1:
            n_cortes = tm_genoma - 1

        cut_points = sorted(random.sample(range(1, tm_genoma), n_cortes))
        filho1, filho2 = [], []

        segemento1, segemento2 = [], []
        start = 0
        for cut in cut_points:
            segemento1.append(pai1.genoma[start:cut])
            segemento2.append(pai2.genoma[start:cut])
            start = cut
        segemento1.append(pai1.genoma[start:])
        segemento2.append(pai2.genoma[start:])

        for i in range(len(segemento1)):
            if i % 2 == 0:
                filho1.extend(segemento1[i])
                filho2.extend(segemento2[i])
            else:
                filho1.extend(segemento2[i])
                filho2.extend(segemento1[i])

        filho1 = Individuo(filho1)
        filho2 = Individuo(filho2)
        filho1.id = f'{pai1.id}.{geracao}'
        filho2.id = f'{pai2.id}.{geracao}'
        filho1.geracao = geracao
        filho2.geracao = geracao

        return filho1, filho2



    @staticmethod
    def mutacao(genoma, TX_MUTACAO, DIRECAO):
        for i in range(len(genoma)):
            if random.random() < TX_MUTACAO:
                genoma[i] = random.choice(DIRECAO)
        return genoma

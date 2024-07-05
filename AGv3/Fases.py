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

    def crossover(pai1, pai2, n_cortes, geracao):
        # Selecionar posições de corte aleatórias
        cortes = random.sample(range(1, len(pai1.genoma)), n_cortes)

        # Inicializar descendente vazio
        genoma = []

        # Alternar entre os genes dos pais em cada posição de corte
        i_pai1 = 0
        i_pai2 = 0
        for corte in sorted(cortes):
            while i_pai1 < corte:
                genoma.append(pai1.genoma[i_pai1])
                i_pai1 += 1

            while i_pai2 < corte:
                genoma.append(pai2.genoma[i_pai2])
                i_pai2 += 1

        # Adicionar os genes restantes do último pai
        if i_pai1 < len(pai1.genoma):
            genoma.extend(pai1.genoma[i_pai1:])
        elif i_pai2 < len(pai2):
            genoma.extend(pai2.genoma[i_pai2:])

        filho = Individuo(genoma)
        filho.id = f'{pai1.id}.{geracao}'
        filho.geracao = geracao

        return filho


    @staticmethod
    def mutacao(genoma, TX_MUTACAO, DIRECAO):
        for i in range(len(genoma)):
            if random.random() < TX_MUTACAO:
                genoma[i] = random.choice(DIRECAO)
        return genoma

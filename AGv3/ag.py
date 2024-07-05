import copy
from Fases import Fases
from Labirinto import Labirinto
from Populacao import Populacao
import matplotlib.pyplot as plt
from Tela import Tela
import numpy as np


TM_POPULACAO = 50
DIRECAO = ["S", "N", "L", "O"]
TX_CRUZAMENTO = 0.85
TX_MUTACAO = 0.05
GERACAO = 1000
tm_matriz = int(input("Qual o tamanho da matriz?  "))
TM_MXGENOMA = int((tm_matriz * tm_matriz) * 0.80)
labirinto = Labirinto()

labirinto.criar_labirinto(tm_matriz)
labirinto.imprimir_labirinto()
print()
labirinto.inserir_elementos()
labirinto.imprimir_labirinto()
print()
labirinto.inserir_percepcao()
labirinto.inserir_agente()
labirinto.imprimir_labirinto()
print()
print()

populacao = Populacao(TM_POPULACAO, TM_MXGENOMA)
populacao.criar_individuos(labirinto)

print("-----------------------ORIGINAL---------------------------")
for i in populacao.individuos:
    i.fitness(labirinto)
    print(i.id, i.geracao, i.genoma, i.pontuacao)

geracao = 0
melhores_individuo = []
interacao = []


while True:
    nova_populacao = Populacao(TM_POPULACAO, TM_MXGENOMA)
    for _ in range(TM_POPULACAO // 2):
        if geracao == 0:
            pai1, pai2 = Fases.selecao_pares(populacao, None)
            filho1, filho2 = Fases.cruzamento(pai1, pai2, TM_MXGENOMA, 0)
            nova_populacao.add_individuos(Fases.mutacao(filho1.genoma, TX_MUTACAO, DIRECAO), filho1.id, filho1.geracao)
            nova_populacao.add_individuos(Fases.mutacao(filho2.genoma, TX_MUTACAO, DIRECAO), filho2.id, filho2.geracao)
        else:
            pai1, pai2 = Fases.selecao_pares(populacao, 0)
            filho1, filho2 = Fases.cruzamento(pai1, pai2, TM_MXGENOMA, geracao)
            nova_populacao.add_individuos(Fases.mutacao(filho1.genoma, TX_MUTACAO, DIRECAO), filho1.id, filho1.geracao)
            nova_populacao.add_individuos(Fases.mutacao(filho2.genoma, TX_MUTACAO, DIRECAO), filho2.id, filho2.geracao)

    for i in nova_populacao.individuos:
        i.pontuacao = 0
        i.fitness(labirinto)
        if i.perdedor:
            nova_populacao.individuos.remove(i)

    nova_populacao.individuos.sort(key=lambda individuo: individuo.pontuacao)

    print()
    print("-----------------------NOVA POPULAÇÃO---------------------------")
    for i in nova_populacao.individuos:
        print("Id:", i.id)
        print("Geração: ", i.geracao)
        print(i.genoma, i.pontuacao)



    populacao = nova_populacao

    melhores_individuo.append(populacao.melhor_genoma())
    interacao.append(geracao)


    geracao += 1

    if (geracao >= GERACAO):
        break

melhorgenoma = []

for i in melhores_individuo:
    melhorgenoma.append(i.pontuacao)

melhor_individuo = max(melhores_individuo, key=lambda individuo: individuo.pontuacao)

print("ID:", melhor_individuo.id)
print("Executar genoma:", melhor_individuo.genoma)
print("Pontuação:", melhor_individuo.pontuacao)
print("Wumpus Morto:", melhor_individuo.wumpus_morto)

#labirinto.executar_genoma(melhor_individuo.genoma)
if melhor_individuo.vencedor:
    print("O Agente conseguiu pegar o Ouro e voltar para casa 0,0")

labirinto.imprimir_labirinto()
tela = Tela(tm_matriz, tm_matriz)
tela.jogar(labirinto.labirinto, melhor_individuo)

# plt.plot(interacao, melhorgenoma)
# plt.xlabel("Geração")
# plt.ylabel("Melhor Individuo")
# plt.show()


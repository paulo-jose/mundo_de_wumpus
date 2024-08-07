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
tm_matriz = int(input("Qual o tamanho da matriz? "))
TM_MXGENOMA = int((tm_matriz * tm_matriz) * 0.95)
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
tx_cruzamento = int(TM_POPULACAO*TX_CRUZAMENTO)

print("-----------------------ORIGINAL---------------------------")
# for i in populacao.individuos:
#     i.fitness(labirinto)
#     print(i.id, i.geracao, i.genoma, i.pontuacao)

geracao = 0
melhores_individuo = []
media_individuos = []
piores_individuos = []
interacao = []

while True:
    nova_populacao = Populacao(TM_POPULACAO, TM_MXGENOMA)
    cruzamento = 0
    for _ in range(TM_POPULACAO // 2):
        pai1, pai2 = Fases.selecao_pares(populacao, None)
        if cruzamento < tx_cruzamento:
            #filho1, filho2 = Fases.cruzamento(pai1, pai2, TM_MXGENOMA, 0)
            filho1, filho2 = Fases.crossover(pai1, pai2, 3, len(pai1.genoma),  geracao)
            nova_populacao.add_individuos(Fases.mutacao(filho1.genoma, TX_MUTACAO, DIRECAO), filho1.id, filho1.geracao)
            nova_populacao.add_individuos(Fases.mutacao(filho2.genoma, TX_MUTACAO, DIRECAO), filho2.id, filho2.geracao)
        else:
            nova_populacao.add_individuos(Fases.mutacao(pai1.genoma, TX_MUTACAO, DIRECAO), pai1.id, pai1.geracao)
            nova_populacao.add_individuos(Fases.mutacao(pai2.genoma, TX_MUTACAO, DIRECAO), pai2.id, pai2.geracao)
        cruzamento += 1


    # retirada dos perdedores
    for i in nova_populacao.individuos:
        i.pontuacao = 0
        i.fitness(labirinto)
        if i.perdedor:
            nova_populacao.individuos.remove(i)
        print("Id: ", i.id)
        print("Geracao: ", i.geracao)
        print("Genoma: ", i.genoma)
        print("Pontuação: ", i.pontuacao)
        print()


    nova_populacao.individuos.sort(key=lambda individuo: individuo.pontuacao)
    populacao = nova_populacao
    melhores_individuo.append(populacao.melhor_genoma())
    piores_individuos.append(populacao.pior_genoma())
    media_individuos.append(populacao.media_genoma())
    interacao.append(geracao)

    geracao += 1

    if (geracao >= GERACAO):
        break

melhor_genoma = []
piores_genoma = []


for i in melhores_individuo:
    melhor_genoma.append(i.pontuacao)

for i in piores_individuos:
    piores_genoma.append(i.pontuacao)

melhor_individuo = max(melhores_individuo, key=lambda individuo: individuo.pontuacao)

print("ID:", melhor_individuo.id)
print("Geração:", melhor_individuo.geracao)
print("Executar genoma:", melhor_individuo.genoma)
print("Pontuação:", melhor_individuo.pontuacao)
print("Wumpus Morto:", melhor_individuo.wumpus_morto)
print("Ouro:", melhor_individuo.ouro)
print("Quantidade de Passos:", melhor_individuo.passos)

# labirinto.executar_genoma(melhor_individuo.genoma)
if melhor_individuo.vencedor:
    print("O Agente conseguiu pegar o Ouro e voltar para casa 0,0")


print()
labirinto.imprimir_labirinto()
print()
# for linha in melhor_individuo.campo:
#     print(' '.join(str(celula) for celula in linha))


tela = Tela(tm_matriz, tm_matriz)
tela.jogar(labirinto.labirinto_inicial, melhor_individuo)

plt.plot(interacao, melhor_genoma, label='Melhores Individuos')
plt.plot(interacao, piores_genoma, label='Piores Individuos')
plt.plot(interacao, media_individuos, label='Media Individuos')
plt.suptitle('Potuação por Geração')
plt.xlabel("Geração")
plt.ylabel("Pontuação")
plt.legend()
plt.show()


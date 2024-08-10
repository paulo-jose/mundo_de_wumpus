from gerador_de_mundov1 import Mundo
from agentev1 import Agente
from wumpus_v1 import Wumpus
from pontuacao import Pontuacao 

pontuacao_geracoes = []

for _ in range(20):

    # tm_mundo = int(input("Qual o tamanho do mundo de wumpus?  "))
    tm_mundo = 3

    wumpus = Wumpus()
    mundo = Mundo(tm_mundo, tm_mundo, wumpus)
    pontuacao = Pontuacao()
    agente = Agente(mundo, pontuacao)

    mundo.gerar_mundo()
    mundo.inserir_pocos()
    mundo.inserir_wumpus()
    mundo.inserir_ouro()
    mundo.inserir_agente()
    mundo.imprimir_matriz(agente)


    while agente.vivo:
        agente.mover()
    print("O Agente encontrou o ouro e Voltou para Casa! Fim")
    print('Pontuação final: ', pontuacao.pontos)

    pontuacao_geracoes.append(pontuacao.pontos)

for i in pontuacao_geracoes:
    print(i)

    
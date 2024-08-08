from gerador_de_mundo import Mundo
from agente import Agente
from wumpus import Wumpus
from caderno import Caderno
from pontuacao import Pontuacao


pontuacao_geracoes = []
qnt_mortes_wumpus = []

for i in range(20):

    tm_mundo = 4

    wumpus = Wumpus()
    mundo = Mundo(tm_mundo, tm_mundo, wumpus)
    caderno = Caderno()
    pontuacao = Pontuacao()
    agente = Agente(mundo, caderno, pontuacao)
    mundo.gerar_mundo()
    mundo.inserir_pocos()
    mundo.inserir_wumpus()
    mundo.inserir_ouro()
    mundo.inserir_agente()
    mundo.imprimir_matriz(agente)


    agente.sensor()

    while agente.vivo:
        agente.hunt_wumpus()
        agente.mover()
        if agente.ouro_encontrado and agente.posicao_atual == (0, 0):
            break
    
    pontuacao_geracoes.append(pontuacao.pontos)
    qnt_mortes_wumpus.append(pontuacao.qnt_mortes_wumpus)

soma = 0
for i in pontuacao_geracoes:
    soma += i
    print(i)

print(soma/50)
print('mortes wumpus',qnt_mortes_wumpus)
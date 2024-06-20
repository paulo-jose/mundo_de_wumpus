from gerador_de_mundov1 import Mundo
from agentev1 import Agente
from wumpus_v1 import Wumpus

def iniciar_jogo(tm_mundo):

    wumpus = Wumpus()
    mundo = Mundo(tm_mundo, tm_mundo, wumpus)
    agente = Agente(mundo)

    mundo.gerar_mundo()
    mundo.inserir_pocos()
    mundo.inserir_wumpus()
    mundo.inserir_ouro()
    mundo.inserir_agente()
    mundo.imprimir_matriz(agente)


    while agente.verificar_objetivo() == False:
        agente.mover()
    print("O Agente encontrou o ouro e Voltou para Casa! Fim")

tm_mundo = int(input("Qual o tamanho do mundo de wumpus?  "))
iniciar_jogo(tm_mundo)
    
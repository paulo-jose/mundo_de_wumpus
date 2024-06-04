from gerador_de_mundo import Mundo
from agente import Agente

def iniciar_jogo(tm_mundo):
    mundo = Mundo(tm_mundo, tm_mundo)
    mundo.gerar_mundo()
    mundo.inserir_pocos()
    mundo.inserir_wumpus()
    mundo.inserir_ouro()
    mundo.imprimir_matriz()

    agente = Agente(mundo)
    while agente.verificar_objetivo() == False:
        agente.mover()
    

tm_mundo = int(input("Qual o tamanho do mundo de wumpus?  "))
iniciar_jogo(tm_mundo)

print("O Agente encontrou o ouro e Voltou para Casa! Fim")
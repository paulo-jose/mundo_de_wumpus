from gerador_de_mundo import Mundo
from agente import Agente
from wumpus import Wumpus
from caderno import Caderno


tm_mundo = int(input("Qual o tamanho do mundo de wumpus?  "))

wumpus = Wumpus()
mundo = Mundo(tm_mundo, tm_mundo, wumpus)
caderno = Caderno()
agente = Agente(mundo, caderno)
mundo.gerar_mundo()
mundo.inserir_pocos()
mundo.inserir_wumpus()
mundo.inserir_ouro()
mundo.inserir_agente()
mundo.imprimir_matriz(agente)


agente.sensor()

while not agente.ouro_encontrado:
    agente.mover()
print("O Agente encontrou o ouro e Voltou para Casa! Fim")
   
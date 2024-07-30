import numpy as np

# Tamanho do mundo
n = 4

# Inicialização das probabilidades
P_Wumpus = np.full((n, n), 1 / (n*n))
P_Poço = np.full((n, n), 0.2)  # Exemplo de probabilidade de poço em cada célula
P_Segura = 1 - P_Wumpus - P_Poço

# Função de atualização de probabilidade com Bayes
def atualizar_probabilidade(celula, evidência, P_Wumpus, P_Poço, P_Segura):
    i, j = celula
    if evidência == "fedor":
        P_Wumpus[i,j] = (P_Wumpus[i,j] * 0.8) / (P_Wumpus[i,j] * 0.8 + (1 - P_Wumpus[i,j]) * 0.2)
    elif evidência == "brisa":
        P_Poço[i,j] = (P_Poço[i,j] * 0.8) / (P_Poço[i,j] * 0.8 + (1 - P_Poço[i,j]) * 0.2)
    P_Segura[i,j] = 1 - P_Wumpus[i,j] - P_Poço[i,j]

# Exemplo de percepção de evidência e atualização de probabilidades
evidências = [("fedor", (1,1)), ("brisa", (1,2))]

for evidência, celula in evidências:
    atualizar_probabilidade(celula, evidência, P_Wumpus, P_Poço, P_Segura)

# Decidir movimento baseado nas probabilidades
movimento_seguro = np.unravel_index(np.argmax(P_Segura), P_Segura.shape)
print(f"Movimento sugerido: {movimento_seguro}")

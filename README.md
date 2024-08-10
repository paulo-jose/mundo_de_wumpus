
# Mundo de Wumpus

## Descrição do Problema

O mundo de Wumpus é um problema clássico em inteligência artificial que desafia o desenvolvimento de agentes capazes de operar em ambientes parcialmente observáveis e perigosos. O objetivo do agente é encontrar um pedaço de ouro e retornar à sua posição inicial, evitando perigos como poços e o Wumpus.

## Funcionamento do Mundo de Wumpus

### Estrutura do Mundo

- **Matriz 4x4**: O mundo é uma grade de 4x4, composta por 16 células. Cada célula pode conter ouro, um poço, o Wumpus, ou estar vazia.
- **Ouro**: Localizado em uma célula aleatória, o ouro é o principal objetivo do agente.
- **Poços**: Aproximadamente 15% das células contêm poços, que são fatais. O agente sente uma brisa nas células adjacentes.
- **Wumpus**: Uma criatura que emite um fedor nas células adjacentes. O agente pode usar uma flecha para matá-lo.

### Regras de Movimento e Percepção

- **Movimento**: O agente pode mover-se para o norte, sul, leste ou oeste.
- **Percepções**: 
  - **Fedor**: Indica proximidade do Wumpus.
  - **Brisa**: Indica proximidade de um poço.
- **Arma**: Uma única flecha para eliminar o Wumpus (Quantidade = 1).

## Detalhamento do Projeto

### Detalhes da implementação do Agente v2
[Heurísticas definidas para mundo de wumpus v2](/agente_reativo-v2/heuristicas.md)
[POMDPs e A* mundo de Wumpus v2](/agente_reativo-v2/readme.md)



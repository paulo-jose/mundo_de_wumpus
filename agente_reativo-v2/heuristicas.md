# Heurísticas do Mundo de Wumpus

## Heurística 1 (HR 1)
### Se uma casa não possui percepção de perigo, então todas as casas adjacentes são seguras.
- **Explicação**: Quando um agente se encontra em uma casa sem sinais de perigo (como o cheiro do Wumpus ou a presença de um poço), isso indica que as casas adjacentes não contêm perigos. Essa heurística é fundamental para a exploração segura do ambiente, permitindo que o agente maximize sua mobilidade e minimize riscos.

## Heurística 2 (HR 2)
### Se não houver posições seguras disponíveis, então o agente deve ir em busca do Wumpus.
- **Explicação**: Em situações em que todas as casas conhecidas são consideradas perigosas, o agente deve mudar sua estratégia. Essa heurística sugere que, ao não haver opções seguras, o melhor caminho é confrontar o Wumpus diretamente. É uma abordagem arriscada, mas necessária em cenários críticos.

## Heurística 3 (HR 3)
### O agente deve arriscar-se somente depois de ter visitado todas as posições seguras e tentado matar o Wumpus.
- **Explicação**: Antes de tomar decisões arriscadas, o agente deve explorar todas as casas seguras disponíveis. Esta heurística prioriza a segurança e a coleta de informações, garantindo que o agente maximize suas chances de sobrevivência e sucesso antes de se expor a perigos.

## Diagrama de Heurísticas

```mermaid
graph TD;
    A[Início] --> B{Casa sem percepção de perigo?}
    B -- Sim --> C[Marcar casas adjacentes como seguras]
    B -- Não --> D{Posições seguras disponíveis?}
    D -- Não --> E[Ir em busca do Wumpus]
    D -- Sim --> F[Explorar casas seguras]
    F --> G{Tentou matar o Wumpus?}
    G -- Não --> H[Continuar explorando]
    G -- Sim --> I[Arriscar-se]
    I --> J[Fim]


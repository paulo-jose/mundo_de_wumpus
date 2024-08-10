# Mundo de Wumpus (v2): Implementação com POMDPs e A*

## Implementação com POMDPs

### O que são POMDPs?

Um processo de decisão de Markov parcialmente observável **(POMDP) é uma generalização de um processo de decisão de Markov (MDP)**. Um POMDP modela um processo de decisão do agente no qual se assume que a dinâmica do sistema é determinada por um MDP, mas **o agente não pode observar diretamente o estado subjacente**. Em vez disso, ele deve manter um modelo de sensor (a distribuição de probabilidade de diferentes observações dada o estado subjacente) e o MDP subjacente.

Ao contrário da função de política em MDP que mapeia os estados subjacentes para as ações, **a política do POMDP é um mapeamento do histórico de observações (ou estados de crença) para as ações**. O framework de POMDP é geral o suficiente para modelar uma variedade de processos de decisão sequenciais do mundo real.

**Notas**: [O framework geral de processos de decisão de Markov com informação imperfeita foi descrito por Karl Johan Åström em 1965 no caso de um espaço de estados discretos, e foi estudado na comunidade de pesquisa operacional onde o acrônimo POMDP foi cunhado. Posteriormente, foi adaptado para problemas em inteligência artificial e planejamento automatizado por Leslie P. Kaelbling e Michael L. Littman](https://en.wikipedia.org/wiki/Partially_observable_Markov_decision_process).

**Em resumo**: Uma solução exata para um POMDP fornece a ação ótima para cada crença possível sobre os estados do mundo. **A ação ideal maximiza a recompensa esperada (ou minimiza o custo) do agente ao longo de um horizonte possivelmente infinito**. A sequência de ações ótimas é conhecida como a **política ótima** do agente para interagir com seu ambiente.

Um POMDP de tempo discreto modela a relação entre um agente e seu ambiente. Formalmente, um POMDP é uma tupla de 7 elementos (S, A, T, R, Ω, O, γ), onde:
- **_S_** é um conjunto de estados
- **_A_** é um conjunto de ações
- **_T_** é um conjunto de probabilidades condicionais de transição entre estados
- **_R_**: **_S x A :left_right_arrow: R_** é a função de recompensa.
- **_Ω_** é um conjunto de observações
- **_O_** é um conjunto de probabilidades condicionais de observação e
- **_γ_** ∈ [0, 1) é o fator de desconto.

### Cálculo em POMDPs

1. **Função de Valor**: O objetivo é maximizar a função de valor \( V(b) \), onde \( b \) é uma crença sobre o estado do mundo. A função de valor é calculada iterativamente usando:

$$
V(b) = \max_{a \in A} \left[ R(b, a) + \gamma \sum_{o \in O} P(o | b, a) V(b') \right]
$$

onde \( \gamma \) é o fator de desconto, \( P(o | b, a) \) é a probabilidade de observação \( o \) dada a crença \( b \) e ação \( a \), e \( b' \) é a crença atualizada após a ação e observação.

2. **Atualização de Crença**: Após cada ação e observação, a crença do agente sobre o estado do mundo é atualizada usando:

$$
b'(s') = \eta \cdot Z(o | s', a) \sum_{s \in S} T(s' | s, a) b(s)
$$

onde \( \eta \) é uma constante de normalização.

## Algoritmo A*

### O que é o Algoritmo A*?

O algoritmo A* é um algoritmo de busca de caminho que é amplamente utilizado em inteligência artificial para encontrar o caminho mais curto entre dois pontos. Ele é particularmente útil em ambientes onde o caminho ideal pode não ser imediatamente óbvio devido a obstáculos ou outros fatores.

### Funcionamento do Algoritmo A*

O algoritmo A* utiliza uma função de custo \( f(n) \) que é a soma de duas componentes:

- **\( g(n) \)**: O custo do caminho desde o nó inicial até o nó \( n \).
- **\( h(n) \)**: Uma heurística que estima o custo do caminho do nó \( n \) até o nó objetivo.

A função de custo é dada por:

$$
f(n) = g(n) + h(n)
$$

#### Heurísticas Admissíveis e Consistentes

No contexto do Mundo de Wumpus, é crucial escolher uma heurística adequada para o algoritmo A*. A distância de Manhattan é uma escolha comum, mas pode ser complementada por informações adicionais do POMDP, como a probabilidade de encontrar perigos em células específicas. Isso torna o planejamento mais robusto e adaptado às condições incertas do ambiente.

#### Otimizações e Implementações (Trabalhos futuros)

O A* pode ser otimizado usando técnicas como a poda alfa-beta para reduzir o espaço de busca ou algoritmos de caminho reverso que planejam do objetivo ao início, aproveitando melhor a estrutura do problema. Além disso, implementações eficientes em estruturas de dados adequadas, como filas de prioridade, podem melhorar o desempenho do algoritmo nesse projeto.

### Exemplos e Simulações

#### Simulação de Cenários

Para ilustrar a integração de POMDPs e A*, considere a simulação de diferentes cenários no Mundo de Wumpus:

1.  **Cenário Inicial**: O agente começa na posição (1,1) e sente uma brisa. A função de crença é atualizada para refletir a alta probabilidade de um poço em uma das células adjacentes (2,1) ou (1,2).
    
2.  **Planejamento com A***: O A* calcula um caminho para o ouro, minimizando a exposição a células adjacentes a possíveis poços. Se o agente move-se para (2,1) e não cai em um poço, a crença é atualizada, reduzindo a probabilidade de poço nessa célula.
    
3.  **Adaptação Contínua**: Conforme o agente avança e faz novas observações, o POMDP reavalia as probabilidades de perigos nas células não visitadas. O A* recalcula o caminho conforme necessário, considerando as novas crenças.

### Overview POMDPs e A* no Mundo de Wumpus

- **Movimentação do Agente**: O agente usa POMDPs para planejar movimentos baseados em percepções de brisa e fedor, atualizando suas crenças sobre a localização de poços e do Wumpus e utiliza A* para se movimentar.
- **Inferência de Poços**: Com base nas percepções de brisa, o agente ajusta suas crenças probabilísticas sobre onde os poços podem estar localizados.
- **Tomada de Decisões**: As decisões são guiadas por heurísticas integradas ao modelo POMDP, que ajudam o agente a otimizar seu caminho e maximizar a pontuação.
- **Gestão de Crenças**: O agente mantém uma crença probabilística sobre a localização de poços e do Wumpus, atualizando-a conforme recebe novas percepções. Essa crença é utilizada para ajustar o custo \( g(n) \) no algoritmo A*.

- **Planejamento de Caminho**: Com base nas crenças, o algoritmo A* é usado para planejar um caminho seguro e eficiente para o ouro e de volta à posição inicial. O custo \( g(n) \) é ajustado para evitar áreas de alto risco (baseado nas crenças de onde os poços e o Wumpus podem estar).

- **Decisões Dinâmicas**: Conforme o agente se move e recebe novas percepções, ele reavalia suas crenças e recalcula o caminho usando A*. Isso permite que o agente se adapte a novas informações e evite perigos inesperados.

#### Componentes Detalhados de POMDPs

Além dos componentes principais, cada elemento do POMDP pode ser expandido para maior clareza:

-   **Estados (S)**: Em um POMDP aplicado ao Mundo de Wumpus, os estados podem incluir a posição do agente, a localização potencial do Wumpus, a presença de poços e a localização do ouro. A cada movimento, o agente deve considerar múltiplas possíveis configurações do mundo.
    
-   **Ações (A)**: As ações do agente incluem mover-se nas quatro direções cardinais, pegar o ouro, atirar uma flecha para tentar matar o Wumpus e sair da caverna. Cada ação tem consequências que afetam a crença do agente sobre o estado do mundo.
    
-   **Transições de Estado (T)**: As transições de estado representam a incerteza sobre como o mundo muda com cada ação. Por exemplo, ao mover-se para uma nova célula, o agente pode acabar em um poço, encontrar o Wumpus ou simplesmente mover-se sem incidentes. As probabilidades dessas transições são capturadas pela função de transição.
    
-   **Observações (O)**: As observações incluem sinais como brisas (indicando poços nas células adjacentes), odores (indicando a proximidade do Wumpus) e brilho (indicando a proximidade do ouro). Essas observações são parciais e sujeitas a ruído.
    
-   **Função de Observação (Z)**: A função de observação modela a probabilidade de uma determinada observação ser feita a partir de um estado específico. Por exemplo, a probabilidade de sentir uma brisa é alta se há um poço nas proximidades, mas pode não ser certa.
    
-   **Recompensas (R)**: As recompensas são atribuídas com base nas ações e estados resultantes. Encontrar ouro e sair da caverna com vida dá uma recompensa alta, enquanto cair em um poço ou encontrar o Wumpus resulta em uma penalidade significativa.

## Sistema de Pontuação

A avaliação do agente é baseada em um sistema de pontuação que incentiva a eficiência e segurança:

- **Cada Passo**: -1 ponto, incentivando a eficiência.
- **Cair em um Poço ou Morrer para o Wumpus**: -1000 pontos, penalizando severamente erros fatais.
- **Matar o Wumpus**: +1000 pontos, recompensando a eliminação de uma ameaça.
- **Pegar o Ouro e Voltar para a Casa Inicial**: +1000 pontos, recompensando o cumprimento do objetivo principal.

Este modelo detalhado do mundo de Wumpus fornece uma visão abrangente das regras, implementação e avaliação do agente, destacando o uso de POMDPs para gerenciar incertezas e guiar a tomada de decisões.

# Resultados Agente v2

## Testes

O agente do mundo de Wumpus foi testado em 5 diferentes tamanhos de mundo: 4x4, 5x5, 10x10, 15x15 e 20x20. Cada ambiente foi testado 20 vezes para avaliar o desempenho e a eficácia do agente em diferentes cenários.

Durante os testes, o agente foi avaliado com base em sua capacidade de encontrar o ouro e retornar à posição inicial, evitando quedas em poços ou encontros com o Wumpus. A pontuação do agente foi calculada com base em um sistema de pontuação que incentivava a eficiência e a segurança.

Os resultados dos testes mostraram que o agente teve um desempenho consistente em todos os tamanhos de mundo. Ele conseguiu encontrar o ouro e retornar à posição inicial na maioria dos casos, evitando quedas em poços e encontros com o Wumpus. No entanto, em alguns cenários mais complexos, o agente teve dificuldade em encontrar o caminho mais curto devido à presença de obstáculos e configurações do mundo desafiadoras.

Em geral, o agente demonstrou uma capacidade promissora de navegar e tomar decisões informadas em ambientes parcialmente observáveis e incertos. Os resultados dos testes forneceram insights valiosos sobre o desempenho do agente em diferentes cenários e podem ser usados para aprimorar ainda mais sua eficácia e eficiência.

![Resultados do Agente](/agente_reativo-v2/resultados/agente_v2.png)


# Conclusão

A integração de POMDPs e o algoritmo A* no mundo de Wumpus permite que o agente tome decisões informadas e eficientes, mesmo em um ambiente incerto e perigoso. POMDPs gerenciam a incerteza e ajustam as crenças do agente, enquanto o A* fornece um método robusto para planejar caminhos seguros e eficientes, adaptando-se dinamicamente às condições do ambiente. Esta abordagem integrada demonstra como técnicas avançadas de IA podem ser aplicadas a problemas complexos de navegação e tomada de decisão em ambientes parcialmente observáveis e incertos.

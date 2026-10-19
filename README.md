# Labirinto com DFS, BFS e Busca Gulosa

Atividade de AED II: busca da saída de um labirinto usando três algoritmos.

## O labirinto

O labirinto tem **13 linhas por 13 colunas**. A entrada `I` fica no canto superior esquerdo e a saída `F` fica dentro de uma sala central.

```text
#############
#I..........#
#...........#
#...........#
#...#####...#
#...#...#...#
#...#.F.#...#
#...#...#...#
#...##.##...#
#...........#
#...........#
#...........#
#############
```

A sala central tem paredes nos lados de cima, esquerda e direita. A única abertura fica embaixo, na posição `(8, 6)`. Essa escolha foi feita para mostrar um ponto em que a Busca Gulosa é enganada: ela se aproxima da saída pelo lado de cima, mas a parede bloqueia a entrada e ela precisa contornar a sala.

Legenda:

- `I` = entrada
- `F` = saída
- `#` = parede no labirinto original
- `.` = casa livre
- `*` = caminho encontrado
- `|` = parede vertical no desenho
- `_` = parede horizontal (chão ou teto) no desenho

No desenho dos caminhos, as casas livres aparecem em branco e as paredes são desenhadas com `|` ou `_` para facilitar a leitura.

## Como executar

```bash
python labirinto_buscas.py
```

O programa usa apenas a biblioteca padrão do Python. Não é necessário instalar nada.

## Implementação

O labirinto é transformado em um grafo:

- cada casa livre é um vértice `(linha, coluna)`;
- duas casas vizinhas (cima, baixo, esquerda, direita) formam uma aresta;
- o grafo é um dicionário no formato `{posição: [vizinhos]}`.

As buscas foram implementadas sem bibliotecas de caminhos prontas:

- **DFS (busca em profundidade):** usa uma pilha. Sempre tenta ir o mais fundo possível antes de voltar.
- **BFS (busca em largura):** usa uma fila. Explora primeiro as casas mais próximas da entrada, em camadas.
- **Busca Gulosa:** usa uma fila de prioridade ordenada pela distância de Manhattan até a saída. A cada passo escolhe a casa que parece mais perto, sem considerar o custo já percorrido.

A quantidade de **casas visitadas** é contada quando a casa é retirada da estrutura de busca e explorada pela primeira vez. Cada casa conta apenas uma vez.

## Resultados

```text
Algoritmo   Arestas  Casas no caminho   Casas visitadas
-------------------------------------------------------
DFS              40                41                82
BFS              16                17                86
Gulosa           22                23                52
```

### Caminho da DFS

```text
_____________
|I**********|
|          *|
|***********|
|*  _____   |
|***|   |   |
|  *| F |   |
|***| * |   |
|*  __*__   |
|******     |
|           |
|           |
_____________
```

### Caminho da BFS

```text
_____________
|I          |
|*          |
|*          |
|*  _____   |
|*  |   |   |
|*  | F |   |
|*  | * |   |
|*  __*__   |
|******     |
|           |
|           |
_____________
```

### Caminho da Busca Gulosa

```text
_____________
|I*****     |
|     *     |
|  ****     |
|  *_____   |
|  *|   |   |
|  *| F |   |
|  *| * |   |
|  *__*__   |
|  ****     |
|           |
|           |
_____________
```

## Respostas para a correção oral

### Por que a BFS encontrou o menor caminho e a DFS não?

A BFS explora o labirinto em camadas: primeiro todas as casas a uma aresta da entrada, depois as que estão a duas arestas, e assim por diante. Por isso, a primeira vez que ela alcança a saída, o caminho encontrado tem a menor quantidade de arestas possível. Neste labirinto, a BFS chegou à saída com **16 arestas**.

A DFS não faz isso. Ela escolhe um caminho e vai até o fim dele, voltando apenas quando não tem mais para onde ir. Assim, ela pode encontrar a saída por um caminho muito mais longo antes de passar por um caminho curto. Neste labirinto, a DFS chegou à saída com **40 arestas**. Ela visitou 82 casas, menos que as 86 da BFS, mas isso não significa que encontrou o melhor caminho.

### Em que ponto a Busca Gulosa foi induzida a um caminho inadequado por uma parede?

A Busca Gulosa sai da entrada e segue em direção à saída. Quando chega à casa `(3, 6)`, logo acima da sala central, a distância de Manhattan até `F` é apenas 3. Aparentemente ela está muito perto.

Porém, a casa `(4, 6)` é a parede de cima da sala, e a única entrada da sala fica embaixo, em `(8, 6)`. A parede impede a entrada pelo norte. A Gulosa então é obrigada a seguir para a esquerda, descer pelo lado esquerdo da sala e contornar até a abertura de baixo.

Ela encontra um caminho com **22 arestas**, enquanto a BFS encontra um com **16 arestas**. A Gulosa visitou menos casas (52), mas o caminho não é o menor. Esse é o ponto em que a heurística "vê" a saída perto, mas a parede invalida o caminho direto.

## Conclusão

- A **BFS** garante o menor caminho em quantidade de arestas, mas pode visitar muitas casas.
- A **DFS** encontra um caminho válido, mas não garante que seja o menor.
- A **Busca Gulosa** costuma visitar menos casas, mas pode ser enganada por paredes e encontrar um caminho maior que o da BFS.

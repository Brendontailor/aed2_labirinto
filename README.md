# Labirinto - AED II

Trabalho de busca em labirinto com os algoritmos DFS, BFS e Busca Gulosa.

## Labirinto

O labirinto tem 13 linhas por 13 colunas. A entrada `I` fica no canto superior esquerdo e a saída `F` fica dentro de uma sala central. A sala tem paredes em cima, à esquerda e à direita; a única abertura fica embaixo.

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

Legenda: `I` = entrada, `F` = saída, `#` = parede, `.` = casa livre.

Na execução, as paredes são desenhadas com `|` (verticais) e `_` (horizontais, chão ou teto), e o caminho é marcado com `*`.

## Como executar

```bash
python labirinto_buscas.py
```

O programa usa apenas a biblioteca padrão do Python.

## Implementações

- **DFS:** usa uma pilha e explora o mais fundo possível antes de voltar.
- **BFS:** usa uma fila e explora as casas em camadas, a partir da entrada.
- **Busca Gulosa:** usa uma fila de prioridade ordenada pela distância de Manhattan até a saída.
- O labirinto é representado por um grafo em dicionário: cada casa livre é um vértice e as casas vizinhas formam as arestas.
- As casas visitadas são contadas quando são retiradas da estrutura de busca pela primeira vez.

## Resultados

| Algoritmo | Arestas | Casas no caminho | Casas visitadas |
|---|---:|---:|---:|
| DFS | 40 | 41 | 82 |
| BFS | 16 | 17 | 86 |
| Gulosa | 22 | 23 | 52 |

A BFS encontrou o menor caminho. A DFS encontrou um caminho bem maior porque segue um ramo até o fim. A Gulosa visitou menos casas, mas foi enganada por uma parede e também não encontrou o menor caminho.



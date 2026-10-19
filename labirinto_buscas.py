# Atividade de AED II - Labirinto
# Legenda: I = entrada, F = saida, # = parede, . = livre

LABIRINTO = [
    "#############",
    "#I..........#",
    "#...........#",
    "#...........#",
    "#...#####...#",
    "#...#...#...#",
    "#...#.F.#...#",
    "#...#...#...#",
    "#...##.##...#",
    "#...........#",
    "#...........#",
    "#...........#",
    "#############",
]


def encontrar(labirinto, simbolo):
    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            if labirinto[linha][coluna] == simbolo:
                return (linha, coluna)
    return None


def eh_livre(labirinto, linha, coluna):
    if linha < 0 or linha >= len(labirinto):
        return False
    if coluna < 0 or coluna >= len(labirinto[linha]):
        return False
    return labirinto[linha][coluna] != "#"


def eh_parede(labirinto, linha, coluna):
    if linha < 0 or linha >= len(labirinto):
        return False
    if coluna < 0 or coluna >= len(labirinto[linha]):
        return False
    return labirinto[linha][coluna] == "#"


def montar_grafo(labirinto):
    grafo = {}
    movimentos = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for linha in range(len(labirinto)):
        for coluna in range(len(labirinto[linha])):
            if not eh_livre(labirinto, linha, coluna):
                continue

            grafo[(linha, coluna)] = []

            for dl, dc in movimentos:
                nova_linha = linha + dl
                nova_coluna = coluna + dc

                if eh_livre(labirinto, nova_linha, nova_coluna):
                    grafo[(linha, coluna)].append((nova_linha, nova_coluna))

    return grafo


def reconstruir_caminho(pai, inicio, fim):
    if fim not in pai:
        return []

    caminho = []
    atual = fim

    while atual != inicio:
        caminho.append(atual)
        atual = pai[atual]

    caminho.append(inicio)
    caminho.reverse()

    return caminho


def busca_profundidade(grafo, inicio, fim):
    pilha = [inicio]
    pai = {inicio: None}
    visitados = set()
    casas_visitadas = 0

    while pilha:
        atual = pilha.pop()

        if atual in visitados:
            continue

        visitados.add(atual)
        casas_visitadas += 1

        if atual == fim:
            break

        for vizinho in grafo[atual]:
            if vizinho not in visitados and vizinho not in pai:
                pai[vizinho] = atual
                pilha.append(vizinho)

    return reconstruir_caminho(pai, inicio, fim), casas_visitadas


def busca_largura(grafo, inicio, fim):
    fila = [inicio]
    pai = {inicio: None}
    visitados = set()
    casas_visitadas = 0

    while fila:
        atual = fila.pop(0)

        if atual in visitados:
            continue

        visitados.add(atual)
        casas_visitadas += 1

        if atual == fim:
            break

        for vizinho in grafo[atual]:
            if vizinho not in visitados and vizinho not in pai:
                pai[vizinho] = atual
                fila.append(vizinho)

    return reconstruir_caminho(pai, inicio, fim), casas_visitadas


def distancia_manhattan(posicao, destino):
    return abs(posicao[0] - destino[0]) + abs(posicao[1] - destino[1])


def busca_gulosa(grafo, inicio, fim):
    fila = [(distancia_manhattan(inicio, fim), inicio)]
    pai = {inicio: None}
    visitados = set()
    casas_visitadas = 0

    while fila:
        fila.sort()
        _, atual = fila.pop(0)

        if atual in visitados:
            continue

        visitados.add(atual)
        casas_visitadas += 1

        if atual == fim:
            break

        for vizinho in grafo[atual]:
            if vizinho not in visitados and vizinho not in pai:
                pai[vizinho] = atual
                fila.append((distancia_manhattan(vizinho, fim), vizinho))

    return reconstruir_caminho(pai, inicio, fim), casas_visitadas


def desenhar(labirinto, caminho):
    casas_do_caminho = set(caminho)
    desenho = []

    for linha in range(len(labirinto)):
        texto = ""

        for coluna in range(len(labirinto[linha])):
            simbolo = labirinto[linha][coluna]

            if simbolo == "#":
                tem_parede_ao_lado = (
                    eh_parede(labirinto, linha, coluna - 1)
                    or eh_parede(labirinto, linha, coluna + 1)
                )
                if tem_parede_ao_lado:
                    texto += "_"
                else:
                    texto += "|"
            elif simbolo == "I" or simbolo == "F":
                texto += simbolo
            elif (linha, coluna) in casas_do_caminho:
                texto += "*"
            else:
                texto += " "

        desenho.append(texto)

    return desenho


def mostrar_caminho(nome, labirinto, caminho):
    print(nome)
    for linha in desenhar(labirinto, caminho):
        print(linha)
    print()


def mostrar_tabela(resultados):
    print(f"{'Algoritmo':<10}{'Arestas':>9}{'Casas no caminho':>18}{'Casas visitadas':>18}")
    print("-" * 55)

    for nome, caminho, visitadas in resultados:
        arestas = len(caminho) - 1 if caminho else 0
        print(f"{nome:<10}{arestas:>9}{len(caminho):>18}{visitadas:>18}")


def main():
    inicio = encontrar(LABIRINTO, "I")
    fim = encontrar(LABIRINTO, "F")
    grafo = montar_grafo(LABIRINTO)

    caminho_dfs, visitadas_dfs = busca_profundidade(grafo, inicio, fim)
    caminho_bfs, visitadas_bfs = busca_largura(grafo, inicio, fim)
    caminho_gulosa, visitadas_gulosa = busca_gulosa(grafo, inicio, fim)

    print("LABIRINTO")
    for linha in LABIRINTO:
        print(linha)
    print()
    print("Legenda: I = entrada, F = saida, * = caminho, | e _ = parede")
    print()

    mostrar_caminho("DFS", LABIRINTO, caminho_dfs)
    mostrar_caminho("BFS", LABIRINTO, caminho_bfs)
    mostrar_caminho("BUSCA GULOSA", LABIRINTO, caminho_gulosa)

    print("TABELA COMPARATIVA")
    mostrar_tabela([
        ("DFS", caminho_dfs, visitadas_dfs),
        ("BFS", caminho_bfs, visitadas_bfs),
        ("Gulosa", caminho_gulosa, visitadas_gulosa),
    ])


if __name__ == "__main__":
    main()

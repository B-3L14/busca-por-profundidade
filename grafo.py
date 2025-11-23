# --- Criação do grafo ---
def criar_grafo():
    return {}


# --- Inserção de vértice ---
def inserir_vertice(grafo, vertice):
    if vertice not in grafo:
        grafo[vertice] = []
    pass


# --- Inserção de aresta ---
def inserir_aresta(grafo, origem, destino, nao_direcionado=False):
    inserir_vertice(grafo, origem)
    inserir_vertice(grafo, destino)

    if destino not in grafo[origem]:
        grafo[origem].append(destino)
    if nao_direcionado:
        if origem not in grafo[destino]:
            grafo[destino].append(origem)
    pass


# --- Vizinhos ---
def vizinhos(grafo, vertice):
    if vertice in grafo:
        return grafo[vertice]
    else:
        return []


def listar_vizinhos(grafo, vertice):
    if vertice in grafo:
        print(f"Vizinhos de {vertice}: {grafo[vertice]}")
    else:
        print(f"O vértice '{vertice}' não existe no grafo.")


# --- Exibir grafo ---
def exibir_grafo(grafo):
    print("\n--- Grafo (Lista de Adjacência) ---")
    for vertice in sorted(grafo.keys()):
        print(f"{vertice} -> {grafo[vertice]}")
    print("----------------------------------\n")


# --- Remover aresta ---
def remover_aresta(grafo, origem, destino, nao_direcionado=False):
    if origem in grafo and destino in grafo[origem]:
        grafo[origem].remove(destino)

    if nao_direcionado and destino in grafo and origem in grafo[destino]:
        grafo[destino].remove(origem)
    pass


# --- Remover vértice ---
def remover_vertice(grafo, vertice, nao_direcionado=True):
    if vertice in grafo:
        for outros_vertices in grafo.values():
            if vertice in outros_vertices:
                outros_vertices.remove(vertice)

        del grafo[vertice]
    pass


# --- Verificar existência de aresta ---
def existe_aresta(grafo, origem, destino):
    if origem in grafo and destino in grafo[origem]:
        return True
    return False


# --- Grau dos vértices ---
def grau_vertices(grafo):
    graus = {}
    for vertice in grafo:
        graus[vertice] = {"out": 0, "in": 0, "total": 0}

    for u in grafo:
        graus[u]["out"] = len(grafo[u])
        for v in grafo:
            if u in grafo[v]:
                graus[u]["in"] += 1

    for v in graus:
        graus[v]["total"] = graus[v]["out"] + graus[v]["in"]

    return graus


# --- Verificar percurso válido ---
def percurso_valido(grafo, caminho):
    if len(caminho) < 2:
        return True

    for i in range(len(caminho) - 1):
        origem = caminho[i]
        destino = caminho[i + 1]
        if not existe_aresta(grafo, origem, destino):
            return False
    return True


#Busca em profundidade

def buscaProfundidade(grafo, vertice, visitados=None):
    if visitados is None:
        visitados = set()

    print(vertice, end=" ")
    visitados.add(vertice)

    for vizinho in grafo.get(vertice, []):
        if vizinho not in visitados:
            buscaProfundidade(grafo, vizinho, visitados)


def executar_buscaProfundidade(grafo, inicio):
    if inicio not in grafo:
        print("O vértice não existe no grafo!")
        return

    print("Percurso:", end=" ")
    buscaProfundidade(grafo, inicio)
    print()


#Detecção de ciclos

def detecta_ciclo(grafo, vertice, visitados, recursao):
    visitados.add(vertice)
    recursao.add(vertice)

    for vizinho in grafo.get(vertice, []):
        if vizinho not in visitados:
            if detecta_ciclo(grafo, vizinho, visitados, recursao):
                return True
        elif vizinho in recursao:
            return True  # ciclo encontrado

    recursao.remove(vertice)
    return False


def detectar_ciclos(grafo):
    visitados = set()
    recursao = set()

    for vertice in grafo:
        if vertice not in visitados:
            if detecta_ciclo(grafo, vertice, visitados, recursao):
                return True

    return False


# ------------------------------------------------------------
#   MENU PRINCIPAL
# ------------------------------------------------------------

def main():
    grafo = criar_grafo()

    while True:
        print("""
===== MENU GRAFO =====
1 - Mostrar o Grafo
2 - Inserir vértice
3 - Inserir aresta
4 - Remover vértice
5 - Remover aresta
6 - Listar vizinhos
7 - Verificar se existe aresta
8 - Exibir graus dos vértices
9 - Verificar percurso válido
10 - Busca em profundidade
11 - Detectar ciclos
0 - Sair
======================
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exibir_grafo(grafo)

        elif opcao == "2":
            v = input("Digite o nome do vértice: ")
            inserir_vertice(grafo, v)
            print("Vértice inserido com sucesso.")

        elif opcao == "3":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(grafo, o, d, nd)
            print("Aresta inserida com sucesso.")

        elif opcao == "4":
            v = input("Vértice a remover: ")
            remover_vertice(grafo, v)
            print("Vértice removido (se existia).")

        elif opcao == "5":
            o = input("Origem: ")
            d = input("Destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            remover_aresta(grafo, o, d, nd)
            print("Aresta removida (se existia).")

        elif opcao == "6":
            v = input("Digite o vértice: ")
            listar_vizinhos(grafo, v)

        elif opcao == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(grafo, o, d))

        elif opcao == "8":
            graus = grau_vertices(grafo)
            for v, g in graus.items():
                print(f"{v}: in={g['in']}, out={g['out']}, total={g['total']}")

        elif opcao == "9":
            caminho = input("Digite o caminho (vértices separados por espaço): ").split()
            if percurso_valido(grafo, caminho):
                print("O percurso é válido.")
            else:
                print("O percurso é inválido.")

        elif opcao == "10":
            v = input("Vértice inicial da busca: ")
            executar_buscaProfundidade(grafo, v)

        elif opcao == "11":
            if detectar_ciclos(grafo):
                print("O grafo possui ciclos!")
            else:
                print("O grafo NÃO possui ciclos.")

        elif opcao == "0":
            print("Encerrando o programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
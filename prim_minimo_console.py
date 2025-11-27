import heapq

def prim_mst(graph, start):
    """
    Algoritmo de Prim para Árbol de Expansión Mínimo.
    graph: diccionario {nodo: [(vecino, peso), ...]}
    start: nodo inicial
    """
    visited = set([start])  # Conjunto de nodos ya conectados
    edges = [(w, start, v) for v, w in graph[start]]  # Aristas desde el nodo inicial
    heapq.heapify(edges)  # Cola de prioridad por peso
    mst = []  # Lista de aristas del MST

    print("=== Simulador Prim (Consola) ===")
    print(f"Inicio en nodo {start}\n")

    while edges:
        w, u, v = heapq.heappop(edges)  # Extraemos la arista más barata
        if v not in visited:
            visited.add(v)
            mst.append((u, v, w))
            print(f"Conecto {u} -> {v} con peso {w}")
            # Añadimos nuevas aristas desde el nodo recién conectado
            for to, weight in graph[v]:
                if to not in visited:
                    heapq.heappush(edges, (weight, v, to))

    print("\nÁrbol Parcial Mínimo construido:")
    for u, v, w in mst:
        print(f"{u} - {v} (peso {w})")

    return mst

# Grafo de ejemplo
graph = {
    "A": [("B", 2), ("C", 3)],
    "B": [("A", 2), ("C", 1), ("D", 4)],
    "C": [("A", 3), ("B", 1), ("D", 5), ("E", 6)],
    "D": [("B", 4), ("C", 5), ("E", 7)],
    "E": [("C", 6), ("D", 7)]
}

mst = prim_mst(graph, "A")

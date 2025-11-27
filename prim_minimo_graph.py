import networkx as nx
import matplotlib.pyplot as plt

def plot_mst(graph_dict, mst):
    G = nx.Graph()
    for u, edges in graph_dict.items():
        for v, w in edges:
            G.add_edge(u, v, weight=w)

    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(7, 5))
    nx.draw(G, pos, with_labels=True, node_color="#87CEFA", node_size=900, font_weight="bold")
    weights = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=weights)

    # Resaltamos las aristas del MST
    mst_edges = [(u, v) for u, v, w in mst]
    nx.draw_networkx_edges(G, pos, edgelist=mst_edges, width=3, edge_color="red")

    plt.title("Árbol Parcial Mínimo (Prim)")
    plt.show()

plot_mst(graph, mst)

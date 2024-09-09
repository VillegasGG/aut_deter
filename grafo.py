import networkx as nx
from matplotlib import pyplot as plt
import itertools as it

def crearGrafo(estados, alfabeto, matriz):
    G = nx.MultiDiGraph(directed=True)
    
    for i, linea in enumerate(matriz):
        lista_linea = linea.split(' ')
        for j, elemento in enumerate(lista_linea):
            G.add_edge(estados[i], elemento, label = alfabeto[j])

    return G

def graficar(G):
    connectionstyle = [f"arc3,rad={r}" for r in it.accumulate([0.15] * 4)]
    pos = nx.shell_layout(G)
    nx.draw_networkx_nodes(G, pos, node_size=6)
    nx.draw_networkx_labels(G, pos, font_size=5)
    nx.draw_networkx_edges(
        G, pos, edge_color="black", connectionstyle=connectionstyle
    )
    labels = {
        tuple(edge): f"{attrs['label']}" for *edge, attrs in G.edges(keys=True, data=True)
    }
    print(labels)
    nx.draw_networkx_edge_labels(
        G,
        pos,
        labels,
        connectionstyle=connectionstyle,
        label_pos=0.7,
        font_color="black",
        font_size=8,
        bbox={"alpha": 0},
    )

    plt.show()
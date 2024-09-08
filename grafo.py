import networkx as nx
from matplotlib import pyplot as plt

def crearGrafo(estados, alfabeto, matriz):
    G = nx.DiGraph()
    
    for i, linea in enumerate(matriz):
        lista_linea = linea.split(' ')
        for j, elemento in enumerate(lista_linea):
            G.add_edge(estados[i], elemento, weight = alfabeto[j])

    return G

def graficar(G):
    # Generar posiciones para los nodos
    pos = nx.spring_layout(G)

    # Dibujar nodos y etiquetas
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)
    nx.draw_networkx_labels(G, pos, font_weight='bold')

    # Dibujar aristas dirigidas
    forward_edges = [(u, v) for u, v in G.edges() if not G.has_edge(v, u)]
    bidirectional_edges = [(u, v) for u, v in G.edges() if G.has_edge(v, u)]

    nx.draw_networkx_edges(G, pos, edgelist=forward_edges, arrowstyle='-|>', arrowsize=20, width=2)
    nx.draw_networkx_edges(G, pos, edgelist=bidirectional_edges, arrowstyle='-|>', arrowsize=20, width=2, connectionstyle='arc3,rad=0.2')

    # Obtener los pesos y dibujarlos como etiquetas en las aristas
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, bbox=dict(facecolor='white', alpha=0.5))

    # Mostrar el gráfico
    plt.show()

    # Imprimir aristas y sus atributos
    print("\nAristas del grafo:")
    for u, v, data in G.edges(data=True):
        print(f"Arista de {u} a {v}: {data}")

    # Imprimir solo los pesos de las aristas
    print("\nPesos de las aristas:")
    edge_weights = nx.get_edge_attributes(G, 'weight')
    for (u, v), weight in edge_weights.items():
        print(f"Arista de {u} a {v} tiene peso {weight}")

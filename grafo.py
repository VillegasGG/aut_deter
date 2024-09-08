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
    # Generar posiciones para los nodos
    pos = nx.spring_layout(G)  # Puedes usar diferentes layouts: spring_layout, circular_layout, etc.

    # Dibujar el grafo
    plt.figure(figsize=(10, 8))

    # Dibujar nodos
    nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=700)

    # Dibujar etiquetas de nodos
    nx.draw_networkx_labels(G, pos, font_weight='bold')

    # Dibujar aristas
    nx.draw_networkx_edges(G, pos, width=2)

    # Obtener los pesos y dibujarlos como etiquetas en las aristas
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12, bbox=dict(facecolor='white', alpha=0.5))

    # Mostrar el gráfico
    plt.title("Grafo No Dirigido con Pesos")
    plt.show()

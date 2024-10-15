import networkx as nx
from matplotlib import pyplot as plt
from networkx.drawing.nx_agraph import to_agraph

def crearGrafo(estados, alfabeto, matriz, aceptados):
    G = nx.MultiDiGraph(directed=True)
    
    for estado in estados:
        if estado in aceptados:
            G.add_node(estado, shape="doublecircle", accepting=True) 
        else:
            G.add_node(estado, shape="circle", accepting=False)  

    for i, linea in enumerate(matriz):
        for j, elemento in enumerate(linea):
            if(elemento!='-'):
                G.add_edge(estados[i], elemento, label = alfabeto[j])

    return G

def graficar(G):
    A = to_agraph(G)

    A.graph_attr['rankdir'] = 'LR'  
    A.node_attr['shape'] = 'circle' 
    A.edge_attr['fontsize'] = 10  

    for u, v, d in G.edges(data=True):
        A.get_edge(u, v).attr['label'] = d['label']

    A.draw('grafo.png', format='png', prog='dot')

    img = plt.imread('grafo.png')
    plt.imshow(img)
    plt.axis('off')
    plt.show()
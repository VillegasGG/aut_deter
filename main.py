import networkx as nx
import grafo
import helper

def main():
    G = nx.MultiDiGraph(directed=True)

    G = helper.entrada()

    grafo.graficar(G)

main()
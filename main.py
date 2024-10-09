import networkx as nx
import grafo
import helper
import algoritmo

def main():
    G = nx.MultiDiGraph(directed=True)

    G, q0, aceptados = helper.entrada()

    grafo.graficar(G)

    algoritmo.automata(G, q0, aceptados)

main()
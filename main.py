import networkx as nx
import grafo
import helper

def main():
    G = nx.DiGraph

    G = helper.entrada()

    grafo.graficar(G)

main()
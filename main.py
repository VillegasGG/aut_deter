import networkx as nx
import grafo
import helper
import algoritmo

def main():
    G = nx.MultiDiGraph(directed=True)

    G, q0, alfabeto = helper.entrada()

    grafo.graficar(G)

    cadena = helper.leer_string(alfabeto)
    algoritmo.automata(G, q0, cadena)
    
    while True:
        helper.opciones()
        opcion = input("Select an option : ")

        if opcion == "1":
            cadena = helper.leer_string(alfabeto)
            algoritmo.automata(G, q0, cadena)
        elif opcion == "2":
            break
        else:
            print("Invalid option. Please try again.")




main()
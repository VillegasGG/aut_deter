import networkx as nx
import grafo

def main():
    G = nx.DiGraph
    matriz_transiciones = []
    estados = input("Ingrese los estados separados por un espacio: ").split(' ')
    alfabeto = input("Ingrese el alfabeto (separe cada elemento con un espacio): ").split(' ')
    print("Ingrese fila a fila las transiciones: ")

    cadena = ''
    for el in alfabeto:
        cadena = cadena + '\t' + el

    print(cadena)
    for i in range(len(estados)):
        t = input(estados[i] + ': ')
        matriz_transiciones.append(t)
    
    # q0 = input("Ingrese el estado inicial: ")
    # estados_aceptados = input("Ingrese los estados de aceptacion: ")

    G = grafo.crearGrafo(estados, alfabeto, matriz_transiciones)

    grafo.graficar(G)

main()
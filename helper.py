import networkx as nx
import grafo

def entrada():
    G = nx.MultiDiGraph()
    matriz_transiciones = []
    estados_aceptados = []
    estados = input("Ingrese los estados separados por un espacio: ").split(' ')
    alfabeto = input("Ingrese el alfabeto (separe cada elemento con un espacio): ").split(' ')
    print("Ingrese fila a fila las transiciones (para vacio agregue \"-\"): ")

    cadena = ''
    for el in alfabeto:
        cadena = cadena + '\t' + el

    print(cadena)
    for i in range(len(estados)):
        t = input(estados[i] + ': ')
        matriz_transiciones.append(t)
    
    q0 = input("Ingrese el estado inicial: ")
    num_aceptados = int(input("Ingrese el numero de estados aceptados: "))

    for i in range(num_aceptados):
        e = input("Estado aceptado: ")
        estados_aceptados.append(e)

    G = grafo.crearGrafo(estados, alfabeto, matriz_transiciones, q0, estados_aceptados)

    return G

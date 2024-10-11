import networkx as nx
import grafo

def entrada():
    G = nx.MultiDiGraph()
    matriz_transiciones = []
    estados_aceptados = []
    estados = input("Enter the states separated by a space: ").split(' ')
    alfabeto = input("Enter the alphabet (separate each item with a space): ").split(' ')
    print("Enter the transitions row by row (\"-\" for empty): ")

    cadena = ''
    for el in alfabeto:
        cadena = cadena + '\t' + el

    print(cadena)
    for i in range(len(estados)):
        while(True):
            t = input(estados[i] + ': ')
            c = 0
            tr = t.split()
            if(len(tr) == len(alfabeto)):
                for el in tr:
                    if el in estados or el == '-':
                        c += 1
                    if el not in estados and el != '-':
                        print(f"Error: {el} is not found in the states list")
                if(c == len(alfabeto)):
                    matriz_transiciones.append(tr)
                    break
            else:
                print(f"Error: You must enter {len(alfabeto)} transitions separated by spaces. (\"-\" for empty)")
    
    q0 = input("Enter the initial state: ")
    estados_aceptados = input("Enter the ACCEPTING states separated by a space: ").split(' ')

    cadena = input("Enter the string to validate (Separate each transition with spaces. E.g.: 0 1 1 1): ").split(' ')

    G = grafo.crearGrafo(estados, alfabeto, matriz_transiciones, q0, estados_aceptados)

    return G, q0, estados_aceptados, cadena
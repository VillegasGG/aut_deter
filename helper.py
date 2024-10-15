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
    
    q0 = leer_q0(estados)
    estados_aceptados = leer_aceptados(estados)
   

    G = grafo.crearGrafo(estados, alfabeto, matriz_transiciones, estados_aceptados)

    return G, q0, alfabeto

def leer_aceptados(estados):
    while(True):
        aceptados = input("Enter the ACCEPTING states separated by a space: ").strip().split(' ')
        b = True
        for el in aceptados:
            if el not in estados:
                print(f"Error: '{el}' is not in the states {estados}. Try again.")
                b = False
                break
        if b:
            return aceptados

def leer_q0(estados):
    while(True):
        q0 = input("Enter the initial state: ")
        if q0 not in estados:
            print(f"Error: '{q0}' is not in the states {estados}. Try again.")
        else:
            return q0


def leer_string(alfabeto):
    while(True):
        cadena = input("Enter the string to validate (Separate each transition with a space. E.g.: 0 1 1 1): ").strip().split(' ')
        b = True
        for el in cadena:
            if el not in alfabeto:
                print(f"Error: '{el}' is not in the alphabet. {alfabeto}. Try again.")
                b = False
                break
        
        if b:
            return cadena

def opciones():
    print("\n=== Select an option ===")
    print("1. Enter new string: ")
    print("2. Exit")
    print("=====================")
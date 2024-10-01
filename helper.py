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
        while(True):
            t = input(estados[i] + ': ')
            
            tr = t.split()
            if(len(tr) == len(alfabeto)):
                matriz_transiciones.append(tr)
                break
            else:
                print(f"Error: Debe ingresar {len(alfabeto)} transiciones separadas por espacios. Nota: para vacio agregue \"-\" ")
    
    q0 = input("Ingrese el estado inicial: ")
    estados_aceptados = input("Ingrese los estados ACEPTADOS separados por un espacio: ").split(' ')

    G = grafo.crearGrafo(estados, alfabeto, matriz_transiciones, q0, estados_aceptados)

    return G

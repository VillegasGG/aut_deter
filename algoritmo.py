def automata(G, q0, aceptados, cadena):
    estado_actual = q0
    for element in cadena:
        print(estado_actual)
        for u, v, data in G.edges(estado_actual, data=True):
            if(data['label'] == element):
                estado_actual = v        

    if(G.nodes[estado_actual]['accepting']):
        print('Cadena aceptada')
    else:
        print('Cadena no aceptada')
    return
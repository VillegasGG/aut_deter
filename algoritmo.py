def automata(G, q0, cadena):
    estado_actual = q0
    for element in cadena:
        for u, v, data in G.out_edges(estado_actual, data=True):
            if(data['label'] == element):
                estado_actual = v        

    if(G.nodes[estado_actual]['accepting']):
        print("=====================")
        print('Accepted string')
        print("=====================")
    else:
        print("=====================")
        print('Rejected string')
        print("=====================")
    return
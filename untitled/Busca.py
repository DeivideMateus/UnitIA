import networkx as nx

def searchPath(v1, v2):
    G = nx.Graph()
    e = [('A', 'B', 5),
         ('B', 'C', 7), ('B', 'F', 2),
         ('C', 'L', 8),
         ('D', 'E', 3),
         ('E', 'I', 6),
         ('F', 'G', 5), ('F', 'J', 6),
         ('G', 'K', 6),
         ('H', 'I', 3),
         ('I', 'J', 2),
         ('J', 'K', 5), ('J', 'O', 2),
         ('K', 'L', 2), ('K', 'T', 9),
         ('L', 'U', 9),
         ('M', 'N', 3),
         ('N', 'O', 2), ('N', 'R', 7),
         ('O', 'P', 3),
         ('P', 'S', 7),
         ('Q', 'R', 3),
         ('R', 'S', 5),
         ('S', 'T', 2),
         ('T', 'U', 2)]

    G.add_weighted_edges_from(e)
    caminhoLista = nx.dijkstra_path(G, v1, v2)
    custoCaminho = nx.dijkstra_path_length(G, v1, v2)
    caminho = ""

    for i in caminhoLista:
        caminho = caminho + i + " - "

    textCaminho = "O menor caminho entre " + v1 + " e " + v2 + " é: " + caminho + ", com custo de " + str(custoCaminho)

    return textCaminho


#print(searchPath('A', 'Q'))

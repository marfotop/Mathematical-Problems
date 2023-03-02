import networkx as nx
import matplotlib.pyplot as plt
import random

G = nx.DiGraph()
V = [1, 2, 3, 4, 5, 6, 7, 8, 9]
U = [(1, 8), (2, 6), (2, 9), (3, 8), (4, 9), (4, 1), (6, 1), (6, 8), (7, 5), (8, 7), (8, 5), (9, 8)]
G.add_nodes_from(V)
G.add_edges_from(U)

# nx.draw_networkx(G)
# plt.show()

for i in range(1, 4):
    L = []
    H = G.copy()
    while len(H) != 0:
        notFound = True
        random.shuffle(list(H.nodes))
        i = 0
        lst = list(H.nodes)
        length = len(lst)
        while i <= length:
            lst = list(H.nodes)
            v = random.choice(lst)
            # print(v)
            # print(list(H.nodes))

            if H.in_degree(v) == 0:
                L.append(v)
                H.remove_node(v)
                lst.remove(v)
                i += 1
                notFound = False  # vertex v has in_degree 0
                break
        if notFound:  # no vertex has in_degree 0
            break
    if len(L) == len(G):
        print("A topological sorting of G: ", L)
    else:
        print("G contains a cycle")

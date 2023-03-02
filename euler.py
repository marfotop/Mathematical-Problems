import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

n = int(input("Give n: "))
for i in range(1, n + 1):
    G.add_node(i)

for i in range(1, n + 1):
    for j in range(i, n + 1):
        if i != j:
            G.add_edge(i, j)


# nx.draw_networkx(G)
# plt.show()

if nx.is_eulerian(G):
    W1 = nx.eulerian_circuit(G)
    print("An Eulerian circuit for G: ", list(W1))
else:
    print("G is not Eulerian graph")
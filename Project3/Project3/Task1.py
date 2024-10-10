import networkx as nx
import matplotlib.pyplot as plt

# Union-Find data structure for cycle detection
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    # Find with path compression
    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    # Union by rank
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank to keep tree flat
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Kruskal's algorithm to find MST
def kruskal(n, edges):
    # Sort edges by their weights
    edges.sort(key=lambda x: x[2])

    uf = UnionFind(n)
    mst = []  # To store the minimum spanning tree

    for u, v, weight in edges:
        # If u and v are in different sets, add the edge to the MST
        if uf.find(u) != uf.find(v):
            mst.append((u, v, weight))
            uf.union(u, v)

    return mst

# Example graph with 5 vertices and edges with weights
# (u, v, weight) where u and v are vertices
edges = [
    (0, 1, 2), (0, 3, 6),
    (1, 2, 3), (1, 3, 8), (1, 4, 5),
    (2, 4, 7), (3, 4, 9)
]

n = 5  # Number of vertices in the graph

# Running Kruskal's algorithm to find the MST
mst = kruskal(n, edges)

# Output the edges in the MST
print("Minimum Spanning Tree edges (with weights):")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")

# Create a graph with NetworkX
G = nx.Graph()

# Add edges to the original graph
for u, v, weight in edges:
    G.add_edge(u, v, weight=weight)

# Draw the original graph with weights
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=12)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Original Graph with Weights")
plt.show()

# Create another graph for the MST
MST = nx.Graph()
for u, v, weight in mst:
    MST.add_edge(u, v, weight=weight)

# Draw the Minimum Spanning Tree (MST)
plt.figure(figsize=(8, 6))
nx.draw(MST, pos, with_labels=True, node_color='lightgreen', node_size=700, font_size=12)
mst_edge_labels = nx.get_edge_attributes(MST, 'weight')
nx.draw_networkx_edge_labels(MST, pos, edge_labels=mst_edge_labels)
plt.title("Minimum Spanning Tree (MST)")
plt.show()

import networkx as nx
import matplotlib.pyplot as plt

# Union-Find data structure for cycle detection
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Kruskal's algorithm to find MST
def kruskal(n, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(n)
    mst = []
    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            mst.append((u, v, weight))
            uf.union(u, v)
    return mst

# Function to create the MST graph
def create_mst_graph():
    edges = [
        (0, 1, 2), (0, 3, 6),
        (1, 2, 3), (1, 3, 8), (1, 4, 5),
        (2, 4, 7), (3, 4, 9)
    ]
    n = 5
    mst_edges = kruskal(n, edges)
    
    G = nx.Graph()
    G.add_weighted_edges_from(edges)
    
    # Create MST graph
    MST = nx.Graph()
    MST.add_weighted_edges_from(mst_edges)
    
    return G, MST

# Testing the MST creation
if __name__ == "__main__":
    G, MST = create_mst_graph()
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=700, font_size=12)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Original Graph with Weights")
    plt.show()

    plt.figure(figsize=(8, 6))
    nx.draw(MST, pos, with_labels=True, node_color='lightgreen', node_size=700, font_size=12)
    mst_edge_labels = nx.get_edge_attributes(MST, 'weight')
    nx.draw_networkx_edge_labels(MST, pos, edge_labels=mst_edge_labels)
    plt.title("Minimum Spanning Tree (MST)")
    plt.show()

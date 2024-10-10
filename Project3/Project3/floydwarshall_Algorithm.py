# floydwarshall_Algorithm.py

def floyd_warshall_algorithm(graph):
    distances = {node: {node2: float('inf') for node2 in graph.nodes} for node in graph.nodes}
    
    # Set the distance from a node to itself to 0
    for node in graph.nodes:
        distances[node][node] = 0
    
    # Initialize distances based on edges
    for u, v, attributes in graph.edges(data=True):
        distances[u][v] = attributes['weight']
        distances[v][u] = attributes['weight']
    
    # Floyd-Warshall algorithm
    for k in graph.nodes:
        for i in graph.nodes:
            for j in graph.nodes:
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    
    return distances  #returns the shortest distances(minimal weight) from the start node(stockholm) to all other nodes(cities)

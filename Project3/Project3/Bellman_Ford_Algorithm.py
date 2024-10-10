# Bellman_Ford_Algorithm.py

def bellman_ford_algorithm(graph, start):
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    
    for _ in range(len(graph.nodes) - 1):
        for u, v, attributes in graph.edges(data=True):
            weight = attributes['weight']
            if distances[u] + weight < distances[v]:
                distances[v] = distances[u] + weight
            if distances[v] + weight < distances[u]:
                distances[u] = distances[v]
    
    return distances #returns the shortest distances(minimal weight) from the start node(stockholm) to all other nodes(cities)

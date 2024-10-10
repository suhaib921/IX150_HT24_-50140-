# dijkstra_Algorithm.py
import heapq

def dijkstra_algorithm(graph, start):
    # Priority queue for Dijkstra's algorithm
    queue = [(0, start)]  # (distance, node)
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    
    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        # Skip processing if we already have a shorter distance recorded
        if current_distance > distances[current_node]:
            continue
        
        for neighbor, attributes in graph[current_node].items():
            distance = current_distance + attributes['weight']
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))
    
    return distances  #returns the shortest distances(minimal weight) from the start node(stockholm) to all other nodes(cities)

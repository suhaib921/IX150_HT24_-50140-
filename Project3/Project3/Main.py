# main.py
import networkx as nx
import matplotlib.pyplot as plt
import timeit
from Task2 import create_graph_with_weights, cities
from dijkstra_Algorithm import dijkstra_algorithm
from Bellman_Ford_Algorithm import bellman_ford_algorithm
from floydwarshall_Algorithm import floyd_warshall_algorithm



# Function to draw the graph
def draw_graph(graph, cities, title):
    plt.figure(figsize=(12, 12))
    pos = nx.spring_layout(graph, seed=42)  # Generate positions for nodes
    nx.draw(graph, pos, with_labels=True, labels={i: cities[i] for i in range(len(cities))},
            node_size=800, node_color="lightblue", font_size=10, font_weight="bold")
    nx.draw_networkx_edges(graph, pos)
    edge_labels = {(u, v): f"{d['weight']:.2f}" for u, v, d in graph.edges(data=True)}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red')
    plt.title(title)
    plt.show()

# Function to manually trace and verify the shortest path
def trace_shortest_path(graph, start, target, cities):
    path = nx.shortest_path(graph, source=start, target=target, weight='weight')
    total_weight = 0
    print(f"\nShortest path from {cities[start]} to {cities[target]}:")
    for i in range(len(path) - 1):
        u, v = path[i], path[i + 1]
        weight = graph[u][v]['weight']
        total_weight += weight
        print(f"  {cities[u]} --> {cities[v]} (Weight: {weight:.2f})")
    print(f"\nTotal weight (inverse capacity) from {cities[start]} to {cities[target]}: {total_weight:.2f}")

        
# Function to simulate link failure
def simulate_link_failure(graph, city1, city2):
    print(f"\n--- Simulating link failure: {city1} – {city2} ---")
    # Find the indices of the cities
    city1_index = cities.index(city1)
    city2_index = cities.index(city2)
    
    if graph.has_edge(city1_index, city2_index):
        # Remove the edge between the cities
        graph.remove_edge(city1_index, city2_index)
        print(f"Link between {city1} and {city2} has been removed.")
    else:
        print(f"Link between {city1} and {city2} does not exist or is already removed.")

# Function to handle link failure and re-run algorithms
def handle_link_failure(graph, city1, city2, start_node, target_node, num_runs, cities):
   
    # Simulate link failure: city1 – city2
    simulate_link_failure(graph, city1, city2)

    # Re-run Dijkstra's algorithm after link failure
    print("\n--- Re-running Dijkstra's Algorithm after link failure ---")
    dijkstra_time_after = timeit.timeit(lambda: dijkstra_algorithm(graph, start_node), number=num_runs) / num_runs
    print(f"Dijkstra's Algorithm (after link failure) execution time: {dijkstra_time_after:.10f} seconds")

    # Trace the shortest path from Stockholm to Abisko after the failure
    trace_shortest_path(graph, start_node, target_node, cities)
    draw_graph(graph, cities, "City Network - After Link Failure")


# Function to print the shortest paths from Stockholm to all other cities
def print_shortest_paths_from_stockholm(graph, start_node, cities, num_runs=1000):
     # Print shortest paths from Stockholm to all other cities
    print("\nShortest paths from Stockholm to all other cities:")
    
    # Get shortest paths from Stockholm to all other cities
    distances = dijkstra_algorithm(graph, start_node)
    for node, distance in distances.items():
        print(f"Shortest distance from {cities[start_node]} to {cities[node]}: {distance:.2f}")

    for target_node in range(len(cities)):
        if target_node != start_node:
            trace_shortest_path(graph, start_node, target_node, cities)


# Main function
def main():
    # Create the graph with predefined and random capacities
    G = create_graph_with_weights()

    # Stockholm index (assuming it's at index 16) and Abisko at index 0
    start_node = 16  # Stockholm
    target_node = 0  # Abisko

    # Number of runs for timing accuracy
    num_runs = 1000


    # Print shortest paths from Stockholm to all other cities
    print_shortest_paths_from_stockholm(G, start_node, cities)

   # Measure and run Dijkstra's algorithm
    print("\n--- Running Dijkstra's Algorithm ---")
    dijkstra_time = timeit.timeit(lambda: dijkstra_algorithm(G, start_node), number=num_runs) / num_runs
    print(f"Dijkstra's Algorithm execution time: {dijkstra_time:.10f} seconds")


   # Measure and run Bellman-Ford Algorithm
    print("\n--- Running Bellman-Ford Algorithm ---")
    bellman_ford_time = timeit.timeit(lambda: bellman_ford_algorithm(G, start_node), number=num_runs) / num_runs
    print(f"Bellman-Ford Algorithm execution time: {bellman_ford_time:.10f} seconds")

    # Measure and run Floyd-Warshall Algorithm
    print("\n--- Running Floyd-Warshall Algorithm ---")
    floyd_warshall_time = timeit.timeit(lambda: floyd_warshall_algorithm(G), number=num_runs) / num_runs
    print(f"Floyd-Warshall Algorithm average execution time: {floyd_warshall_time:.10f} seconds")

    trace_shortest_path(G, start_node, target_node, cities)

    # Draw the graph with the calculated paths
    draw_graph(G, cities, "City Network - Shortest Paths")

     # Stockholm index (assuming it's at index 16) and Abisko at index 0
    start_node = 3  # Goteborg 
    target_node = 12  # Lund

     # Measure and run Dijkstra's algorithm
    print("\n--- bkababm ---")
    dijkstra_time = timeit.timeit(lambda: dijkstra_algorithm(G, start_node), number=num_runs) / num_runs
    print(f"Dijkstra's Algorithm execution time: {dijkstra_time:.10f} seconds")

    trace_shortest_path(G, start_node, target_node, cities)


    # Handle link failure and re-run algorithms
    handle_link_failure(G, "Goteborg", "Lund", start_node, target_node, num_runs, cities)

if __name__ == "__main__":
    main()

import networkx as nx
import matplotlib.pyplot as plt

# Define the cities and links between them without inverse capacity (just connections)
cities = ["Abisko", "Boden", "Falun", "Goteborg", "Hoganas", "Hudiksvall", "Jonkoping", 
          "Kalmar", "Kiruna", "Lidkoping", "Linkoping", "Lulea", "Lund", "Malmo", "Mariestad", 
          "Ostersund", "Stockholm", "Strangnas", "Timra", "Uppsala", "Umea", "Varberg", "Visby"]

# Define the links between cities (just connections, no weights)
links = [
    (15, 18), (13, 17), (3, 16), (6, 3), (18, 6), (12, 2), (15, 11), (19, 21), (7, 8),
    (19, 2), (7, 4), (21, 17), (17, 11), (23, 11), (10, 7), (16, 17), (10, 20),
    (13, 5), (3, 17), (7, 22), (15, 10), (16, 18), (11, 16), (17, 23), (18, 17),
    (20, 6), (11, 7), (9, 2), (3, 20), (4, 17), (19, 17), (7, 20), (22, 4), (14, 7),
    (15, 17), (6, 17), (20, 5), (16, 15), (11, 3), (9, 1), (4, 10), (5, 14), (6, 16),
    (16, 19), (13, 8), (8, 23), (16, 10), (4, 13), (2, 16), (15, 3), (20, 18)
]

# Create a graph
G = nx.Graph()


# Adjust indexing to 0-based for Python
adjusted_links = [(city1 - 1, city2 -1) for city1, city2 in links]

# Add the links and draw the graph again
G.add_edges_from(adjusted_links)


# Display the direct links between cities with city names
print("Direct connections between cities:")
for link in links:
    city1, city2= link
    print(link)
    print(f"{cities[city1-1]} <--> {cities[city2-1]}")

# Visualization of the graph (optional)
plt.figure(figsize=(10, 10))
pos = nx.spring_layout(G)  # Positions for all nodes
nx.draw(G, pos, with_labels=True, labels={i: cities[i] for i in range(len(cities))}, node_size=700, node_color="lightblue")
plt.title("City Network without Weights")
plt.show()

import networkx as nx
import random

# Define the cities
cities = ["Abisko", "Boden", "Falun", "Goteborg", "Hoganas", "Hudiksvall", "Jonkoping", 
          "Kalmar", "Kiruna", "Lidkoping", "Linkoping", "Lulea", "Lund", "Malmo", "Mariestad", 
          "Ostersund", "Stockholm", "Strangnas", "Timra", "Uppsala", "Umea", "Varberg", "Visby"]

# Define the links between cities (connections only, no capacity yet)
links = [
    (15, 18), (13, 17), (3, 16), (6, 3), (18, 6), (12, 2), (15, 11), (19, 21), (7, 8),
    (19, 2), (7, 4), (21, 17), (17, 11), (23, 11), (10, 7), (16, 17), (10, 20),
    (13, 5), (3, 17), (7, 22), (15, 10), (16, 18), (11, 16), (17, 23), (18, 17),
    (20, 6), (11, 7), (9, 2), (3, 20), (4, 17), (19, 17), (7, 20), (22, 4), (14, 7),
    (15, 17), (6, 17), (20, 5), (16, 15), (11, 3), (9, 1), (4, 10), (5, 14), (6, 16),
    (16, 19), (13, 8), (8, 23), (16, 10), (4, 13), (2, 16), (15, 3), (20, 18)
]

# Predefined capacities for specific links (provided in the task)
predefined_capacities = {
    ('Stockholm', 'Goteborg'): 25,
    ('Stockholm', 'Lund'): 30,
    ('Goteborg', 'Lund'): 25,
    ('Stockholm', 'Falun'): 15,
    ('Falun', 'Ostersund'): 15,
    ('Ostersund', 'Umea'): 15
}
# Function to calculate the inverse of capacity
def calculate_inverse_capacity(links, predefined_capacities):
    weighted_links = []
    for link in links:
        city1_index, city2_index = link
        city1 = cities[city1_index - 1]  # Adjust to 1-based indexing
        city2 = cities[city2_index - 1]
        
        # Check if the capacity for this link is predefined
        if (city1, city2) in predefined_capacities:
            capacity = predefined_capacities[(city1, city2)]
        elif (city2, city1) in predefined_capacities:
            capacity = predefined_capacities[(city2, city1)]
        else:
            # Assign random capacity between 1 and 10 for undefined links
            capacity = random.randint(1, 10)
        
        # Calculate the weight (inverse of capacity)
        weight = 1 / capacity
        
        # Add the link with weight to the list
        weighted_links.append((city1_index - 1, city2_index - 1, weight))
    
    return weighted_links

# Function to create the graph with weighted edges
def create_graph_with_weights():
    G = nx.Graph()
    G.add_nodes_from(range(len(cities)))
    
    # Generate the weighted links with calculated inverse capacities
    weighted_links = calculate_inverse_capacity(links, predefined_capacities)
    
    # Add the edges with weights to the graph
    for city1, city2, weight in weighted_links:
        G.add_edge(city1, city2, weight=weight)

    return G
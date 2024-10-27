import networkx as nx
import random
import folium
import os
from geopy.geocoders import Nominatim
from dijkstra_Algorithm import dijkstra_algorithm
from IPython.display import IFrame
from selenium import webdriver



save_directory = "/home/suhkth/Documents/Diskret/IX150_HT24_-50140--main/Project3/Project3"


# Initialize geolocator
geolocator = Nominatim(user_agent="sweden_city_locator")

# Define cities in Sweden
cities = ["Abisko", "Boden", "Falun", "Goteborg", "Hoganas", "Hudiksvall", "Jonkoping", 
          "Kalmar", "Kiruna", "Lidkoping", "Linkoping", "Lulea", "Lund", "Malmo", "Mariestad", 
          "Ostersund", "Stockholm", "Strangnas", "Timra", "Uppsala", "Umea", "Varberg", "Visby"]

# Fetch coordinates for each city
city_coordinates = {}
for city in cities:
    location = geolocator.geocode(city + ", Sweden")
    if location:
        city_coordinates[city] = (location.latitude, location.longitude)
    else:
        print(f"Could not find coordinates for {city}")

# Define links (city connections) and some predefined capacities
links = [
    (15, 18), (13, 17), (3, 16), (6, 3), (18, 6), (12, 2), (15, 11), (19, 21), (7, 8),
    (19, 2), (7, 4), (21, 17), (17, 11), (23, 11), (10, 7), (16, 17), (10, 20),
    (13, 5), (3, 17), (7, 22), (15, 10), (16, 18), (11, 16), (17, 23), (18, 17),
    (20, 6), (11, 7), (9, 2), (3, 20), (4, 17), (19, 17), (7, 20), (22, 4), (14, 7),
    (15, 17), (6, 17), (20, 5), (16, 15), (11, 3), (9, 1), (4, 10), (5, 14), (6, 16),
    (16, 19), (13, 8), (8, 23), (16, 10), (4, 13), (2, 16), (15, 3), (20, 18)
]

predefined_capacities = {
    ('Stockholm', 'Goteborg'): 25,
    ('Stockholm', 'Lund'): 30,
    ('Goteborg', 'Lund'): 25,
    ('Stockholm', 'Falun'): 15,
    ('Falun', 'Ostersund'): 15,
    ('Ostersund', 'Umea'): 15
}

# Calculate inverse capacities (weights) for links
def calculate_inverse_capacity(links, predefined_capacities):
    weighted_links = []
    for link in links:
        city1_index, city2_index = link
        city1 = cities[city1_index - 1]  # Adjust to 1-based indexing
        city2 = cities[city2_index - 1]
        
        # Use predefined capacity if available, otherwise assign a random capacity
        if (city1, city2) in predefined_capacities:
            capacity = predefined_capacities[(city1, city2)]
        elif (city2, city1) in predefined_capacities:
            capacity = predefined_capacities[(city2, city1)]
        else:
            capacity = random.randint(1, 10)  # Random capacity for undefined links
        
        weight = 1 / capacity  # Calculate weight as the inverse of capacity
        weighted_links.append((city1_index - 1, city2_index - 1, weight))
    
    return weighted_links

# Create a graph with weighted edges based on the capacities
def create_graph_with_weights():
    G = nx.Graph()
    G.add_nodes_from(range(len(cities)))
    
    weighted_links = calculate_inverse_capacity(links, predefined_capacities)
    
    for city1, city2, weight in weighted_links:
        G.add_edge(city1, city2, weight=weight)

    return G

# Create the graph
G = create_graph_with_weights()

# Run Dijkstra's algorithm and print results
start_node_index = cities.index("Stockholm")  # Convert start_node name to index
shortest_paths = dijkstra_algorithm(G, start_node_index)

# Print distances from Stockholm to each city
for city_index, distance in shortest_paths.items():
    print(f"Distance from Stockholm to {cities[city_index]}: {distance:.3f}")

# Display the map with cities and links
sweden_map = folium.Map(location=[63.0, 18.0], zoom_start=5)
for city, coords in city_coordinates.items():
    folium.Marker(location=coords, popup=city).add_to(sweden_map)

for link in links:
    city1 = cities[link[0] - 1]
    city2 = cities[link[1] - 1]
    if city1 in city_coordinates and city2 in city_coordinates:
        folium.PolyLine(
            locations=[city_coordinates[city1], city_coordinates[city2]],
            color='blue',
            weight=2.5,
            opacity=0.5
        ).add_to(sweden_map)

# Save HTML file in specified directory
html_file = os.path.join(save_directory, 'sweden_cities_map.html')
sweden_map.save(html_file)

# Get the absolute path to the HTML file
html_path = 'file://' + html_file

# Function to save map as PNG
def save_map_as_png(html_path, png_path):
    # Set up Selenium WebDriver
    driver = webdriver.Chrome()
    driver.get(html_path)
    
    # Adjust the window size and take a screenshot
    driver.set_window_size(1024, 1024)
    driver.save_screenshot(png_path)
    
    driver.quit()
    
    # Optionally, show the image
    img = Image.open(png_path)
    img.show()

# Save PNG file in specified directory
png_file = os.path.join(save_directory, 'sweden_cities_map.png')
save_map_as_png(html_path, png_file)

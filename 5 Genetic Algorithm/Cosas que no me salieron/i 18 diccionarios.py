from collections import deque
import random


def random_path(graph, start, end, limit=30):
    path = [start]
    total_time = 0
    attempts = 0
    while path[-1] != end:
        if not graph[path[-1]] or attempts >= limit:
            return None, total_time  # No path found or limit reached
        next_station = random.choice(graph[path[-1]])
        path.append(next_station[0])
        total_time += next_station[1]
        attempts += 1
    return path, total_time


# Complete the graph
graph = {
    "Atlalilco": [("Balderas", 1, '6'), ("Barranca del Muerto", 2, '6')],
    "Balderas": [("Atlalilco", 1, '6')],
    "Barranca del Muerto": [],
    # Add the rest of the stations and their connections
}

start_station = "Balderas"
end_station = "Barranca del Muerto"

# Check if the start and end stations are in the graph
if start_station not in graph:
    print(f"Start station {start_station} not found in the graph.")
elif end_station not in graph:
    print(f"End station {end_station} not found in the graph.")
else:
    path, total_time = random_path(graph, "Balderas", "Barranca del Muerto")
    if path:
        print("Path found:", " -> ".join(path))
        print("Total time:", total_time)
    else:
        print("No path found.")

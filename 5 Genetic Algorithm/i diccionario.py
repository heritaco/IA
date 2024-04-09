graph = {
    'rosario': [0, 6, 0, 0, 0, 0],
    'instituto': [6, 0, 2, 0, 0, 0],
    'la_raza': [0, 2, 0, 3, 3, 3],
    'consulado': [0, 0, 3, 0, 0, 0],
    'deportivo_18_de_marzo': [0, 0, 3, 0, 0, 0]
}


def dijkstra(graph, start, goal):
    shortest_distances = {node: float('infinity') for node in graph.keys()}
    shortest_distances[start] = 0
    unvisited_nodes = list(graph.keys())

    while unvisited_nodes:
        current_node = min(
            unvisited_nodes, key=lambda node: shortest_distances[node])
        unvisited_nodes.remove(current_node)

        if current_node == goal:
            return shortest_distances[goal]

        for neighbor, distance in enumerate(graph[current_node]):
            if distance > 0:  # there is a connection to the neighbor
                new_distance = shortest_distances[current_node] + distance
                if new_distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = new_distance

    return float('infinity')  # there is no path to the goal


distance = dijkstra(graph, 'rosario', 'instituto')
print('The distance from', start, ' to ', goal, 'is', distance)

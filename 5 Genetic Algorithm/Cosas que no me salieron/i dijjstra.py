rosario = [0, 6, 0, 0, 0, 0]
instituto = [6, 0, 2, 0, 0, 0]
la_raza = [0, 2, 0, 3, 3, 3]
consulado = [0, 0, 3, 0, 0, 0]
deportivo_18_de_marzo = [0, 0, 3, 0, 0, 0]


def dijkstra(graph, start, goal):
    shortest_distances = {node: float('infinity')
                          for node in range(len(graph))}
    shortest_distances[start] = 0
    unvisited_nodes = list(range(len(graph)))

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


graph = [rosario, instituto, la_raza, consulado,
         deportivo_18_de_marzo]

start_node = graph.index(rosario)  # index of rosario
goal_node = graph.index(la_raza)  # index of instituto

distance = dijkstra(graph, start_node, goal_node)

print('the distance from', 'rosario', ' to ', ' la raza', 'is', distance)

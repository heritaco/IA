from collections import deque
import random
from typing import Callable, List, Tuple

# Complete the graph
graph = {
    "Atlalilco": [("Balderas", 1, 'line a'), ("Barranca del Muerto", 2, 'line b')],
    "Balderas": [("Atlalilco", 1, 'line c')],
    "Barranca del Muerto": [],
    # Add the rest of the stations and their connections
}

start_station = "Balderas"
end_station = "Barranca del Muerto"
limit_genome = 30
size_population = 10
n_parents = 2
n_generations = 100

Genome = List[Tuple[str, int]]
Population = List[Genome]
Fintess_func = Callable[[Genome], float]


def generate_genome(graph, start, end, limit_genome) -> Genome:
    path = [(start, '')]  # Start station has no '6'
    total_time = 0
    attempts = 0
    while path[-1][0] != end:
        if not graph[path[-1][0]] or attempts >= limit_genome:
            return None, total_time  # No path found or limit reached
        next_station = random.choice(graph[path[-1][0]])
        # Include 'line 6' in path
        path.append((next_station[0], next_station[2]))
        total_time += next_station[1]
        attempts += 1
    return path, total_time


def generate_population(graph, start, end, limit_genome, size_population) -> Population:
    return [generate_genome(graph, start, end, limit_genome) for _ in range(size_population)]


def fitness(genome: Genome) -> float:
    if genome[1] == 0:  # Prevent division by zero
        return float('inf')  # Maximum fitness for zero time
    return 1 / genome[1]


def select_parents(population: Population, Fitness_func, n_parents: int) -> List[Genome]:
    return random.choices(
        population=population,
        weights=[Fitness_func(genome)],
        k=n_parents
    )


def single_point_crossover(parents: Tuple[Genome, Genome]) -> Tuple[Genome, Genome]:

def crossover(parents: Tuple[Genome, Genome]) -> Tuple[Genome, Genome]:
    parent1, parent2 = parents
    if len(parent1[0]) < 2 or len(parent2[0]) < 2:  # Prevent empty crossover
        return parent1, parent2
    crossover_point = random.randint(
        1, min(len(parent1[0]), len(parent2[0])) - 1)
    child1 = parent1[0][:crossover_point] + parent2[0][crossover_point:]
    child2 = parent2[0][:crossover_point] + parent1[0][crossover_point:]
    total_time1 = sum(graph[station[0]][0][1] for station in child1 if isinstance(
        station, tuple) and graph[station[0]])  # Calculate total time
    total_time2 = sum(graph[station[0]][0][1] for station in child2 if isinstance(
        station, tuple) and graph[station[0]])  # Calculate total time
    return (child1, total_time1), (child2, total_time2)


def mutate(genome: Genome, graph, start, end, limit_genome) -> Genome:
    mutated_genome = genome[0].copy()  # Corrected to genome[0]
    mutation_point = random.randint(0, len(mutated_genome) - 1)
    mutated_genome[mutation_point] = random.choice(
        graph[mutated_genome[mutation_point][0]])
    total_time = sum(station[1] for station in mutated_genome if isinstance(
        station, tuple))  # Calculate total time
    return mutated_genome, total_time  # Corrected to return total time


# Generate a population
population = generate_population(
    graph, start_station, end_station, limit_genome, size_population)

# Calculate fitness for each genome in the population
fitness_scores = [fitness(genome) for genome in population]

# Find the genome with the highest fitness
best_genome, best_time = max(population, key=lambda genome: fitness(genome))


# Run the genetic algorithm for a certain number of generations
for _ in range(n_generations):
    # Calculate fitness for each genome in the population
    fitness_scores = [fitness(genome) for genome in population]

    # Select parents
    parents = select_parents(population, fitness_scores, n_parents)

    # Perform crossover and mutation to generate a new population
    population = [mutate(crossover([parents[random.randint(0, n_parents - 1)] for _ in range(2)]), graph, start_station,
                         end_station, limit_genome) for _ in range(size_population)]

    # Find the genome with the highest fitness
    best_genome, best_time = max(
        population, key=lambda genome: fitness(genome))

    # Print all genomes in the population
    for genome in population:
        print(genome)

    # Print the total time for the best genome
    print(best_time)

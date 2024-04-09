from collections import deque
import random
from typing import List, Tuple

# Complete the graph
graph = {
    "Atlalilco": [("Balderas", 1, '6'), ("Barranca del Muerto", 2, '6')],
    "Balderas": [("Atlalilco", 1, '6')],
    "Barranca del Muerto": [],
    # Add the rest of the stations and their connections
}


start_station = "Balderas"
end_station = "Barranca del Muerto"
limit_genome = 30
size_population = 5
n_parents = 2

Genome = List[Tuple[str, int]]
Population = List[Genome]


def fitness(genome: Genome) -> float:
    if genome[1] == 0:  # Prevent division by zero
        return float('inf')  # Maximum fitness for zero time
    return 1 / genome[1]

def generate_genome(graph, start, end, limit_genome) -> Genome:
    path = [(start, '')]  # Start station has no '6'
    total_time = 0
    attempts = 0
    while path[-1][0] != end:
        if not graph[path[-1][0]] or attempts >= limit_genome:
            return None, total_time  # No path found or limit reached
        next_station = random.choice(graph[path[-1][0]])
        path.append((next_station[0], next_station[2]))  # Include '6' in path
        total_time += next_station[1]
        attempts += 1
    return path, total_time


genome = generate_genome(graph, start_station, end_station, limit_genome)
print(genome)


def generate_population(graph, start, end, limit_genome, size_population) -> Population:
    return [generate_genome(graph, start, end, limit_genome) for _ in range(size_population)]





print(fitness(genome))


def select_parents(population: Population, fitnesses: List[float], n_parents: int) -> List[Genome]:
    total_fitness = sum(fitnesses)
    probabilities = [fitness / total_fitness for fitness in fitnesses]
    parents = random.choices(population, weights=probabilities, k=n_parents)
    return parents


def crossover(parents: List[Genome]) -> Genome:
    child = []
    for i in range(len(parents[0])):
        child.append(random.choice([parents[0][i], parents[1][i]]))
    return child


def mutate(genome: Genome, graph, start, end, limit_genome) -> Genome:
    mutated_genome = genome.copy()
    mutation_point = random.randint(0, len(genome) - 1)
    mutated_genome[mutation_point] = random.choice(
        graph[mutated_genome[mutation_point][0]])
    return mutated_genome


# Generate a population
population = generate_population(
    graph, start_station, end_station, limit_genome, size_population)

# Calculate fitness for each genome in the population
fitness_scores = [fitness(genome) for genome in population]

# Find the genome with the highest fitness
best_genome, best_time = max(population, key=lambda genome: fitness(genome))

# Print the path for the best genome
print(best_genome)
print(best_time)

print(Genome)

# Print all genomes in the population
for genome in population:
    print(genome)

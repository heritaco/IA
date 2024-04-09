"""FC3 Genetic Alorithm from El Rosario to Consulado"""

import matplotlib.pyplot as plt
import random
from typing import List, Tuple


class Ruta:
    """Clase para representar una ruta entre dos puntos de la ciudad"""

    def __init__(self, puntoa: str, puntob: str, time: int, linea: str):
        # Use a set to represent the two endpoints
        self.puntos = {puntoa, puntob}
        self.time = time
        self.linea = linea

    def __str__(self):
        return f'Ruta: {self.puntos} (Linea {self.linea})'


estaciones = [
    "Atlalilco",          # 0
    "Balderas",           # 1
    "Barranca del Muerto",  # 2
    "Bellas Artes",       # 3
    "Candelaria",         # 4
    "Centro Médico",      # 5
    "Chabacano",          # 6
    "Ciudad Azteca",      # 7
    "Consulado",          # 8
    "Cuatro Caminos",     # 9
    "Deportivo 18 de Marzo",  # 10
    "El Rosario",         # 11
    "Ermita",             # 12
    "Garibaldi",          # 13
    "Gomez Farias",       # 14
    "Guerrero",           # 15
    "Hidalgo",            # 16
    "Indios Verdes",      # 17
    "Instituto del Petroleo",  # 18
    "Jamaica",            # 19
    "La Raza",            # 20
    "Martin Carrera",     # 21
    "Mixcoac",            # 22
    "Morelos",            # 23
    "Oceania",            # 24
    "Pantitlan",          # 25
    "Pino Suárez",        # 26
    "Politécnico",        # 27
    "Salto del Agua",     # 28
    "San Lázaro",         # 29
    "Tacuba",             # 30
    "Tacubaya",           # 31
    "Tasqueña",           # 32
    "Tláhuac",            # 33
    "Universidad",        # 34
    "Zapata"              # 35
]


rutas = [
    Ruta(estaciones[1], estaciones[2], 1, '6'),
    Ruta(estaciones[2], estaciones[3], 1, '6'),
    Ruta(estaciones[3], estaciones[4], 1, '6'),
    Ruta(estaciones[4], estaciones[5], 1, '6'),
    Ruta(estaciones[5], estaciones[6], 1, '6'),
    Ruta(estaciones[6], estaciones[7], 1, '6'),
    Ruta(estaciones[7], estaciones[8], 1, '6'),
    Ruta(estaciones[8], estaciones[9], 1, '6'),
    Ruta(estaciones[9], estaciones[10], 1, '6'),
    Ruta(estaciones[10], estaciones[11], 1, '6'),
    Ruta(estaciones[11], estaciones[12], 1, '6'),
    Ruta(estaciones[12], estaciones[13], 1, '6'),
    Ruta(estaciones[13], estaciones[14], 1, '6'),
    Ruta(estaciones[14], estaciones[15], 1, '6'),
    Ruta(estaciones[15], estaciones[16], 1, '6'),
    Ruta(estaciones[16], estaciones[17], 1, '6'),
    Ruta(estaciones[17], estaciones[18], 1, '6'),
    Ruta(estaciones[18], estaciones[19], 1, '6'),
    Ruta(estaciones[19], estaciones[20], 1, '6'),
    Ruta(estaciones[20], estaciones[21], 1, '6'),
    Ruta(estaciones[21], estaciones[22], 1, '6'),
    Ruta(estaciones[22], estaciones[23], 1, '6'),
    Ruta(estaciones[23], estaciones[24], 1, '6'),
    Ruta(estaciones[24], estaciones[25], 1, '6'),
    Ruta(estaciones[25], estaciones[26], 1, '6'),
    Ruta(estaciones[26], estaciones[27], 1, '6'),
    Ruta(estaciones[27], estaciones[28], 1, '6'),
    Ruta(estaciones[28], estaciones[29], 1, '6'),
    Ruta(estaciones[29], estaciones[30], 1, '6'),
    Ruta(estaciones[30], estaciones[31], 1, '6'),
    Ruta(estaciones[31], estaciones[32], 1, '6'),
    Ruta(estaciones[32], estaciones[33], 1, '6'),
    Ruta(estaciones[33], estaciones[34], 1, '6'),
    Ruta(estaciones[34], estaciones[35], 1, '6'),
    Ruta(estaciones[35], estaciones[0], 1, '6'),
    Ruta(estaciones[0], estaciones[1], 1, '6'),
]


start_point = 'El Rosario'
end_point = 'Consulado'
size_pop = 5
size_genome = 100
num_generations = 1000
# Genome

Genome = Tuple[List[int], int, List[str], List[Tuple[str, str]]]
# List of indexes, time, lineas, stages


def generate_genome(rutas: List[Ruta], start_point: str, end_point: str) -> Genome:
    current_point = start_point
    indexes = []
    selected_routes = []
    while current_point != end_point:
        available_routes = [i for i, ruta in enumerate(
            rutas) if current_point in ruta.puntos]
        if not available_routes:
            raise ValueError(f"No available routes from {current_point}")
        i = random.choice(available_routes)
        indexes.append(i)
        selected_routes.append(rutas[i])
        current_point = next(iter(rutas[i].puntos - {current_point}))
        # Remove the selected route from the list of routes to avoid loops
        rutas = [ruta for j, ruta in enumerate(rutas) if j != i]
    time = sum(route.time for route in selected_routes)
    lineas = [route.linea for route in selected_routes]
    stages = [(route.puntos - {current_point}) for route in selected_routes]
    return indexes, time, lineas, stages


# Population
Population = List[Genome]


def generate_population(rutas: List[Ruta], size_pop) -> Population:
    """function to generate a population of genomes"""
    return [generate_genome(rutas, start_point, end_point) for _ in range(size_pop)]


def calculate_distance(start: str, end: str, genome: Genome, rutas: List[Ruta]) -> Tuple[str, int]:
    """function to calculate the distance between two points in the city and the path to follow to get from one to the other"""
    total_time = 0
    current_station = start
    path = []
    for i in genome[0]:  # genome[0] is the list of indices
        ruta = rutas[i]
        current_point = next(iter(ruta.puntos - {current_station}))
        if current_point != current_station:
            total_time += ruta.time
            current_station = current_point
            path.append((ruta.linea, current_station))
        if current_station == end:
            break
    else:  # If the loop didn't break, the path doesn't reach the destination
        return "", float('inf')  # Return infinite distance

    path_str = f"De {start} a {end} tarde {total_time}\nEl camino es\n "
    for paths in path:
        path_str += f"De {start} a {paths[1]} con la linea {paths[0]}\n "
        start = paths[1]
    return path_str, total_time


def fitness(genome: Genome, rutas: List[Ruta]) -> float:
    """function to calculate the fitness of a genome"""
    value = 1/calculate_distance(start_point, end_point, genome, rutas)[1]
    return value


# Generate a population
population = generate_population(rutas, size_pop)

# Calculate fitness for each genome in the population
for genome in population:
    fit = fitness(genome, rutas)
# Find the genome with the highest fitness
best_genome = max(population, key=lambda genome: fitness(genome, rutas))

# Print the path for the best genome
path, total_time = calculate_distance(
    start_point, end_point, best_genome, rutas)
print(path)


def mutate_genome(genome: Genome, rutas: List[Ruta]) -> Genome:
    """function to mutate a genome"""
    indexes, time, lineas, stages = genome
    index = random.randint(0, len(indexes) - 1)
    new_index = random.randint(0, len(rutas) - 1)
    indexes[index] = new_index
    time = sum(rutas[i].time for i in indexes)
    lineas = [rutas[i].linea for i in indexes]
    stages = [tuple(rutas[i].puntos) for i in indexes]  # Changed this line
    return indexes, time, lineas, stages


def crossover_genomes(genome1: Genome, genome2: Genome) -> Genome:
    """function to crossover two genomes"""
    indexes1, time1, lineas1, stages1 = genome1
    indexes2, time2, lineas2, stages2 = genome2
    crossover_point = random.randint(1, len(indexes1) - 1)
    new_indexes = indexes1[:crossover_point] + indexes2[crossover_point:]
    new_time = sum(rutas[i].time for i in new_indexes)
    new_lineas = [rutas[i].linea for i in new_indexes]
    new_stages = [tuple(rutas[i].puntos)
                  for i in new_indexes]  # Changed this line
    return new_indexes, new_time, new_lineas, new_stages


def evolve_population(population: Population, rutas: List[Ruta], tournament_size: int = 5, mutation_rate: float = 0.25) -> Population:
    """function to evolve a population of genomes"""
    new_population = []
    while len(new_population) < len(population):
        # Select individuals for the tournament
        tournament = random.sample(population, tournament_size)
        # Select the best individual
        parent1 = max(tournament, key=lambda genome: fitness(genome, rutas))
        # Repeat the process for the second parent
        tournament = random.sample(population, tournament_size)
        parent2 = max(tournament, key=lambda genome: fitness(genome, rutas))
        # Generate a child through crossover
        child = crossover_genomes(parent1, parent2)
        # Mutate the child
        if random.random() < mutation_rate:
            child = mutate_genome(child, rutas)
        # Add the child to the new population
        new_population.append(child)
    return new_population


# Evolve the population for a certain number of generations

# Evolve the population for a certain number of generations
best_times = []  # List to store the best time of each generation
for i in range(num_generations):
    # Evolve the population and replace the old population with the new one
    population = evolve_population(population, rutas)
    # Print the entire population
    print(f"Generation {i + 1}:")
    for genome in population:
        path, total_time = calculate_distance(
            'El Rosario', 'Consulado', genome, rutas)
        print(path)
    # Find the genome with the highest fitness
    best_genome = max(population, key=lambda genome: fitness(genome, rutas))
    # Calculate the time for the best genome and add it to the list
    _, total_time = calculate_distance(
        'El Rosario', 'Consulado', best_genome, rutas)
    best_times.append(total_time)

# Print the path for the best genome
path, total_time = calculate_distance(
    'El Rosario', 'Consulado', best_genome, rutas)
print(path)

# Print the best time of each generation
print(best_times)


# Generate x-axis values (generations)
generations = range(1, num_generations + 1)

# Plot the best times
plt.plot(generations, best_times)
plt.xlabel('Generation')
plt.ylabel('Best Time')
plt.title('Best Time Evolution')
plt.show()

# Print out the routes data to check its contents
print(rutas)

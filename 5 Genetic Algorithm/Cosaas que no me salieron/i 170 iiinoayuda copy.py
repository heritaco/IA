"""FC3 Genetic Alorithm from El Rosario to Consulado"""

import random
from typing import List, Tuple


class Ruta:
    """Clase para representar una ruta entre dos puntos de la ciudad"""

    def __init__(self, puntoa: str, puntob: str, time: int, linea: str):
        self.puntoa = puntoa
        self.puntob = puntob
        self.time = time
        self.linea = linea

    def __str__(self):
        return f'Ruta: {self.puntoa} <-> {self.puntob} (Linea {self.linea})'


estaciones = ["Atlalilco",          # 0
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
              "Gómez Farías",       # 14
              "Guerrero",           # 15
              "Hidalgo",            # 16
              "Indios Verdes",      # 17
              "Instituto del Petroleo",  # 18
              "Jamaica",            # 19
              "La Raza",            # 20
              "Martín Carrera",     # 21
              "Mixcoac",            # 22
              "Morelos",            # 23
              "Oceanía",            # 24
              "Pantitlán",          # 25
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


rutas = [Ruta(estaciones[11], estaciones[18], 100, '6'),
         Ruta(estaciones[11], estaciones[12], 10, '6'),
         Ruta(estaciones[12], estaciones[8], 1, '6'),
         Ruta(estaciones[11], estaciones[1], 1, '6'),
         Ruta(estaciones[1], estaciones[8], 1, '6'),
         Ruta(estaciones[11], estaciones[16], 10, '6'),
         Ruta(estaciones[16], estaciones[8], 3, '6'),
         Ruta(estaciones[18], estaciones[20], 1, '5'),
         Ruta(estaciones[20], estaciones[8], 1, '5'),
         Ruta(estaciones[20], estaciones[10], 3, '5')]


start_point = 'El Rosario'
end_point = 'Consulado'
size_pop = 5
size_genome = 100
num_generations = 10
# Genome

Genome = Tuple[List[int], int, List[str], List[Tuple[str, str]]]
# List of indexes, time, lineas, stages


def generate_genome(rutas: List[Ruta], start_point: str, end_point: str) -> Genome:
    current_point = start_point
    indexes = []
    while current_point != end_point:
        available_routes = [i for i, ruta in enumerate(
            # Check if the current point is in the set of endpoints
            rutas) if current_point in {ruta.puntoa, ruta.puntob}]
        if not available_routes:
            raise ValueError(f"No available routes from {current_point}")
        i = random.choice(available_routes)
        indexes.append(i)
        # Get the other endpoint
        ruta = rutas[i]  # Access the Ruta object at index i
        current_point = ruta.puntob if ruta.puntoa == current_point else ruta.puntoa
    time = sum(rutas[i].time for i in indexes)
    lineas = [rutas[i].linea for i in indexes]
    stages = [(rutas[i].puntoa, rutas[i].puntob) for i in indexes]
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
        if ruta.puntoa == current_station:
            total_time += ruta.time
            current_station = ruta.puntob
            path.append((ruta.linea, ruta.puntoa, ruta.puntob))
        if current_station == end:
            break
    else:  # If the loop didn't break, the path doesn't reach the destination
        return "", float('inf')  # Return infinite distance

    path_str = f"De {start} a {end} tarde {total_time}\nEl camino es\n "
    for paths in path:
        path_str += f"De {paths[1]} a {paths[2]} con la linea {paths[0]}\n "
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
    stages = [(rutas[i].puntoa, rutas[i].puntob) for i in indexes]
    return indexes, time, lineas, stages


def crossover_genomes(genome1: Genome, genome2: Genome) -> Genome:
    """function to crossover two genomes"""
    indexes1, time1, lineas1, stages1 = genome1
    indexes2, time2, lineas2, stages2 = genome2
    crossover_point = random.randint(1, len(indexes1) - 1)
    new_indexes = indexes1[:crossover_point] + indexes2[crossover_point:]
    new_time = sum(rutas[i].time for i in new_indexes)
    new_lineas = [rutas[i].linea for i in new_indexes]
    new_stages = [(rutas[i].puntoa, rutas[i].puntob) for i in new_indexes]
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

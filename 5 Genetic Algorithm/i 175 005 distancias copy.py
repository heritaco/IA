
"""FC3 Genetic Alorithm from El Rosario to Consulado"""

import random
from typing import List, Tuple
from typing import Tuple, List
import random



class Ruta:
    """Clase para representar una ruta entre dos puntos de la ciudad"""
    def __init__(self, a: str, b: str, time: int, linea: str):
        self.start = a
        self.end = b
        self.time = time
        self.linea = linea

    def __str__(self):
        return f'Ruta: de {self.start} a {self.end} (Linea {self.linea})'

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


start_point = 'Balderas'
end_point = 'Consulado'
size_pop = 5
num_generations = 10
elite_size = 2
# Genome


rutas = [
    Ruta(estaciones[3], estaciones[8], 1, '1'),
    Ruta(estaciones[2], estaciones[12], 10, '2'),
    Ruta(estaciones[2], estaciones[3], 1, '3'),
    Ruta(estaciones[2], estaciones[8], 100, '4'),
    Ruta(estaciones[1], estaciones[2], 1, '5'),
    Ruta(estaciones[11], estaciones[16], 10, '6'),
    Ruta(estaciones[16], estaciones[8], 3, '7'),
    Ruta(estaciones[18], estaciones[20], 1, '8'),
    Ruta(estaciones[20], estaciones[8], 1, '9'),
    Ruta(estaciones[20], estaciones[10], 3, '10')]
        
Genome = Tuple[List[int], int, List[str], List[Tuple[str, str]]]
# List of indexes, time, lineas, stages
# Population
Population = List[Genome]
        

def generate_genome(rutas: List[Ruta], start_point: str, end_point: str) -> Genome:
    current_point = start_point
    indexes = []
    stages = []
    while current_point != end_point:
        available_routes = [i for i, ruta in enumerate(rutas) if current_point == ruta.start]
        if not available_routes:
            raise ValueError(f"No available routes from {current_point}")
        i = random.choice(available_routes)
        indexes.append(i)
        next_point = rutas[i].end
        stages.append((current_point, next_point))
        current_point = next_point
    time = sum(rutas[i].time for i in indexes)
    lineas = [rutas[i].linea for i in indexes]
    genome_str = f" El tiempo fue de: {time}, Rutas disponibles tomadas: {indexes}, Las estaciones fueron de: {stages}, en las lineas: {lineas},"
    return indexes, time, lineas, stages, genome_str

def generate_population(rutas: List[Ruta], size_pop) -> Population:
    """function to generate a population of genomes"""
    return [generate_genome(rutas, start_point, end_point) for _ in range(size_pop)]
population = generate_population(rutas, size_pop)

def fitness(genome: Genome, rutas: List[Ruta]) -> float:
    """function to calculate the fitness of a genome"""
    time = genome[1]  # genome[1] is the total time
    value = 1/time if time != 0 else 0  # Avoid division by zero
    return value

def mutate_genome(genome: Genome, rutas: List[Ruta], start_point: str, end_point: str) -> Genome:
    """function to mutate a genome"""
    # Choose a random index to mutate
    index_to_mutate = random.randint(1, len(genome[0]) - 3)
    new_start_point = rutas[genome[0][index_to_mutate - 1]].end
    # Generate a new route
    new_route = generate_genome(rutas, new_start_point, end_point)
    # Create the new genome
    new_genome = list(genome)
    new_genome[0] = new_genome[0][:index_to_mutate] + new_route[0]
    new_genome[1] = sum(rutas[i].time for i in new_genome[0])
    new_genome[2] = [rutas[i].linea for i in new_genome[0]]
    new_genome[3] = [(rutas[i].start, rutas[i].end) for i in new_genome[0]]
    new_genome[4] = f" El tiempo fue de: {new_genome[1]}, Rutas disponibles tomadas: {new_genome[0]}, Las estaciones fueron de: {new_genome[3]}, en las lineas: {new_genome[2]},"
    return tuple(new_genome)

def elitism(population: Population, rutas: List[Ruta], elite_size: int) -> Population:
    """function to carry over the top individuals to the next generation"""
    fitness_values = [(genome, fitness(genome, rutas)) for genome in population]
    sorted_by_fitness = sorted(fitness_values, key=lambda x: x[1], reverse=True)
    elite = [genome for genome in sorted_by_fitness[:elite_size]]
    return elite


mutation_rate = 0.0
def create_new_population(population: Population, rutas: List[Ruta], elite_size: int, mutation_rate: float) -> Population:
    """function to create a new population"""
    # Select the elite individuals
    elite, fitness_values, sorted_by_fitness = elitism(population, rutas, elite_size)
    random_genomes = [generate_genome(rutas, start_point, end_point) for _ in range(size_pop - len(elite))]
    new_population = list(elite) + random_genomes
    return new_population

new_population = create_new_population(population, rutas, elite_size, mutation_rate)

print("\nNew population:")
for genome in new_population:
    print(genome)

print("\nOriginal population:")
elite = elitism(population, rutas, elite_size)
print(elite)

print("Size of the new population:", len(new_population))
print("Size of the original population:", len(population))


def genetic_algorithm(rutas: List[Ruta], population: Population, num_generations: int, elite_size: int, mutation_rate: float):
    """function to run the genetic algorithm"""
    for _ in range(num_generations):
        # Create a new population
        population = create_new_population(population, rutas, elite_size, mutation_rate)
        
        # Mutate the population
        for i in range(len(population)):
            if random.random() < mutation_rate:
                population[i] = mutate_genome(population[i], rutas, start_point, end_point)
                
    # Return the final population
    return population

# Run the genetic algorithm
final_population = genetic_algorithm(rutas, population, num_generations, elite_size, mutation_rate)

# Print the final population
print("\nFinal population:")
for genome in final_population:
    print(genome)

# Print the best genome
best_genome = max(final_population, key=lambda genome: fitness(genome, rutas))
print("\nBest genome:")
print(best_genome)
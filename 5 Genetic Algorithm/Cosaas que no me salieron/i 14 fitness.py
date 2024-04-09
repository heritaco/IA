"""FC3 Genetic Alorithm"""

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


rutas = [Ruta(estaciones[11], estaciones[18], 6, '6'),
         Ruta(estaciones[11], estaciones[8], 6, '6'),
         Ruta(estaciones[18], estaciones[20], 2, '5'),
         Ruta(estaciones[20], estaciones[8], 3, '5'),
         Ruta(estaciones[20], estaciones[10], 3, '5')]


def calculate_distance(start: str, end: str, rutas: List[Ruta]) -> Tuple[str, int]:
    """Calcula la distancia entre dos puntos de la ciudad y la ruta a seguir para llegar de uno a otro"""
    total_time = 0
    current_station = start
    path = []
    while current_station != end:
        for ruta in rutas:
            if ruta.puntoa == current_station:
                total_time += ruta.time
                current_station = ruta.puntob
                path.append((ruta.linea, ruta.puntoa, ruta.puntob))
                break

    path_str = f"De {start} a {end} tarde {total_time}\nEl camino es\n "
    for paths in path:
        path_str += f"De {paths[1]} a {paths[2]} con la linea {paths[0]}\n "
    return path_str, total_time


class Genome:
    """Class to represent a genome for the genetic algorithm."""

    def __init__(self, start: str, end: str, rutas: List[Ruta]):
        self.ruta = self.generate_path(start, end, rutas)

    def generate_path(self, start: str, end: str, rutas: List[Ruta]) -> List[Ruta]:
        """Generate a valid path from start to end."""
        path = []
        current_station = start
        while current_station != end:
            valid_rutas = [
                ruta for ruta in rutas if ruta.puntoa == current_station]
            if not valid_rutas:
                break
            ruta = random.choice(valid_rutas)
            path.append(ruta)
            current_station = ruta.puntob
        return path

    def fitness(self) -> int:
        """Calculate the fitness of this genome."""
        total_time = sum(ruta.time for ruta in self.ruta)
        return total_time

    def __str__(self):
        """Return a string representation of this genome."""
        return ' -> '.join(str(ruta) for ruta in self.ruta)


def selection(population: List[Genome]) -> Tuple[Genome, Genome]:
    """Select two genomes from the population for reproduction."""
    return random.choice(population), random.choice(population)


def crossover(parent1: Genome, parent2: Genome, start: str, end: str, rutas: List[Ruta]) -> Genome:
    """Create a new genome by combining parts of two parent genomes."""
    crossover_point = random.randint(0, len(parent1.ruta))
    child_ruta = parent1.ruta[:crossover_point] + \
        parent2.ruta[crossover_point:]
    child_genome = Genome(start, end, child_ruta)
    return child_genome


def mutation(genome: Genome, start: str, end: str, rutas: List[Ruta]) -> Genome:
    """Randomly alter a genome."""
    mutation_point = random.randint(0, len(genome.ruta) - 1)
    new_ruta = random.choice(
        [ruta for ruta in rutas if ruta.puntoa == genome.ruta[mutation_point].puntoa])
    genome.ruta[mutation_point] = new_ruta
    return Genome(start, end, genome.ruta)


def genetic_algorithm(population: List[Genome], generations: int, start: str, end: str, rutas: List[Ruta]) -> Genome:
    """Run the genetic algorithm."""
    for _ in range(generations):
        population = sorted(population, key=lambda genome: genome.fitness())
        next_generation = population[:2]  # keep the best 2 genomes
        for _ in range(len(population) // 2 - 1):
            parent1, parent2 = selection(population)
            child1 = crossover(parent1, parent2, start, end, rutas)
            child2 = crossover(parent1, parent2, start, end, rutas)
            next_generation += [mutation(child1, start, end, rutas),
                                mutation(child2, start, end, rutas)]
        population = next_generation
    # return the best genome
    return min(population, key=lambda genome: genome.fitness())


# Usage
path_str, total_time = calculate_distance('El Rosario', 'Consulado', rutas)
print(path_str)
print(total_time)


# Create an initial population
population = []
for _ in range(100):  # population size
    random.shuffle(rutas)
    population.append(Genome('El Rosario', 'Consulado', rutas[:]))

# Run the genetic algorithm
best_genome = genetic_algorithm(
    population, 100, 'El Rosario', 'Consulado', rutas)  # number of generations

# Print the best path found
print(best_genome)

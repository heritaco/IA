from typing import List, Tuple
import random


class Ruta:
    def __init__(self, puntoa: str, puntob: str, time: int, linea: str):
        self.puntoa = puntoa
        self.puntob = puntob
        self.time = time
        self.linea = linea

    def __str__(self):
        return f'Ruta: {self.puntoa} <-> {self.puntob} (Linea {self.linea})'


estaciones = ['El Rosario', 'Instituto', 'La Raza',
              'Consulado', 'Deportivo 18 de Marzo']

rutas = [Ruta(estaciones[0], estaciones[1], 6, '6'),
         Ruta(estaciones[0], estaciones[3], 6, '6'),
         Ruta(estaciones[1], estaciones[2], 2, '5'),
         Ruta(estaciones[2], estaciones[3], 3, '5'),
         Ruta(estaciones[2], estaciones[4], 3, '5')]


def calculate_distance(start: str, end: str, rutas: List[Ruta]) -> Tuple[str, int]:
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


# Usage
path_str, total_time = calculate_distance('El Rosario', 'Consulado', rutas)
print(path_str)
print(total_time)


def create_individual(rutas):
    return random.sample(rutas, len(rutas))


def calculate_fitness(individual):
    path_str, total_time = calculate_distance(
        'El Rosario', 'Consulado', individual)
    return total_time


def crossover(parent1, parent2):
    crossover_point = random.randint(1, len(parent1) - 1)
    child = parent1[:crossover_point] + parent2[crossover_point:]
    return child


def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            random_index = random.randint(0, len(individual) - 1)
            individual[i], individual[random_index] = individual[random_index], individual[i]
    return individual


def genetic_algorithm(rutas, population_size, mutation_rate, generations):
    population = [create_individual(rutas) for _ in range(population_size)]

    for _ in range(generations):
        fitness_scores = [calculate_fitness(
            individual) for individual in population]
        sorted_population = [individual for _, individual in sorted(
            zip(fitness_scores, population))]
        new_population = sorted_population[:population_size // 2]

        while len(new_population) < population_size:
            parent1 = random.choice(sorted_population)
            parent2 = random.choice(sorted_population)
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    best_individual = population[0]
    best_fitness = calculate_fitness(best_individual)
    return best_individual, best_fitness


best_individual, best_fitness = genetic_algorithm(
    rutas, population_size=100, mutation_rate=0.01, generations=100)
print(f"Best individual: {best_individual}")
print(f"Best fitness: {best_fitness}")

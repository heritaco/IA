import random
from typing import List, Tuple
from rutas import estaciones, rutas
from values import start_point, end_point, size_pop, num_generations, elite_size, mutation_rate
import matplotlib.pyplot as plt

class Ruta:
    def __init__(self, a: str, b: str, time: int, linea: str):
        self.start, self.end, self.time, self.linea = a, b, time, linea

Genome = Tuple[List[int], int, List[str], List[Tuple[str, str]]]

def generate_genome(rutas: List[Ruta], start_point: str, end_point: str) -> Genome:
    current_point, indexes, stages = start_point, [], []
    while current_point != end_point:
        i = random.choice([i for i, ruta in enumerate(rutas) if current_point == ruta.start])
        indexes.append(i)
        stages.append((current_point, rutas[i].end))
        current_point = rutas[i].end
    time = sum(rutas[i].time for i in indexes)
    lineas = [rutas[i].linea for i in indexes]
    return indexes, time, lineas, stages

def generate_population(rutas: List[Ruta], size_pop) -> List[Genome]:
    return [generate_genome(rutas, start_point, end_point) for _ in range(size_pop)]

def fitness(genome: Genome, rutas: List[Ruta]) -> float:
    return 1/genome[1] if genome[1] != 0 else 0

def elitism(population: List[Genome], rutas: List[Ruta], elite_size: int) -> List[Genome]:
    return sorted(population, key=lambda genome: fitness(genome, rutas), reverse=True)[:elite_size]

def mutate_genome(genome: Genome, rutas: List[Ruta], start_point: str, end_point: str) -> Genome:
    index_to_mutate = random.randint(1, len(genome[0]) - 1)
    new_start_point = rutas[genome[0][index_to_mutate - 1]].end
    new_route = generate_genome(rutas, new_start_point, end_point)
    new_genome = list(genome)
    new_genome[0] = new_genome[0][:index_to_mutate] + new_route[0]
    new_genome[1] = sum(rutas[i].time for i in new_genome[0])
    new_genome[2] = [rutas[i].linea for i in new_genome[0]]
    new_genome[3] = [(rutas[i].start, rutas[i].end) for i in new_genome[0]]
    return tuple(new_genome)

def create_new_population(population: List[Genome], rutas: List[Ruta], elite_size: int, mutation_rate: float) -> List[Genome]:
    elite = elitism(population, rutas, elite_size)
    random_genomes = [generate_genome(rutas, start_point, end_point) for _ in range(size_pop - len(elite))]
    return elite + random_genomes

def genetic_algorithm(rutas: List[Ruta], population: List[Genome], num_generations: int, elite_size: int, mutation_rate: float):
    best_times = []
    for _ in range(num_generations):
        population = create_new_population(population, rutas, elite_size, mutation_rate)
        for i in range(len(population)):
            if random.random() < mutation_rate:
                population[i] = mutate_genome(population[i], rutas, start_point, end_point)
        best_genome = max(population, key=lambda genome: fitness(genome, rutas))
        best_times.append(1/best_genome[1] if best_genome[1] < 1 else best_genome[1])
    return population, best_times

population = generate_population(rutas, size_pop)
final_population, best_times = genetic_algorithm(rutas, population, num_generations, elite_size, mutation_rate)

plt.plot(best_times)
plt.title('Best time in each generation')
plt.xlabel('Generation')
plt.ylabel('Best time')
plt.show()
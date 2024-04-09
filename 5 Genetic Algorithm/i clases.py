class Ruta:
    def __init__(self, puntoa: str, puntob: str, time: int, linea: str):
        self.puntoa = puntoa
        self.puntob = puntob
        self.time = time
        self.linea = linea

    def __str__(self):
        return f'Ruta: {self.puntoa} <-> {self.puntob} (Linea {self.linea})'
    

estaciones = ['el rosatio', 'instituto', 'la raza', 'consulado', 'deportivo 18 de marzo']



rutas = [Ruta(estaciones[0], estaciones[1], 6, '6'),
         Ruta(estaciones[1], estaciones[2], 2, '5'),
         Ruta(estaciones[2], estaciones[3], 3, '5'),
         Ruta(estaciones[2], estaciones[4], 3, '5')]

for cada_ruta in rutas:
    print(cada_ruta.puntoa)


rosario = [0, 6, 0, 0, 0, 0, 0, 0, 0]
instituto = [6, 0, 2, 0, 0, 0, 0, 0, 0]
la_raza = [0, 2, 0, 3, 3, 3, 0, 0, 0]
consulado = [0, 0, 3, 0, 0, 0, 0, 0, 0]
deportivo_18_de_marzo = [0, 0, 3, 0, 0, 0, 0, 0, 0]
nada = [0, 0, 3, 0, 0, 0, 0, 0, 0]
start2 = [0, 0, 0, 0, 0, 0, 0, 3, 0]
goal = [0, 0, 0, 0, 0, 0, 3, 0, 0]
start = [0, 0, 0, 0, 0, 0, 0, 0, 0]

matriz_adyacencia = [rosario, instituto, la_raza, consulado, deportivo_18_de_marzo, nada, start2, goal, start]

from typing import List

Genome = List[]

def create_genome(rutas: List[Ruta]) -> Genome:
    genome = []
    for ruta in rutas:
        genome.append(ruta.puntoa)
        genome.append(ruta.puntob)
    return genome

Population = List[Genome]

def create_population(rutas: List[Ruta], population_size: int) -> Population:
    population = []
    for _ in range(population_size):
        population.append(create_genome(rutas))
    return population

def fitness(genome: Genome, matriz_adyacencia: List[List[int]]) -> int:
    fitness = 0
    for i in range(len(genome) - 1):
        fitness += matriz_adyacencia[genome[i]][genome[i + 1]]
    return fitness

Thing = namedtuple('Thing', ['name', 'value', 'weight'])

things = [
    Thing('A', 3, 2),
    Thing('B', 6, 3),
    Thing('C', 10, 5),
    Thing('D', 2, 1),
    Thing('E', 7, 4),
]

def selection_pair(population: Population, matriz_adyacencia: List[List[int]]) -> Population:
    return sorted(population, key=lambda genome: fitness(genome, matriz_adyacencia))[:2]
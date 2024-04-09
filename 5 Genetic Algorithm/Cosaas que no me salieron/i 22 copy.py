"""FC3 Genetic Alorithm from El Rosario to Consulado"""

from typing import List, Tuple
import numpy as np
import random
import operator
import pandas as pd
import matplotlib.pyplot as plt


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


class Fitness:
    def __init__(self, ruta):
        self.ruta = ruta

    def fitness(self) -> int:
        total_time = sum(ruta.time for ruta in self.ruta)
        return total_time  # return total time directly


start_point = "El Rosario"
end_point = "Consulado"


def createRoute(rutas: list, limitrutas) -> Tuple[str, int]:
    route = [ruta for ruta in rutas if ruta.puntoa == start_point]
    remaining_rutas = [ruta for ruta in rutas if ruta not in route]
    total_time = 0
    path = []
    while route[-1].puntob != end_point and len(route) < limitrutas:
        next_rutas = [
            ruta for ruta in remaining_rutas if ruta.puntoa == route[-1].puntob]
        if next_rutas:
            next_ruta = random.choice(next_rutas)
            route.append(next_ruta)
            total_time += next_ruta.time
            path.append((next_ruta.linea, next_ruta.puntoa, next_ruta.puntob))
            remaining_rutas.remove(next_ruta)
        else:
            break
    path_str = f"De {start_point} a {
        end_point} tarde {total_time}\nEl camino es\n "
    for paths in path:
        path_str += f"De {paths[1]} a {paths[2]} con la linea {paths[0]}\n "
    return path_str, total_time


def createrutas(start: str, end: str, rutas: List[Ruta], lim: int) -> Tuple[str, int]:
    """Calcula la distancia entre dos puntos de la ciudad y la ruta a seguir para llegar de uno a otro"""
    total_time = 0
    lim = 0
    current_station = start
    path = []
    while current_station != end and lim < limitrutas:
        lim += 1
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


limitrutas = 10


def initialPopulation(popSize, rutas):
    population = []

    for i in range(0, popSize):
        population.append(createRoute(rutas, limitrutas))
    return population


popSize = 100


def rankRoutes(population):
    fitnessResults = {}
    for i in range(0, len(population)):
        fitnessResults[i] = Fitness(population[i]).fitness()
    return sorted(fitnessResults.items(), key=operator.itemgetter(1), reverse=True)


def selection(popRanked, eliteSize):
    selectionResults = []
    for i in range(0, eliteSize):
        selectionResults.append(popRanked[i][0])
    while len(selectionResults) < len(popRanked):  # use tournament selection
        competitors = random.sample(popRanked, eliteSize)
        selectionResults.append(
            sorted(competitors, key=lambda x: x[1], reverse=True)[0][0])
    return selectionResults


def matingPool(population, selectionResults):
    matingpool = []
    for i in range(0, len(selectionResults)):
        index = selectionResults[i]
        matingpool.append(population[index])
    return matingpool


def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * (len(parent1) - 2)) + 1
    geneB = int(random.random() * (len(parent1) - 2)) + 1

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1 and item.puntoa !=
               start_point and item.puntob != end_point]

    child = [parent1[0]] + childP1 + childP2 + \
        [ruta for ruta in parent1 if ruta.puntob == end_point]
    return child


def breedPopulation(matingpool, eliteSize):
    children = []
    length = len(matingpool) - eliteSize
    pool = random.sample(matingpool, len(matingpool))

    for i in range(0, eliteSize):
        children.append(matingpool[i])

    while len(children) < len(matingpool):  # ensure new population has same size as old one
        child = breed(random.choice(pool), random.choice(pool))
        children.append(child)
    return children


def mutate(individual, mutationRate):
    for swapped in range(1, len(individual) - 1):
        if (random.random() < mutationRate):
            swapWith = int(random.random() * (len(individual) - 2)) + 1

            while swapWith == swapped:
                swapWith = int(random.random() * (len(individual) - 2)) + 1

            city1 = individual[swapped]
            city2 = individual[swapWith]

            individual[swapped] = city2
            individual[swapWith] = city1
    return individual


def mutatePopulation(population, mutationRate):
    mutatedPop = []

    for ind in range(0, len(population)):
        mutatedInd = mutate(population[ind], mutationRate)
        mutatedPop.append(mutatedInd)
    return mutatedPop


def nextGeneration(currentGen, eliteSize, mutationRate):
    popRanked = rankRoutes(currentGen)
    bestRouteIndex = popRanked[0][0]
    bestRoute = currentGen[bestRouteIndex]

    # Check if the best route ends at "Consulado"
    if bestRoute[-1].puntob == end_point:
        print("Arrived at Consulado. Stopping...")
        return currentGen

    selectionResults = selection(popRanked, eliteSize)
    matingpool = matingPool(currentGen, selectionResults)
    children = breedPopulation(matingpool, eliteSize)
    nextGeneration = mutatePopulation(children, mutationRate)
    # include some parents in next generation
    nextGeneration[:eliteSize] = currentGen[:eliteSize]
    return nextGeneration


def geneticAlgorithm(population, popSize, eliteSize, mutationRate, generations):
    pop = initialPopulation(popSize, population)
    print("Initial time: " + str(1 / rankRoutes(pop)[0][1]))
    print("Initial route: " + str([str(ruta)
                                   for ruta in pop[rankRoutes(pop)[0][0]]]))

    for i in range(0, generations):
        pop = nextGeneration(pop, eliteSize, mutationRate)
        bestRouteIndex = rankRoutes(pop)[0][0]
        bestRoute = pop[bestRouteIndex]
        print(f"Generation {i+1} Best Route: " + " -> ".join([f'from "{ruta.puntoa}" to "{
            ruta.puntob}" with line "{ruta.linea}" and a time of {ruta.time}' for ruta in bestRoute]))

        # Stop if the end point is reached
        if bestRoute[-1].puntob == end_point:
            print("Arrived at Consulado. Stopping...")
            break

    print("Final time: " + str(1 / rankRoutes(pop)[0][1]))
    bestRouteIndex = rankRoutes(pop)[0][0]
    bestRoute = pop[bestRouteIndex]
    print("Final route: " + str([str(ruta) for ruta in bestRoute]))
    return bestRoute, pop  # return final population and best route


geneticAlgorithm(population=rutas, popSize=10, eliteSize=1,
                 mutationRate=0.01, generations=10)

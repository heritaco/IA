import random

# Define the table of distances
distances = [
    [0, 2, 9, 10],
    [1, 0, 6, 4],
    [15, 7, 0, 8],
    [6, 3, 12, 0]
]

# Define the population size and number of generations
population_size = 10
num_generations = 100

# Define the length of the chromosome (number of cities)
chromosome_length = len(distances)

# Generate an initial population
population = []
for _ in range(population_size):
    chromosome = list(range(chromosome_length))
    random.shuffle(chromosome)
    population.append(chromosome)

# Define the fitness function


def calculate_fitness(chromosome):
    total_distance = 0
    for i in range(chromosome_length - 1):
        city1 = chromosome[i]
        city2 = chromosome[i + 1]
        total_distance += distances[city1][city2]
    return total_distance


# Main loop for the Genetic Algorithm
for generation in range(num_generations):
    # Calculate the fitness for each chromosome in the population
    fitness_scores = [calculate_fitness(chromosome)
                      for chromosome in population]

    # Select the best chromosomes for reproduction
    selected_chromosomes = sorted(
        zip(population, fitness_scores), key=lambda x: x[1])[:population_size]

    # Create a new population through crossover and mutation
    new_population = []
    for _ in range(population_size):
        parent1, _ = random.choice(selected_chromosomes)
        parent2, _ = random.choice(selected_chromosomes)
        child = parent1[:]
        for i in range(chromosome_length):
            if random.random() < 0.5:
                index = child.index(parent2[i])
                child[i], child[index] = child[index], child[i]
        new_population.append(child)

    # Replace the old population with the new population
    population = new_population

# Find the best solution
best_chromosome, best_fitness = min(
    zip(population, fitness_scores), key=lambda x: x[1])

# Print the best solution
print("Best solution:", best_chromosome)
print("Best fitness:", best_fitness)

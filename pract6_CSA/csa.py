import numpy as np
import random
import matplotlib.pyplot as plt

# -------------------------------
# Reproducibility
random.seed(42)
np.random.seed(42)

# -------------------------------
# Problem: Minimize Sphere Function
# f(x) = x1^2 + x2^2 + ... + xn^2

def objective_function(x):
    return np.sum(x ** 2)

# -------------------------------
# Parameters

POP_SIZE = 20
DIM = 5
GENERATIONS = 50

CLONE_FACTOR = 5
MUTATION_RATE = 0.7

LOWER_BOUND = -5
UPPER_BOUND = 5

# -------------------------------
# Initialize Population

def initialize_population():
    return [
        np.random.uniform(LOWER_BOUND, UPPER_BOUND, DIM)
        for _ in range(POP_SIZE)
    ]

# -------------------------------
# Affinity Calculation
# Lower fitness = better antibody

def calculate_affinity(population):
    return [
        (antibody, objective_function(antibody))
        for antibody in population
    ]

# -------------------------------
# Selection
# Select best half antibodies

def select_best(pop_affinity):

    pop_affinity.sort(key=lambda x: x[1])

    return pop_affinity[:POP_SIZE // 2]

# -------------------------------
# Cloning

def clone(selected):

    clones = []

    for antibody, affinity in selected:

        for _ in range(CLONE_FACTOR):

            clones.append(np.copy(antibody))

    return clones

# -------------------------------
# Mutation

def mutate(clones):

    mutated = []

    for clone in clones:

        if random.random() < MUTATION_RATE:

            noise = np.random.normal(0, 0.5, DIM)

            clone = clone + noise

            clone = np.clip(
                clone,
                LOWER_BOUND,
                UPPER_BOUND
            )

        mutated.append(clone)

    return mutated

# -------------------------------
# Main CSA Algorithm

population = initialize_population()

fitness_history = []

for gen in range(GENERATIONS):

    # Calculate affinity
    pop_affinity = calculate_affinity(population)

    # Selection
    selected = select_best(pop_affinity)

    # Cloning
    clones = clone(selected)

    # Mutation
    mutated_clones = mutate(clones)

    # Elitism
    elite = [antibody for antibody, _ in selected]

    # Combine elites + mutated clones
    new_population = elite + mutated_clones

    # Select best population globally
    population = sorted(
        new_population,
        key=objective_function
    )[:POP_SIZE]

    # Best solution
    best = min(population, key=objective_function)

    best_fitness = objective_function(best)

    fitness_history.append(best_fitness)

    print(
        f"Generation {gen} Best Fitness: "
        f"{best_fitness:.6f}"
    )

# -------------------------------
# Final Best Solution

best_solution = min(population, key=objective_function)

print("\nBest Solution Found:")
print(best_solution)

print("\nBest Fitness:")
print(objective_function(best_solution))

# -------------------------------
# Plot Graph

plt.plot(
    range(GENERATIONS),
    fitness_history,
    marker='o'
)

plt.xlabel("Generation")

plt.ylabel("Best Fitness")

plt.title("Clonal Selection Algorithm Optimization")

plt.grid(True)

plt.show()
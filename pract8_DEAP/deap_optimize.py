import random
from deap import base, creator, tools, algorithms

# Fitness function (minimize)
def eval_func(individual):
    return sum(x**2 for x in individual),

# DEAP Setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", random.uniform, -5.0, 5.0)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=3)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", eval_func)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Create population
population = toolbox.population(n=50)

# Evaluate initial population
fitnesses = list(map(toolbox.evaluate, population))
for ind, fit in zip(population, fitnesses):
    ind.fitness.values = fit

# GA loop
print("=" * 40)
print("Distributed Evolutionary Algorithm")
print("=" * 40)

for gen in range(20):
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)
    fitnesses = list(map(toolbox.evaluate, offspring))
    for ind, fit in zip(offspring, fitnesses):
        ind.fitness.values = fit
    population = toolbox.select(offspring, k=len(population))
    best = tools.selBest(population, k=1)[0]
    print(f"Generation {gen+1:2d} | Best Fitness: {best.fitness.values[0]:.4f}")

# Final result
best_ind = tools.selBest(population, k=1)[0]
print("\n" + "=" * 40)
print(f"Best Individual: {[round(x, 4) for x in best_ind]}")
print(f"Best Fitness   : {best_ind.fitness.values[0]:.4f}")
print("=" * 40)
print("\nConclusion: Successfully implemented DEAP Distributed Evolutionary Algorithm.")
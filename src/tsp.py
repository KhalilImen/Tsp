import numpy as np
from deap import base, creator, tools, algorithms

def eval_tsp(individual, distances):
    total_distance = 0
    for i in range(len(individual) - 1):
        city_a, city_b = individual[i], individual[i + 1]
        total_distance += distances[city_a][city_b]
    total_distance += distances[individual[-1]][individual[0]]
    return total_distance,

def genetic_algorithm(distances, n_cities, n_population=300, n_generations=400):
    creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
    creator.create("Individual", list, fitness=creator.FitnessMin)
    
    toolbox = base.Toolbox()
    toolbox.register("indices", np.random.permutation, n_cities)
    toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.indices)
    toolbox.register("population", tools.initRepeat, list, toolbox.individual)
    
    toolbox.register("mate", tools.cxOrdered)
    toolbox.register("mutate", tools.mutShuffleIndexes, indpb=0.05)
    toolbox.register("select", tools.selTournament, tournsize=3)
    toolbox.register("evaluate", eval_tsp, distances=distances)

    population = toolbox.population(n=n_population)
    algorithms.eaSimple(population, toolbox, cxpb=0.7, mutpb=0.2, ngen=n_generations, verbose=True)

    best_individual = tools.selBest(population, 1)[0]
    return best_individual, eval_tsp(best_individual, distances)

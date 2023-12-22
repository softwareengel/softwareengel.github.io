import numpy as np

# Define the problem
weights_of_items = np.array([2.3, 8.1, 6., 4.2, 1.3, 2.9, 7., 7.9, 3.6, 5., 3.1, 5., 3.4, 5.3, 0.8, 6.9, 9.8, 4.4, 5.4, 7.5, 4.6, 0.3, 9.2, 8.8, 2.2, 3.3, 9.9, 7.6, 5.9, 4.2, 4.9, 5.8, 4.4, 2.9, 0.1, 2.4, 5.6, 7.8, 7., 7.5, 7.3, 7.4, 6.4, 1.6, 6.8, 4., 4.6, 4.1, 0.5, 6.3, 5.2, 1.5, 9.7, 1.6, 2.6, 1.3, 6.5, 2.6, 7.8, 6.3, 8.4, 9.4, 1.4, 7.5])
costs_of_items = [6., 17., 10., 26., 19., 81., 67., 36., 21., 33., 13., 5., 172., 138., 185., 27., 4., 3., 11., 19., 95., 90., 24., 20., 28., 19., 7., 28., 14., 43., 40., 12., 25., 37., 25., 16., 85., 20., 15., 59., 72., 168., 30., 57., 49., 66., 75., 23., 79., 20., 104., 9., 32., 46., 47., 55., 21., 18., 23., 44., 61., 8., 42., 1.]
knapsack_weight_limit = 100
import numpy as np
import random

# Initialize the population
def initialize_population(population_size, chromosome_size, weights, weight_limit, probability_of_ones_in_a_new_chromosome):
   pop = []
   for _ in range(population_size):
       chromosome = []
       for _ in range(chromosome_size):
           if random.random() < probability_of_ones_in_a_new_chromosome:
               chromosome.append(1)
           else:
               chromosome.append(0)
       pop.append(chromosome)
   return np.array(pop)

# Evaluate the fitness of the population
def evaluate_fitness(pop, weights, costs, weight_limit):
   fitness_values = []
   weights_values = []
   for i in range(len(pop)):
       weight = 0
       cost = 0
       for j in range(len(pop[i])):
           if pop[i][j] == 1:
               weight += weights[j]
               cost += costs[j]
       if weight > weight_limit:
           fitness_values.append(0)
       else:
           fitness_values.append(cost)
       weights_values.append(weight)
   return np.array(fitness_values), np.array(weights_values)

# Roulette selection
def roulette_selection(pop, fit, num_parents):
   fit_sum = sum(fit)
   prob = [f/fit_sum for f in fit]
   parents = np.random.choice(pop, size=num_parents, p=prob)
   return parents

# Crossover
def cross_comp(pr, pop):
   cross = []
   for i in range(len(pr)//2):
       c1 = pr[i]
       c2 = pr[i+len(pr)//2]
       p = random.randint(0, len(c1)-1)
       child1 = np.hstack((c1[:p], c2[p:]))
       child2 = np.hstack((c2[:p], c1[p:]))
       cross.append(child1)
       cross.append(child2)
   return np.array(cross)

# Mutation
def mu_list(cross, pop):
   mut_list = []
   for i in range(len(cross)):
       if random.random() < 0.01:
           p = random.randint(0, len(cross[i])-1)
           if cross[i][p] == 0:
               cross[i][p] = 1
           else:
               cross[i][p] = 0
       mut_list.append(cross[i])
   return np.array(mut_list)

# Define the fitness function
def fitness(w, c, L, g):
  score = 0
  score1 = 0
  for i in range(len(w)):
      score = score + np.sum(w[i]*g[i])
  if score > L:
      f = 0
  else:
      for i in range(len(w)):
          score1 = score1 + np.sum(c[i]*g[i])
      f = score1
  return score1, score

# Initialize the population
pop = initialize_population(population_size=100, chromosome_size=64, weights=weights_of_items, weight_limit=50, probability_of_ones_in_a_new_chromosome=0.1)

# Evaluate the fitness of the population
fit, wgh = evaluate_fitness(pop, weights_of_items, costs_of_items, 100)

# Selection
pr = roulette_selection(pop, fit, 74)

# Crossover
cross = cross_comp(pr, pop)

# Mutation
mut_list = mu_list(cross, pop)

# Replacement
new_pr = roulette_selection(pop, fit, 26)
new_popi = np.vstack((mut_list, new_pr))
pop = new_popi

# Termination
while True:
   # Evaluate the fitness of the population
   fit, wgh = evaluate_fitness(pop, weights_of_items, costs_of_items, 100)

   # Selection
   pr = roulette_selection(pop, fit, 74)

   # Crossover
   cross = cross_comp(pr, pop)

   # Mutation
   mut_list = mu_list(cross, pop)

   # Replacement
   new_pr = roulette_selection(pop, fit, 26)
   new_popi = np.vstack((mut_list, new_pr))
   pop = new_popi

   # Termination condition
   if fit[0] >= knapsack_weight_limit:
       break

import random
import math
from copy import deepcopy
from chromosome import Chromosome

class GeneticsSolver:
    def __init__(self, puzzle, population_size=1000, mutation_probability=0.9, crossover_rate=0.3):
        self.puzzle = puzzle

        self.population_size = population_size
        self.mutation_probability = mutation_probability
        self.crossover_rate = crossover_rate

        self.population = []
        self.best_solution = None
        self.total_error = None

    def _initialize_population(self):
        self.population = [Chromosome(puzzle=self.puzzle) for _ in range(self.population_size)]

    def _evaluate_population(self):
        if not self.population:
            return

        if self.best_solution is None:
            self.best_solution = self.population[0]

        total_error = 0
        for individual in self.population:
            individual.update_error()
            if individual.error < self.best_solution.error:
                self.best_solution = deepcopy(individual)
            total_error += individual.error

        self.total_error = total_error / len(self.population)

    def _select_fittest(self):
        fitness_scores = []
        total_fitness = 0

        for individual in self.population:
            fitness = 1 / (0.000001 + individual.error)
            total_fitness += fitness
            fitness_scores.append(total_fitness)

        def _roulette_selection():
            random_point = random.random() * total_fitness
            for index, cumulative_fitness in enumerate(fitness_scores):
                if random_point < cumulative_fitness:
                    return index

        selected_population = []
        while len(selected_population) < self.population_size:
            index = _roulette_selection()
            selected_population.append(self.population[index])
        
        self.population = selected_population

    def _perform_crossover(self):
        if len(self.population) < 2:
            return

        crossover_count = math.ceil(len(self.population) * self.crossover_rate)
        available_indices = list(range(len(self.population)))

        for _ in range(crossover_count):
            parent_a, parent_b = random.sample(available_indices, 2)

            available_indices.remove(parent_a)
            available_indices.remove(parent_b)

            offspring_a, offspring_b = Chromosome.CrossOver(self.population[parent_a], self.population[parent_b])

            if offspring_a.error < min(self.population[parent_a].error, self.population[parent_b].error):
                self.population[parent_a] = offspring_a
            if offspring_b.error < min(self.population[parent_a].error, self.population[parent_b].error):
                self.population[parent_b] = offspring_b

    def _perform_mutation(self):
        for individual in self.population:
            if random.random() < self.mutation_probability:
                individual.Mutate()

    def solve(self, max_iter=1000, optimal_error=0):
        random.seed()
        self._initialize_population()

        for iteration in range(max_iter):
            if self.best_solution and self.best_solution.error_puzzle_cost <= optimal_error:
                break

            self._perform_crossover()
            self._evaluate_population()
            self._select_fittest()
            self._perform_mutation()

            self._display_progress(iteration)

        return self.best_solution

    def _display_progress(self, iteration):
        print(f"Iteration: {iteration} ")
        print(f"Population Size: {len(self.population)}   Total Error: {self.total_error:.4f}")

        if self.best_solution:
            print(f"Best Solution: {self.best_solution.error:.4f}   -> Puzzle Cost: {self.best_solution.error_puzzle_cost:.4f} + Gene Length: {self.best_solution.error_gene_len:.4f}")
            # print(f"Best Solution: {self.best_solution}")
        
        print("\n")

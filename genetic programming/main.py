from GamePad import Pad
from GeneticSolver import GeneticsSolver

MUTATION_CHANCE = 0.9
CROSSOVER_RATE = 0.3
POPULATION_SIZE = 1000
MAX_ITERATIONS = 1000

def main():
    puzzle = Pad()
    puzzle.shuffle()

    solver = GeneticsSolver(puzzle, POPULATION_SIZE, 
                            MUTATION_CHANCE, 
                            CROSSOVER_RATE)
    
    best_solution = solver.solve(max_iter=MAX_ITERATIONS)

    print('Initial Puzzle Board:')
    print(puzzle)

    print('Solution:')
    print(best_solution.gene)
    print("\n")

    puzzle.apply_chain(best_solution.gene, with_display=True)

    print('Result:')
    print(puzzle)

if __name__ == "__main__":
    main()

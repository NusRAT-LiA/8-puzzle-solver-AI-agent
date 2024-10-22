import random
from copy import deepcopy

class Chromosome:
    VALID_MOVES = ['up', 'down', 'left', 'right']

    def __init__(self, puzzle, gene=None):
        if gene is None:
            gene = []

        self.error = None
        self.error_puzzle_cost = None
        self.error_gene_len = None
        self.puzzle = puzzle
        self.gene = gene
        self.update_error()

    def update_error(self):
        temp = deepcopy(self.puzzle)
        temp.apply_chain(self.gene)

        self.error_puzzle_cost = temp.cost()
        self.error_gene_len = len(self.gene) * 0.01
        self.error = self.error_puzzle_cost + self.error_gene_len

    @staticmethod
    def CrossOver(a, b):
     if len(b.gene) > len(a.gene):
        return Chromosome.CrossOver(b, a)
 
     len_a, len_b = len(a.gene), len(b.gene)

     geneA = [a.gene[i] if random.random() < 0.5 else b.gene[i] for i in range(len_b)]
     geneB = [b.gene[i] if random.random() < 0.5 else a.gene[i] for i in range(len_b)]
 
     geneA.extend(a.gene[len_b:])

     return Chromosome(a.puzzle, geneA), Chromosome(b.puzzle, geneB)


    def Mutate(self, allow_only_growing=False):
     def add_gene():
        self.gene.append(random.choice(self.VALID_MOVES))

     def mutate_gene():
        i = random.randrange(len(self.gene))
        self.gene[i] = random.choice(self.VALID_MOVES)

     if not self.gene:
        add_gene()  
     elif random.random() < 0.5:
        add_gene()  
     else:
        mutate_gene()  

    def __str__(self):
        return '(%d)  %s' % (len(self.gene), ' -> '.join(self.gene))
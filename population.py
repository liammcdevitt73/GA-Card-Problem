import random

class Population:
    """
    This class represents a population in a genetic algorithm.
    
    The main functions are initialization and evaluation.
    
    Authors: Liam McDevitt & Andrew Pozzuloi
    Date:    2023 - 03 - 02
    """
    
    def __init__(pop_size=50):
        """
        Initializes the population class.

        Args:
            pop_size (int): Population size, i.e., the number of chromosomes. Defaults to 50.
        """
        # Initialize global variables
        self.pop_size = pop_size

    def init_pop(self):
        """
        Initializes each chromosome in the population randomly from the gene pool.
        """
        self.individuals = [random.shuffle(problem.gene_pool) for i in range(self.pop_size)]
        
    def eval_pop(self):
        """
        Evaluates the fitness of each individual in the population.
        """
        for individual in self.individuals:
            individual.fitness = problem.eval(individual.chromosome)
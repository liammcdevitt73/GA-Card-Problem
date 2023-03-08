import random
import individual
import problem
from statistics import mean, median, stdev

class Population:
    """
    This class represents a population in a genetic algorithm.
    
    The main functions are initialization and evaluation.
    
    Authors: Liam McDevitt & Andrew Pozzuoli
    Date:    2023 - 03 - 02
    """
    
    def __init__(self, problem, pop_size=50):
        """
        Initializes the population class.

        Args:
            pop_size (int): Population size, i.e., the number of chromosomes. Defaults to 50.
        """
        # Initialize global variables
        self.pop_size = pop_size
        self.problem = problem
        
        # Initialize population
        self.init_pop()
        self.eval_pop()

    def init_pop(self):
        """
        Initializes each chromosome in the population randomly from the gene pool.
        """
        self.individuals = [individual.Individual(random.sample(self.problem.gene_pool, len(self.problem.gene_pool))) for i in range(self.pop_size)]

        
        
    def eval_pop(self):
        """
        Evaluates the fitness of each individual in the population.
        """
        for individual in self.individuals:
            individual.fitness = self.problem.eval(individual.chromosome)

    def get_best(self):
        """
        returns the best individual in the population
        """
        if self.problem.min:
            return min(self.individuals, key=lambda x : x.fitness)
        else:
            return max(self.individuals, key=lambda x : x.fitness)
        
    def get_avg_fitness(self):
        """
        returns the population average fitness
        """
        sum = 0
        
        for i in range(len(self.individuals)):
            sum += self.problem.eval(self.individuals[i].chromosome)
        
        return sum / len(self.individuals)
    
    def get_fitnesses(self):
        fitnesses = []
        for ind in self.individuals:
            fitnesses.append(ind.fitness)
        return fitnesses

    def get_stats(self):
        fits = self.get_fitnesses()
        return f'{mean(fits)},{median(fits)},{stdev(fits)},{min(fits)},{max(fits)}'

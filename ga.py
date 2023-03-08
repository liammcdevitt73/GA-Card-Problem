import random
import population as pop
import individual as ind
class GA:
    """
    The main genetic algorithm library class meant to be generalizable to numerous
    discrete optimization problems.
    
    Authors: Liam McDevitt & Andrew Pozzuoli
    Date:    2023 - 03 - 02
    """
   
    def __init__(self, problem, num_generations=100, population_size=100, crossover_rate=0.4, mutation_rate=0.6, 
                 selection_type='tournament', crossover_type='UOX', mutation_type='swap', num_elites=1):
        """
        Initializes and runs the GA when the object is created.

        Args:
            num_generations (int):   Number of alloted generations. Defaults to 100.
            population_size (int):   Population size.               Defaults to 100.
            crossover_rate  (float): Crossover rate.                Defaults to 0.4.
            mutation_rate   (float): Mutation rate.                 Defaults to 0.6.
            selection_type  (str):   Type of selection.             Defaults to 'tournament'.
            crossover_type  (str):   Type of crossover.             Defaults to 'UOX'.
            mutation_type   (str):   Type of mutation.              Defaults to 'swap'.
            num_elites      (int):   Number of elites.              Defaults to 1.
        """
        
        # Initializing global variables
        self.num_generations = num_generations
        self.population_size = population_size
        self.crossover_rate  = crossover_rate
        self.mutation_rate   = mutation_rate
        self.selection_type  = selection_type
        self.crossover_type  = crossover_type
        self.mutation_type   = mutation_type
        self.num_elites      = num_elites
        
        # Initialize population
        self.population = pop.Population(problem, population_size)
        
        # Run GA
        self.run()
        
    def run(self):
        """
        Iterates the GA until it reaches the maximum number of alloted iterations.
        """
        for i in range(self.num_generations):
            self.iterate()
            print(f'ITERATION [{i+1}]: Best -> {self.population.get_best()}')
        
    def iterate(self):
        """
        Performs one iteration of the genetic algorithm.
        """
        
        # Elitism -> Keep the best num_elites from the previous population
        sortedPop = sorted(self.population.individuals, key=lambda x : x.fitness)
        for i in range(self.num_elites):
            self.population.individuals[i] = sortedPop[i]
        
        # Selection -> Create a whole new population (generational)
        for i in range(self.num_elites, self.population_size):
            if self.selection_type == 'tournament':
                self.selection_tournament()
                self.population.individuals[i] = self.selection_tournament()
        
        # Crossover -> Combine parent chromosomes to produce new solutions
        for i in range(self.population_size - 1):
            if random.random() < self.crossover_rate:
                children = []
                if self.crossover_type == 'UOX':
                    children = self.crossover_UOX(self.population.individuals[i], self.population.individuals[i + 1])
                self.population.individuals[i]     = children[0]
                self.population.individuals[i + 1] = children[1]                   
                    
        
        # Mutation -> Alter an individual for exploration of the search space
        for i in range(self.population_size):
            if random.random() < self.mutation_rate:
                if self.mutation_type == 'reverse':
                    self.mutation_reverse(self.population.individuals[i])
                if self.mutation_type == 'swap':
                    self.mutation_swap(self.population.individuals[i])
        
        # Evaluate -> Determine the fitness of each individual in the new population
        self.population.eval_pop()
        
        
    def crossover_UOX(self, p1, p2):
        """
        Performs a uniform-order crossover.

        Args:
            p1 (Individual): Parent 1
            p2 (Individual): Parent 2

        Returns:
            [Individual]: [0] Child 1, [1] Child 2
        """
        # Randomly initialize mask
        mask = [random.choice([True, False]) for i in range(len(p1.chromosome))]
        
        # Initialize children
        c1 = [-1 for i in range(len(p1.chromosome))]
        c2 = [-1 for i in range(len(p2.chromosome))]
        
        # Fill in children depending on mask
        for i in range(len(mask)):
            if mask[i]:
                c1[i] = p1.chromosome[i]
                c2[i] = p2.chromosome[i]
        
        # Fill in missing children from opposite parent
        for i in range(len(c1)):
            if c1[i] == -1:
                for j in range(len(p2.chromosome)):
                    if not(p2.chromosome[j] in c1):
                        c1[i] = p2.chromosome[j]
                        break
            if c2[i] == -1:
                for j in range(len(p1.chromosome)):
                    if not(p1.chromosome[j] in c2):
                        c2[i] = p1.chromosome[j]
                        break
        
        # Return final children
        return [ind.Individual(c1), ind.Individual(c2)]
    
    def selection_tournament(self, k=3):
        """
        Selects the most fit individual of k random individuals from the population
        to be a parent in reproduction of the new population.

        Args:
            k (int): Tournament size. Defaults to 4.

        Returns:
            Individual: A possible parent for reproduction.
        """
        return min(random.sample(self.population.individuals, k), key=lambda x : x.fitness)
        
    def mutation_reverse(self, i):
        """
        Performs reverse mutation on an Individual i, i.e., reverse the chromosome vector.

        Args:
            i (Individual): Individual to mutate
        """
        i.chromosome.reverse()

    def mutation_swap(self, i):
        """
        Performs swap mutation on an Individual i, i.e., swap to genes in the chromosome vector.

        Args:
            i (Individual): Individual to mutate
        """
        idx = range(len(i.chromosome))
        i1, i2 = random.sample(idx, 2)
        i.chromosome[i1], i.chromosome[i2] = i.chromosome[i2], i.chromosome[i1]
        
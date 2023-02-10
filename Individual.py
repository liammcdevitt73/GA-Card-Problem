
from math import prod
import random

class Individual:
    """
    This class represents each individual candidate solution in the population

    Individuals are represented as an array of ten numbers in any order and one split variable
    The split variable indicates that everything left of the split index is in the sum pile
    and everything right of and including the split index is in the product pile

    eg. [2, 5, 1, 3, 7, 8, 10, 4, 6, 9]
        split = 3
        sum = [2, 5, 1]
        product = [3, 7, 8, 10, 4, 6, 9]

    """

    GOAL_SUM = 36       # goal sum value
    GOAL_PROD = 360     # goal product value
    NUM_CARDS = 10      # total number of cards

    def __init__(self, chromosome=[x for x in range(1,11)], split=0):
        """
        This funciton initializes a new candidate solution

        :param chromosome: A list of unique integers 1..10 in some order. Default [1,2,3,4,5,6,7,8,9,10]
        :param split:      The index splitting the list into sum and product
        """
        split = self.__clamp(split, 0, len(chromosome)-1)
        self.chromosome = chromosome
        self.split = split


    def fitness(self):
        """
        Returns the fitness of this candidate solution expressed as the 
        sum of errors of each pile

        :return: the sum of errors
        """
        sum = 0
        prod = 1

        for n in self.chromosome[0:self.split]:
            sum = sum + n

        for n in self.chromosome[self.split:len(self.chromosome)]:
            prod = prod * n

        return abs(sum - self.GOAL_SUM) + abs(prod - self.GOAL_PROD)

    def generate_new(self):
        """
        This method randomizes the current individual's chromosome
        Used to generate a new individual after initializing
        """
        random.shuffle(self.chromosome)
        self.split = random.randint(0,len(self.chromosome))

    def get_chromosome(self):
        """
        Returns a tuple (chromosome, split)

        :return: tuple (chromosome, split)
        """
        return self.chromosome, self.split

    def set_chromosome(self, chromosome=None, split=None):
        """
        Allows modification of chromosome and split values

        :param chromosome: the new chromosome
        :param split: the new index
        """
        if chromosome is not None:
            if (len(chromosome) != 10):
                raise Exception("ERROR: INVALID CHROMOSOME LENGTH")
            else:
                self.chromosome = chromosome
        
        if split is not None:
            if not type(split) is int:
                raise Exception("ERROR: SPLIT MUST BE OF TYPE INTEGER")
            else:
                split = self.__clamp(split, 0, len(chromosome)-1)
                self.split = split


    def __str__(self):
        fitness = self.fitness()
        sum_pile = [x for x in self.chromosome[0:self.split]]
        prod_pile = [x for x in self.chromosome[self.split:]]
        return f"FITNESS:{fitness}\tSUM PILE:{sum_pile}\tPROD PILE:{prod_pile}"


    def __clamp(self, val, _min, _max):
        """
        Helper function to clamp a value between range

        :param val: value to clamp between range
        :param _min: lower bound
        :param _max: upper bound
        :return: the value between the range
        """

        return max(_min, min(val, len(_max)-1))

    def repair(self):
        """
        If the chromosome is invalid, then this method repairs the chromosome to be valid
        """
        count = [0] * self.NUM_CARDS
        dupl = []

        # Check if the length of the chromosome is correct and adjust if not
        if len(self.chromosome) < self.NUM_CARDS:
            self.chromosome.extend([0]*abs(self.NUM_CARDS-len(self.chromosome)))
        elif len(self.chromosome) > self.NUM_CARDS:
            while len(self.chromosome) > self.NUM_CARDS:
                self.chromosome.pop()
        
        # Check for duplicates
        for gene in len(self.chromosome):
            count[gene] = count[gene]+1
            if count[gene] > 1:
                dupl.append(gene) # add duplicate value to dupl list
        
        # Loop over duplicate values
        for d in dupl:
            i = count.index(0)
            new_gene = count[i] # find number not in chromosome
            count[i] += 1
            self.chromosome[self.chromosome.index(d)] = new_gene




        






        


    

    


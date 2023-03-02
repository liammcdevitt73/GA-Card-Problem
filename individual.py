from math import prod
import random

class Individual:
    """
    This class represents individual candidate solutions 
    These solutions are represented as 1D vectors with unique,discrete values


    # Author: Andrew Pozzuoli
    # Date:    2023 - 02 - 22

    """

    def __init__(self, chromosome=[]):
        """
        This funciton initializes a new candidate solution

        :param chromosome: A list of unique integers in some order. Default []
        """
        self.chromosome = chromosome
        self.fitness = 0


    def get_fitness(self):
        """
        :return: fitness variable
        """
        return self.fitness


    def get_chromosome(self):
        """
        Returns the chromosome

        :return: chromosome
        """
        return self.chromosome

    def set_chromosome(self, chromosome=None):
        """
        Allows modification of chromosome

        :param chromosome: the new chromosome
        """
        if chromosome is not None:
            self.chromosome = chromosome


    def __str__(self):
        fitness = self.get_fitness()
        return f'FITNESS:{fitness}\tCHROMOSOME:{self.chromosome}'





        






        


    

    


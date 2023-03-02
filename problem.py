import ga
class Problem:
    """ 
    Authors: Liam McDevitt & Andrew Pozzuoli
    Date:    2023 - 03 - 02
    
    The problem class gives the chromosome representation, fitness evaluation, and whether
    the problem is a minimization or maximization.

    This example shows the card problem

    Individuals are represented as a vector of size 11 [0..10]. The '0' represents where the deck is split.
    Everything left of the '0' is in the sum pile and everything right of the '0' is in the product pile
    """

    GOAL_SUM = 36
    GOAL_PROD = 360
    gene_pool = []

    def __init__(self, gene_pool=[], min=True):
        """ Initialize chromosome gene_pool and whether the problem is minimization
        :param gene_pool: the genes available to make a vector
        :param min: boolean representing if the problem is one of minimization
        """
        self.gene_pool = gene_pool
        self.min = min
        self.ga = ga.GA() # Run the GA

    def eval(self, ind = []):
        """
        :param ind: the individual being evaluated
        :return: sum of errors 
        """
        sum = 0
        prod = 1
        split = False

        for i in ind:
            if ind[i] == 0:     # If we have reached the split, stop summing
                split = True
                continue
            elif not split:     # If we are left of split, sum the values
                sum = sum + ind[i]
            else:
                prod = prod * ind[i]
        
        return abs(sum - self.GOAL_SUM) + abs(prod - self.GOAL_PROD)

def main():
    Problem(list(range(0,11)), True)
    
if __name__ == '__main__':
    main()
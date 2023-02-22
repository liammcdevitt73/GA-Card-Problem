import unittest
import individual

class IndividualTest(unittest.TestCase):
    """
    Test suite for individual class

    Author: Andrew Pozzuoli
    """

    def setUp(self):
        self.indv = [1,2,3,4,5]
        self.individual = individual.Individual(self.indv)

    def test_init_individual(self):
        self.assertEqual(self.individual.get_chromosome(), self.indv, 'Individual not initialized correctly')
        self.assertEqual(self.individual.get_fitness(), 0, "Initial fitness not 0")
    
    def test_alter_chromosome(self):
        new_indv = [10,11,5]
        self.individual.set_chromosome(new_indv)
        self.assertEqual(self.individual.get_chromosome(), new_indv, 'Individual not updated')

def suite():
    suite = unittest.TestSuite()
    suite.addTest(IndividualTest('test_init_individual')) 
    suite.addTest(IndividualTest('test_alter_chromosome'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())

    

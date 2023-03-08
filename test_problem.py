import unittest
import problem

class ProblemTest(unittest.TestCase):
    """
    Test suite for problem class

    Author: Andrew Pozzuoli
    """

    def setUp(self):
        self.indv = [2, 7, 8, 9, 10, 0, 1, 3, 4, 5, 6]
        self.problem = problem.Problem(list(range(0,11)), True)

    def test_eval(self):
        self.assertEqual(self.problem.eval(self.indv), 0, "Fitness not 0")

    
def suite():
    suite = unittest.TestSuite()
    suite.addTest(ProblemTest('test_eval'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
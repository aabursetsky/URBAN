import unittest
import tests_12_3

ratST = unittest.TestSuite()
ratST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
ratST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(ratST)

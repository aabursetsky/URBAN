import runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        runner_walk = runner.Runner("Walk")
        for _ in range(10):
            runner_walk.walk()
        self.assertEqual(runner_walk.distance, 50)

    def test_run(self):
        runner_run = runner.Runner("Run")
        for _ in range(10):
            runner_run.run()
        self.assertEqual(runner_run.distance, 100)

    def test_challenge(self):
        first = runner.Runner("First")
        second = runner.Runner("Second")
        for _ in range(10):
            first.run()
            second.walk()
        self.assertNotEqual(first.distance, second.distance)


if __name__ == "__main__":
    unittest.main()


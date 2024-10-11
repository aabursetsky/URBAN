import runner_and_tournament as rat
import unittest

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        runner_walk = rat.Runner("Walk")
        for _ in range(10):
            runner_walk.walk()
        self.assertEqual(runner_walk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        runner_run = rat.Runner("Run")
        for _ in range(10):
            runner_run.run()
        self.assertEqual(runner_run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        first = rat.Runner("First")
        second = rat.Runner("Second")
        for _ in range(10):
            first.run()
            second.walk()
        self.assertNotEqual(first.distance, second.distance)

class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.first = rat.Runner("Усэйн", 10)
        self.second = rat.Runner("Андрей", 9)
        self.third = rat.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            print(show_result)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_1(self):
        self.tour_1 = rat.Tournament(90, self.first, self.third)
        self.all_results = self.tour_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[1] = self.all_results  # ключ 1

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_2(self):
        self.tour_2 = rat.Tournament(90, self.second, self.third)
        self.all_results = self.tour_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[2] = self.all_results  # ключ 2

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run_3(self):
        self.tour_3 = rat.Tournament(90, self.first, self.second, self.third)
        self.all_results = self.tour_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results  # ключ 3


if __name__ == "__main__":
    unittest.main()

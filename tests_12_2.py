import runner_and_tournament as rat
import unittest


class TournamentTest(unittest.TestCase):
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

    def test_run_1(self):
        self.tour_1 = rat.Tournament(90, self.first, self.third)
        self.all_results = self.tour_1.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[1] = self.all_results  # ключ 1

    def test_run_2(self):
        self.tour_2 = rat.Tournament(90, self.second, self.third)
        self.all_results = self.tour_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[2] = self.all_results  # ключ 2

    def test_run_3(self):
        self.tour_3 = rat.Tournament(90, self.first, self.second, self.third)
        self.all_results = self.tour_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Ник')
        TournamentTest.all_results[3] = self.all_results  # ключ 3


if __name__ == "__main__":
    unittest.main()

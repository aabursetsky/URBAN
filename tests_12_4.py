import logging
import unittest
import rt_with_exceptions as rat

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @classmethod
    def setUpClass(cls):
        logging.basicConfig(
            filename='runner_tests.log',
            filemode='w',
            level=logging.INFO,
            encoding='utf-8',
            format='%(asctime)s | %(levelname)s | %(message)s')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            runner_walk = rat.Runner(name="Walk", speed=-10)
            for _ in range(10):
                runner_walk.walk()
            self.assertEqual(runner_walk.distance, 50)
        except ValueError:
            logging.warning(msg='Неверная скорость для Runner', exc_info=True)
        logging.info('"test_walk" выполнен успешно')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            runner_run = rat.Runner(name="Run", speed=12)
            for _ in range(10):
                runner_run.run()
            self.assertEqual(runner_run.distance, 240)
        except TypeError:
            logging.warning(msg='Неверный тип данных для объекта Runner', exc_info=True)
        logging.info('"test_run" выполнен успешно')

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

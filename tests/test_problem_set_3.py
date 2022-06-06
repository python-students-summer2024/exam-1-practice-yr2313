"""
Do not run this file directly!  It won't work.
Run it using the Test panel in Visual Studio Code.
"""

from problem_set_3 import *
import problem_set_3

class Tests:

    def test_get_random_int(self, monkeypatch):
        """
        Check whether the get_random_int function produces values in the correct range
        """
        # check that random numbers are in the correct range
        num_times = 50
        for i in range(num_times):
          low = random.randint(1, 10)
          high = random.randint(11, 20)
          actual = get_random_int(low, high)
          assert low <= actual <= high


        # check that the randint function is being used correctly
        counter = {'randint': 0, 'low': None, 'high': None}
        def mock_randint(x, y):
            counter['randint'] += 1
            counter['low'] = x
            counter['high'] = y
        low = random.randint(1, 10)
        high = random.randint(11, 20)
        monkeypatch.setattr("random.randint", lambda x, y: mock_randint(x, y))
        get_random_int(low, high)
        # compare low and high boundaries to expected
        assert counter['low'] == low
        assert counter['high'] == high

    def test_get_guess(self, monkeypatch):
      """
      Check that the guess is being solicited and its result returned correctly.
      """
      cases = [
        {"max": 5, "rand": 3, "guess": "3", "expected": True}, # correct
        {"max": 5, "rand": 5, "guess": "5", "expected": True}, # correct
        {"max": 5, "rand": 3, "guess": "5", "expected": False}, # incorrect
        {"max": 5, "rand": 3, "guess": "0", "expected": -1}, # invalid
        {"max": 5, "rand": 3, "guess": "10", "expected": -1}, # invalid
        {"max": 5, "rand": 3, "guess": "foo", "expected": -1}, # invalid

        {"max": 10, "rand": 5, "guess": "5", "expected": True}, # correct
        {"max": 10, "rand": 10, "guess": "10", "expected": True}, # correct
        {"max": 10, "rand": 5, "guess": "7", "expected": False}, # incorrect
        {"max": 10, "rand": 5, "guess": "0", "expected": -1}, # invalid
        {"max": 10, "rand": 5, "guess": "20", "expected": -1}, # invalid
        {"max": 10, "rand": 5, "guess": "bar", "expected": -1}, # invalid

        {"max": 20, "rand": 10, "guess": "10", "expected": True}, # correct
        {"max": 20, "rand": 20, "guess": "20", "expected": True}, # correct
        {"max": 20, "rand": 10, "guess": "15", "expected": False}, # incorrect
        {"max": 20, "rand": 10, "guess": "0", "expected": -1}, # invalid
        {"max": 20, "rand": 10, "guess": "25", "expected": -1}, # invalid
        {"max": 20, "rand": 10, "guess": "baz", "expected": -1}, # invalid
      ]

      for case in cases:
        counter = { 'input': 0, 'rand': 0 }
        def mock_input(x):
            counter['input'] += 1
            return case['guess']
        def mock_rand(x, y):
            counter['rand'] += 1
            return case['rand']
        monkeypatch.setattr("builtins.input", lambda x: mock_input(x))
        monkeypatch.setattr("problem_set_3.get_random_int", lambda x,y: mock_rand(x,y))
        result = get_guess(case['max'])
        assert result == case['expected']

    def test_play_game(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        cases = [
          {"get_guess": [True, True, True, True], "expected": "Correct!\nCorrect!\nCorrect!\nCorrect!\nYou guessed 100% of the random numbers correctly."},
          {"get_guess": [True, False, True, False], "expected": "Correct!\nWrong!\nCorrect!\nWrong!\nYou guessed 50% of the random numbers correctly."},
          {"get_guess": [False, True, False, True], "expected": "Wrong!\nCorrect!\nWrong!\nCorrect!\nYou guessed 50% of the random numbers correctly."},
          {"get_guess": [False, True, True, True], "expected": "Wrong!\nCorrect!\nCorrect!\nCorrect!\nYou guessed 75% of the random numbers correctly."},
          {"get_guess": [False, True, False, False], "expected": "Wrong!\nCorrect!\nWrong!\nWrong!\nYou guessed 25% of the random numbers correctly."},
          {"get_guess": [False, False, False, False], "expected": "Wrong!\nWrong!\nWrong!\nWrong!\nYou guessed 0% of the random numbers correctly."},
          {"get_guess": [-1], "expected": "Invalid response!"},
          {"get_guess": [True, -1], "expected": "Correct!\nInvalid response!"},
          {"get_guess": [False, -1], "expected": "Wrong!\nInvalid response!"},
          {"get_guess": [True, False, -1], "expected": "Correct!\nWrong!\nInvalid response!"},
          {"get_guess": [False, True, -1], "expected": "Wrong!\nCorrect!\nInvalid response!"},
          {"get_guess": [True, False, True, -1], "expected": "Correct!\nWrong!\nCorrect!\nInvalid response!"},
          {"get_guess": [False, True, False, -1], "expected": "Wrong!\nCorrect!\nWrong!\nInvalid response!"},
        ]

        for case in cases:
          expected_count = len(case['get_guess'])
          counter = { 'get_guess': 0 }
          def mock_get_guess(x):
              counter['get_guess'] += 1
              return case['get_guess'].pop(0)
          monkeypatch.setattr("problem_set_3.get_guess", lambda x: mock_get_guess(x))
          play_game()
          actual = capsys.readouterr().out
          actual = actual.strip()
          assert actual == case['expected']
          assert counter['get_guess'] == expected_count

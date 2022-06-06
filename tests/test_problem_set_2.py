"""
Do not run this file directly!  It won't work.
Run it using the Test panel in Visual Studio Code.
"""

from problem_set_2 import *

class Tests:

    @classmethod
    def run_tests(self, method, cases, capsys, monkeypatch, count_inputs=False):
        for case in cases:
            expected_input_count = len(case['inputs'])
            counter = { 'input': 0 }
            def mock_input(x):
                counter['input'] += 1
                return case['inputs'].pop(0)
            monkeypatch.setattr("builtins.input", lambda x: mock_input(x))
            expected = case["expected"].strip()
            weather_helper()
            actual = capsys.readouterr().out
            actual = actual.strip()
            assert actual == expected
            if count_inputs:
                assert counter['input'] == expected_input_count

    def test_temp_validation(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        import random
        cases = [
          { "inputs": ["-71"], "expected": "Invalid temperature!" },
          { "inputs": ["135"], "expected": "Invalid temperature!" },
          { "inputs": [random.randint(135, 400)], "expected": "Invalid temperature!" },
          { "inputs": [random.randint(135, 400)], "expected": "Invalid temperature!" },
          { "inputs": [random.randint(-400, -69)], "expected": "Invalid temperature!" },
          { "inputs": [random.randint(-400, -69)], "expected": "Invalid temperature!" },
        ]
        self.run_tests(weather_helper, cases, capsys, monkeypatch, count_inputs=True)

    def test_over_90(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        import random
        cases = [
                        # temp                      #aircon
          { "inputs": [str(random.randint(91, 134)), "yes"], "expected": "Stay cool indoors." },
          { "inputs": [str(random.randint(91, 134)), "yes"], "expected": "Stay cool indoors." },
          { "inputs": [str(random.randint(91, 134)), "no"], "expected": "I hope you have a fan." },
          { "inputs": [str(random.randint(91, 134)), "no"], "expected": "I hope you have a fan." },
        ]
        self.run_tests(weather_helper, cases, capsys, monkeypatch, count_inputs=True)

    def test_under_40(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        import random
        cases = [
                        # temp                      #snow   #jacket
          { "inputs": [str(random.randint(-70, 39)), "yes", "yes"], "expected": "Glad to hear you're dressed appropriately!" },
          { "inputs": [str(random.randint(-70, 39)), "yes", "yes"], "expected": "Glad to hear you're dressed appropriately!" },
          { "inputs": [str(random.randint(-70, 39)), "yes", "no"], "expected": "What were you thinking when you left home today?!" },
          { "inputs": [str(random.randint(-70, 39)), "yes", "no"], "expected": "What were you thinking when you left home today?!" },
        ]
        self.run_tests(weather_helper, cases, capsys, monkeypatch, count_inputs=True)

    def test_cold_rain(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        import random
        cases = [
                            # temp                      #snow  #rain #umbrella
            { "inputs": [str(random.randint(-70, 39)), "no", "yes", "yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "no", "yes", "yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "no", "yes", "no"], "expected": "You must enjoy getting wet!" },
            { "inputs": [str(random.randint(-70, 39)), "no", "yes", "no"], "expected": "You must enjoy getting wet!" },
        ]
        self.run_tests(weather_helper, cases, capsys, monkeypatch, count_inputs=True)

    def test_affirmatives(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        import random
        cases = [
            { "inputs": [str(random.randint(-70, 39)), "no", "yes", "yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "no", "yeah", "yeah"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "no", "yup", "yup"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "yes", "yes"], "expected": "Glad to hear you're dressed appropriately!" },
            { "inputs": [str(random.randint(-70, 39)), "yeah", "yeah"], "expected": "Glad to hear you're dressed appropriately!" },
            { "inputs": [str(random.randint(-70, 39)), "yup", "yup"], "expected": "Glad to hear you're dressed appropriately!" },
        ]
        self.run_tests(weather_helper, cases, capsys, monkeypatch)

    def test_negatives(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        import random
        cases = [
          { "inputs": [str(random.randint(91, 134)), "no"], "expected": "I hope you have a fan." },
          { "inputs": [str(random.randint(91, 134)), "nah"], "expected": "I hope you have a fan." },
          { "inputs": [str(random.randint(91, 134)), "nope"], "expected": "I hope you have a fan." },
          { "inputs": [str(random.randint(-70, 39)), "yes", "no"], "expected": "What were you thinking when you left home today?!" },
          { "inputs": [str(random.randint(-70, 39)), "yes", "nah"], "expected": "What were you thinking when you left home today?!" },
          { "inputs": [str(random.randint(-70, 39)), "yes", "nope"], "expected": "What were you thinking when you left home today?!" },
            { "inputs": [str(random.randint(-70, 39)), "no", "yes", "yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "nah", "yes", "yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "nope", "yes", "yes"], "expected": "Good job staying dry!" },
        ]
        self.run_tests(weather_helper, cases, capsys, monkeypatch)

    def test_case_insensitivity(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        import random
        cases = [
            { "inputs": [str(random.randint(-70, 39)), "no", "yes", "yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "No", "Yes", "Yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "NO", "YES", "YES"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "no", "yup", "yup"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "No", "Yup", "Yup"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "NO", "YUP", "YUP"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "yes", "yes"], "expected": "Glad to hear you're dressed appropriately!" },
            { "inputs": [str(random.randint(-70, 39)), "Yes", "Yes"], "expected": "Glad to hear you're dressed appropriately!" },
            { "inputs": [str(random.randint(-70, 39)), "YES", "YES"], "expected": "Glad to hear you're dressed appropriately!" },
            { "inputs": [str(random.randint(-70, 39)), "yeah", "yeah"], "expected": "Glad to hear you're dressed appropriately!" },
            { "inputs": [str(random.randint(-70, 39)), "Yeah", "Yeah"], "expected": "Glad to hear you're dressed appropriately!" },
            { "inputs": [str(random.randint(-70, 39)), "YEAH", "YEAH"], "expected": "Glad to hear you're dressed appropriately!" },
            { "inputs": [str(random.randint(-70, 39)), "yup", "yup"], "expected": "Glad to hear you're dressed appropriately!" },
            { "inputs": [str(random.randint(-70, 39)), "Yup", "Yup"], "expected": "Glad to hear you're dressed appropriately!" },
            { "inputs": [str(random.randint(91, 134)), "no"], "expected": "I hope you have a fan." },
            { "inputs": [str(random.randint(91, 134)), "No"], "expected": "I hope you have a fan." },
            { "inputs": [str(random.randint(91, 134)), "NO"], "expected": "I hope you have a fan." },
            { "inputs": [str(random.randint(91, 134)), "nah"], "expected": "I hope you have a fan." },
            { "inputs": [str(random.randint(91, 134)), "Nah"], "expected": "I hope you have a fan." },
            { "inputs": [str(random.randint(91, 134)), "NAH"], "expected": "I hope you have a fan." },
            { "inputs": [str(random.randint(91, 134)), "nope"], "expected": "I hope you have a fan." },
            { "inputs": [str(random.randint(91, 134)), "Nope"], "expected": "I hope you have a fan." },
            { "inputs": [str(random.randint(91, 134)), "NOPE"], "expected": "I hope you have a fan." },
            { "inputs": [str(random.randint(-70, 39)), "yes", "no"], "expected": "What were you thinking when you left home today?!" },
            { "inputs": [str(random.randint(-70, 39)), "Yes", "No"], "expected": "What were you thinking when you left home today?!" },
            { "inputs": [str(random.randint(-70, 39)), "YES", "NO"], "expected": "What were you thinking when you left home today?!" },
            { "inputs": [str(random.randint(-70, 39)), "yes", "nah"], "expected": "What were you thinking when you left home today?!" },
            { "inputs": [str(random.randint(-70, 39)), "Yes", "Nah"], "expected": "What were you thinking when you left home today?!" },
            { "inputs": [str(random.randint(-70, 39)), "YES", "NAH"], "expected": "What were you thinking when you left home today?!" },
            { "inputs": [str(random.randint(-70, 39)), "yes", "nope"], "expected": "What were you thinking when you left home today?!" },
            { "inputs": [str(random.randint(-70, 39)), "Yes", "Nope"], "expected": "What were you thinking when you left home today?!" },
            { "inputs": [str(random.randint(-70, 39)), "YES", "NOPE"], "expected": "What were you thinking when you left home today?!" },
            { "inputs": [str(random.randint(-70, 39)), "no", "yes", "yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "No", "Yes", "Yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "NO", "YES", "YES"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "nah", "yes", "yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "Nah", "Yes", "Yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "NAH", "YES", "YES"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "nope", "yes", "yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "Nope", "Yes", "Yes"], "expected": "Good job staying dry!" },
            { "inputs": [str(random.randint(-70, 39)), "NOPE", "YES", "YES"], "expected": "Good job staying dry!" },
        ]
        self.run_tests(weather_helper, cases, capsys, monkeypatch)


"""
Do not run this file directly!  It won't work.
Run it using the Test panel in Visual Studio Code.
"""

from problem_set_1 import *

class Tests:

    def test_bark(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        import random
        random1 = str(random.randint(1, 100))
        random2 = str(random.randint(1, 100))
        random3 = str(random.randint(1, 100))
        cases = [
            { "inputs": ["Gustav", "4", "Schnauzer"], "expected": 'Gustav, the 4 year old Schnauzer, says, "Woof!"' },
            { "inputs": ["sport", "1", "terrier"], "expected": 'Sport, the 1 year old Terrier, says, "Woof!"' },
            { "inputs": ["FAUSTA", "66", "POODLE"], "expected": 'Fausta, the 66 year old Poodle, says, "Woof!"' },
            { "inputs": [random1, random2, random3], "expected": random1 + ', the ' + random2 + ' year old ' + random3 + ', says, "Woof!"' },
        ]

        for case in cases:
            expected_input_count = len(case['inputs'])
            counter = { 'input': 0 }
            def mock_input(x):
                counter['input'] += 1
                return case['inputs'].pop(0)
            monkeypatch.setattr("builtins.input", lambda x: mock_input(x))
            expected = case["expected"].strip()
            bark()
            actual = capsys.readouterr().out
            actual = actual.strip()
            assert actual == expected
            assert counter['input'] == expected_input_count

    def test_bark_with_validation(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        import random
        random1 = str(random.randint(1, 100))
        random2 = str(random.randint(1, 100))
        random3 = str(random.randint(1, 100))
        cases = [
            { "inputs": ["Gustav", "4", "Schnauzer"], "expected": 'Gustav, the 4 year old Schnauzer, says, "Woof!"' },
            { "inputs": ["sport", "1", "terrier"], "expected": 'Sport, the 1 year old Terrier, says, "Woof!"' },
            { "inputs": ["FAUSTA", "15", "POODLE"], "expected": 'Fausta, the 15 year old Poodle, says, "Woof!"' },
            { "inputs": ["Gustav" + random1, random2, "Terrier" + random3], "expected": 'Name error!' },
            { "inputs": ["g", "4", "Schnauzer"], "expected": 'Name error!' },
            { "inputs": ["Gustav1", "4", "Schnauzer"], "expected": 'Name error!' },
            { "inputs": ["sport", "18", "terrier"], "expected": 'Age error!' },
            { "inputs": ["sport", "-12", "terrier"], "expected": 'Age error!' },
            { "inputs": ["FAUSTA", "66", "Rottweiler"], "expected": 'Age error!' },
            { "inputs": ["Jane", "15", "Rottweiler"], "expected": 'Breed error!' },
            { "inputs": ["Snottle", "15", "Shepherd"], "expected": 'Breed error!' },
        ]
        for case in cases:
            monkeypatch.setattr("builtins.input", lambda x: case["inputs"].pop(0))
            expected = case["expected"].strip()
            bark_with_validation()
            actual = capsys.readouterr().out
            actual = actual.strip()
            assert actual == expected

    def test_respond_to_anything(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        cases = [
            { "inputs": ["Hello, are you well?"], "expected": "I'm sorry, I don't know." },
            { "inputs": ["What's your name?"], "expected": "I'm sorry, I don't know." },
            { "inputs": ["Hello, you are well."], "expected": "That's true." },
            { "inputs": ["That's your name."], "expected": "That's true." },
            { "inputs": ["Hello, you are well!"], "expected": "Exciting!" },
            { "inputs": ["That's your name!"], "expected": "Exciting!" },
            { "inputs": ["Hello, you are well"], "expected": "Please include a punctuation mark at the end of your sentence!" },
            { "inputs": ["That's your name"], "expected": "Please include a punctuation mark at the end of your sentence!" }
        ]
        for case in cases:
            expected_input_count = len(case['inputs'])
            counter = { 'input': 0 }
            def mock_input(x):
                counter['input'] += 1
                return case['inputs'].pop(0)
            monkeypatch.setattr("builtins.input", lambda x: mock_input(x))
            expected = case["expected"].strip()
            respond_to_anything()
            actual = capsys.readouterr().out
            actual = actual.strip()
            assert actual == expected
            assert counter['input'] == expected_input_count

    def test_respond_to_anything_but_nonsense(self, capsys, monkeypatch):
        """
        Check whether the output is correct in all cases.
        """
        cases = [
            { "inputs": ["Hello, are you well?"], "expected": "I'm sorry, I don't know." },
            { "inputs": ["What's your name?"], "expected": "I'm sorry, I don't know." },
            { "inputs": ["Hello, you are well."], "expected": "That's true." },
            { "inputs": ["That's your name."], "expected": "That's true." },
            { "inputs": ["Hello, you are well!"], "expected": "Exciting!" },
            { "inputs": ["That's your name!"], "expected": "Exciting!" },
            { "inputs": ["Hello, you are well"], "expected": "Please include a punctuation mark at the end of your sentence!" },
            { "inputs": ["That's your name"], "expected": "Please include a punctuation mark at the end of your sentence!" },
            { "inputs": ["That's nonsense."], "expected": "" },
            { "inputs": ["Nonsense that is"], "expected": "" },
            { "inputs": ["There's nothing but nonsense in this test"], "expected": "" },
        ]
        for case in cases:
            expected_input_count = len(case['inputs'])
            counter = { 'input': 0 }
            def mock_input(x):
                counter['input'] += 1
                return case['inputs'].pop(0)
            monkeypatch.setattr("builtins.input", lambda x: mock_input(x))
            expected = case["expected"].strip()
            respond_to_anything_but_nonsense()
            actual = capsys.readouterr().out
            actual = actual.strip()
            assert actual == expected
            assert counter['input'] == expected_input_count

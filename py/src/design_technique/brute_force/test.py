import unittest
from chapter_exercises import Challenge

# python3 -m unittest test.py
# python3 -m unittest test.TestChallenge.test_exercise35

class TestChallenge(unittest.TestCase):
    def test_is_even(self):
        challenge = Challenge()
        self.assertTrue(challenge.is_even(4))
        self.assertFalse(challenge.is_even(5))

    def test_exercise35(self):
        challenge = Challenge()
        result = challenge.exercise35()
        self.assertIsInstance(result, int)
        self.assertGreaterEqual(result, 0)
        

    def test_exercise31(self):
        challenge = Challenge()
        challenge.exercise31()

    def test_exercise32(self):
        challenge = Challenge()
        challenge.exercise32()

    def test_exercise33(self):
        challenge = Challenge()
        challenge.exercise33()

    def test_exercise34(self):
        challenge = Challenge()
        challenge.exercise34()

if __name__ == '__main__':
    unittest.main()

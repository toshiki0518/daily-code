import unittest
from chapter_exercises import Challenge

# python3 -m unittest test.py

class TestChallenge(unittest.TestCase):
    def test_is_even(self):
        challenge = Challenge()
        self.assertTrue(challenge.is_even(4), "4は偶数であるべきです")
        self.assertFalse(challenge.is_even(5), "5は偶数ではありません")

    def test_exercise35(self):
        """
        $ python3 -m unittest test.TestChallenge.test_exercise35
        """
        challenge = Challenge()
        result = challenge.exercise35()
        self.assertIsInstance(result, int, "結果は整数であるべきです")
        self.assertGreaterEqual(result, 0, "結果は0以上であるべきです")
        

    def test_exercise36(self):
        challenge = Challenge()
        """
        $ python3 -m unittest test.TestChallenge.test_exercise36
        """
        challenge.exercise36(5, 10)
        print("\nTest Case 2:")
        challenge.exercise36(3, 6)

    def test_exercise36_case1(self):
        """
        $ python3 -m unittest test.TestChallenge.test_exercise36_1
        """
        challenge = Challenge()
        result = challenge.exercise36(5, 10)

    def test_exercise36_case2(self):
        """
        $ python3 -m unittest test.TestChallenge.test_exercise36_2
        """
        challenge = Challenge()
        result = challenge.exercise36(3, 6)

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

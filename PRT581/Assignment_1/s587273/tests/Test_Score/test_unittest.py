import Test_Score
import unittest


class Test_TestScore(unittest.TestCase):
    # If the player score is not equal to 5, continue the loop #

    def playerScore(self):
        self.assertEqual(Test_Score.playerScore(4), 1)


if __name__ == '__main__':
    unittest.main()

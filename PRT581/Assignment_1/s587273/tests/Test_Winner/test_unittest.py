import Test_winner
import unittest


class Test_Testwinner(unittest.TestCase):
    # Test for winner of round from defined list of options #
    # This test will return the winner of the hand, either 'CPU' or 'Player' #
    # Only one combination can be the outcome #

    def test_checkForWinner(self):
        self.assertTrue(Test_winner.checkForWinner(1), 2)


if __name__ == '__main__':
    unittest.main()

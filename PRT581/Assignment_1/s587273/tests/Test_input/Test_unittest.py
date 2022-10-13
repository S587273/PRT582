import Test_input
import unittest


class Test_Testinput(unittest.TestCase):
    # Test for valid input from defined list of options #

    CpuScore = 0
    PlayerScore = 0
    Draw = 0
    PossibleDeals = ["Rock", "Paper", "Scissors"]

    def test_testcheckInput(self):
        self.assertEqual(Test_input.checkInput(1), 2)

    while True:
        playerHand = input("\n Pick a hand. Rock, Paper or Scissors:")
        if (playerHand == "Rock" or playerHand == "Paper" or
                playerHand == "Scissors"):
            break
        else:
            print("Invalid input. Try again!")


if __name__ == '__main__':
    unittest.main()

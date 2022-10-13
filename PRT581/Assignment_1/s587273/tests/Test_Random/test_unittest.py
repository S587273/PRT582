import Test_Random
import unittest


class Test_TestRandom(unittest.TestCase):
    # Test CPU choice is random from defined list of options #

    def test_randomChoice(self):
        self.assertEqual(Test_Random.randomChoice(1), 2)


if __name__ == '__main__':
    unittest.main()

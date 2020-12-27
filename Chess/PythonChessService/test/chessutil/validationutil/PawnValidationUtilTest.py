import setup
import sys
import os
directory = os.getcwd()
sys.path.append(directory)
import unittest
from main.chessutil.validationutil import PawnValidationUtil

class PawnValidationUtilTest(unittest.TestCase):

    def test__canCapture(self):
        self.assertTrue(PawnValidationUtil.canCapture())

    def test__canEnPassant(self):
        self.assertEqual(1,0)


if __name__ == '__main__':
    unittest.main()
import unittest
from math import sqrt


class CaseTest(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(sqrt(25), 5)
        self.assertEqual(sqrt(9), 3)
        self.assertEqual(sqrt(0), 0)


if __name__ == '__main__':
    unittest.main()

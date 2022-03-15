
import unittest
from kk import plus

class testkk(unittest.TestCase):
    def test_kk(self):
        self.assertEqual(plus(2, 4), 6)
        # self.assertEqual(kk.plus(1, 0.5), 1.5)


if __name__ == '__main__':
    unittest.main()

import unittest
from hw3_fibonacci import fibonacci


class FibonacciTest(unittest.TestCase):

    def test_1(self):

        result = fibonacci(5)

        self.assertEqual(5, result)


if __name__ == '__main__':
    unittest.main()

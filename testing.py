import unittest
from fib import fibonacci
from sum_natural_num import sum_natural_num

class TestAll(unittest.TestCase):
    # testing the fibonacci function
    def test_fibonacci(self):
        fib = [0,1,1,2,3,5,8,13,21]
        for i, num in enumerate(fib):
            self.assertEqual(fibonacci(i), num, "something went wrong in fibonacci")

    # testing sum_natural_num
    def test_sum_natural_num(self):
        self.assertEqual(sum_natural_num(50), (50*51)/2, "something went wrong in sum_natural_num")


if __name__ == "__main__":
    unittest.main()

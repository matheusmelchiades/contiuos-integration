import unittest   # The test framework

from main import calculate_sum

class Test_main(unittest.TestCase):
    def test_calculate_sum(self):
        result = calculate_sum(1, 2)
        assert result == 3


if __name__ == '__main__':
    unittest.main()

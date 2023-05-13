import unittest

class TestCalculateAverage(unittest.TestCase):
    def setUp(self):
        self.my_numbers = [10, 15, 20, 25, 30]

    def test_calculate_average(self):
        result = calculate_average(self.my_numbers)
        self.assertEqual(result, 20.0)

    def test_calculate_average_empty_list(self):
        result = calculate_average([])
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

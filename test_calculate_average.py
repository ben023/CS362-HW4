import unittest
import calculate_average

class TestAverage(unittest.TestCase):
    def test1(self):
        self.assertEqual(calculate_average.calc_average([1,2,3,4,"a"]), "Invalid Set")
    def test2(self):
        self.assertRaises(ZeroDivisionError, lambda: calculate_average.calc_average([]))
    def test3(self):
        self.assertEqual(calculate_average.calc_average([1,2,3,4,6]), 3.2)

if __name__ == '__main__':
    unittest.main()
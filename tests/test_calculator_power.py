import unittest

from utils import calculator


class TestCalculatorPower(unittest.TestCase):
    def test_power(self):
        self.assertEqual(calculator.calculate(2, "^", 10), 1024)
        self.assertAlmostEqual(calculator.calculate(9, "^", 0.5), 3)
        self.assertEqual(calculator.calculate(2, "^", -1), 0.5)

    def test_complex_result_rejected(self):
        with self.assertRaises(ValueError):
            calculator.power(-8, 1 / 3)


if __name__ == "__main__":
    unittest.main()

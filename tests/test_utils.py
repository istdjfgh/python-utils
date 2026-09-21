import unittest

from utils import calculator, converter, password_generator, text_stats


class TestCalculator(unittest.TestCase):
    def test_operations(self):
        self.assertEqual(calculator.calculate(2, "+", 3), 5)
        self.assertEqual(calculator.calculate(10, "/", 4), 2.5)

    def test_zero_division(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(1, 0)


class TestConverter(unittest.TestCase):
    def test_length(self):
        self.assertAlmostEqual(converter.convert_length(1, "km", "m"), 1000)

    def test_temperature(self):
        self.assertAlmostEqual(converter.convert_temperature(100, "C", "F"), 212)
        self.assertAlmostEqual(converter.convert_temperature(0, "C", "K"), 273.15)


class TestPassword(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(password_generator.generate_password(16)), 16)

    def test_too_short(self):
        with self.assertRaises(ValueError):
            password_generator.generate_password(3)


class TestTextStats(unittest.TestCase):
    def test_stats(self):
        result = text_stats.stats("Привіт світ. Привіт знову!")
        self.assertEqual(result["слів"], 4)
        self.assertEqual(result["речень"], 2)


if __name__ == "__main__":
    unittest.main()

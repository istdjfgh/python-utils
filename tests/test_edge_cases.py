import string
import unittest

from utils import calculator, converter, password_generator, text_stats


class TestCalculatorEdgeCases(unittest.TestCase):
    def test_subtraction_and_multiplication(self):
        self.assertEqual(calculator.calculate(7, "-", 12), -5)
        self.assertEqual(calculator.calculate(-4, "*", 3), -12)

    def test_unknown_operation(self):
        with self.assertRaises(ValueError):
            calculator.calculate(1, "%", 2)

    def test_division_by_zero_through_dispatcher(self):
        with self.assertRaises(ZeroDivisionError):
            calculator.calculate(4, "/", 0)


class TestConverterEdgeCases(unittest.TestCase):
    def test_mass_conversion(self):
        self.assertAlmostEqual(converter.convert_mass(2, "kg", "g"), 2000)
        self.assertAlmostEqual(converter.convert_mass(1, "lb", "kg"), 0.45359237)

    def test_length_round_trip(self):
        miles = converter.convert_length(1234, "m", "mi")
        self.assertAlmostEqual(converter.convert_length(miles, "mi", "m"), 1234)

    def test_temperature_round_trip(self):
        fahrenheit = converter.convert_temperature(-40, "C", "F")
        self.assertAlmostEqual(fahrenheit, -40)
        self.assertAlmostEqual(converter.convert_temperature(fahrenheit, "F", "C"), -40)

    def test_invalid_units(self):
        for conversion in (converter.convert_length, converter.convert_mass,
                           converter.convert_temperature):
            with self.subTest(conversion=conversion.__name__):
                with self.assertRaises(KeyError):
                    conversion(1, "unknown", "unknown")


class TestPasswordEdgeCases(unittest.TestCase):
    def test_minimum_length_includes_each_required_group(self):
        password = password_generator.generate_password(4)
        self.assertEqual(len(password), 4)
        for pool in (string.ascii_lowercase, string.ascii_uppercase,
                     string.digits, "!@#$%^&*()-_=+"):
            with self.subTest(pool=pool):
                self.assertTrue(any(character in pool for character in password))

    def test_optional_character_groups(self):
        for use_digits in (False, True):
            for use_symbols in (False, True):
                with self.subTest(digits=use_digits, symbols=use_symbols):
                    password = password_generator.generate_password(
                        16, use_digits=use_digits, use_symbols=use_symbols
                    )
                    self.assertEqual(len(password), 16)
                    self.assertEqual(any(character.isdigit() for character in password),
                                     use_digits)
                    self.assertEqual(any(not character.isalnum() for character in password),
                                     use_symbols)

    def test_strength_levels(self):
        self.assertEqual(password_generator.password_strength("Abcdefghi12!"), "сильний")
        self.assertEqual(password_generator.password_strength("Abcdefghi123"), "добрий")
        self.assertEqual(password_generator.password_strength("Ab1"), "середній")
        self.assertEqual(password_generator.password_strength("abc"), "слабкий")


class TestTextEdgeCases(unittest.TestCase):
    def test_empty_text(self):
        self.assertEqual(text_stats.stats(""), {
            "символів": 0, "слів": 0, "речень": 0, "найчастіші": []
        })

    def test_repeated_sentence_punctuation(self):
        result = text_stats.stats("Привіт?! Світ...")
        self.assertEqual(result["слів"], 2)
        self.assertEqual(result["речень"], 2)

    def test_ukrainian_words_and_frequency(self):
        text = "П'ять п’ять синьо-жовтий Привіт привіт"
        result = text_stats.stats(text)
        self.assertEqual(result["символів"], len(text))
        self.assertEqual(result["слів"], 5)
        self.assertEqual(result["найчастіші"][0], ("привіт", 2))
        self.assertIn("синьо-жовтий", text_stats.word_list(text))


if __name__ == "__main__":
    unittest.main()

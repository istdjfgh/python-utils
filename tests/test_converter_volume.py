import unittest
from unittest import mock

from utils import converter


class TestConverterVolume(unittest.TestCase):
    def test_basic(self):
        self.assertAlmostEqual(converter.convert_volume(1, "l", "ml"), 1000)
        self.assertAlmostEqual(converter.convert_volume(1, "m3", "l"), 1000)
        self.assertAlmostEqual(converter.convert_volume(1, "gal", "l"), 3.785411784)

    def test_roundtrip(self):
        value = converter.convert_volume(converter.convert_volume(5, "gal", "ml"), "ml", "gal")
        self.assertAlmostEqual(value, 5)

    def test_unknown_unit(self):
        with self.assertRaises(KeyError):
            converter.convert_volume(1, "cup", "l")

    def test_menu_has_volume(self):
        answers = iter(["volume", "2", "l", "ml"])
        with mock.patch("builtins.input", lambda _="": next(answers)),                 mock.patch("builtins.print") as fake_print:
            converter.run()
        fake_print.assert_called_with("Результат: 2000.0000 ml")


if __name__ == "__main__":
    unittest.main()

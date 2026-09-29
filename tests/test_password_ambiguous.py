import string
import unittest
from unittest import mock

from utils import password_generator as pg


class TestPasswordAmbiguous(unittest.TestCase):
    def test_excluded(self):
        for _ in range(300):
            pwd = pg.generate_password(64, exclude_ambiguous=True)
            self.assertFalse(set(pwd) & set(pg.AMBIGUOUS), pwd)

    def test_default_unchanged(self):
        seen = set()
        for _ in range(300):
            seen |= set(pg.generate_password(64)) & set(pg.AMBIGUOUS)
        self.assertEqual(seen, set(pg.AMBIGUOUS))

    def test_groups_kept(self):
        pwd = pg.generate_password(8, exclude_ambiguous=True)
        self.assertEqual(len(pwd), 8)
        self.assertTrue(any(c.islower() for c in pwd))
        self.assertTrue(any(c.isupper() for c in pwd))
        self.assertTrue(any(c.isdigit() for c in pwd))
        self.assertTrue(any(c in string.punctuation for c in pwd))

    def test_menu_question(self):
        answers = iter(["16", "y"])
        with mock.patch("builtins.input", lambda _="": next(answers)),                 mock.patch("builtins.print") as fake_print:
            pg.run()
        printed = fake_print.call_args[0][0]
        password = printed.split()[1]
        self.assertEqual(len(password), 16)
        self.assertFalse(set(password) & set(pg.AMBIGUOUS))


if __name__ == "__main__":
    unittest.main()

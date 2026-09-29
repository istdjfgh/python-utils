import unittest
from unittest import mock

from utils import text_stats


class TestTextStatsExtra(unittest.TestCase):
    def test_average_word_length(self):
        self.assertEqual(text_stats.average_word_length("кіт і пес"), 2.33)

    def test_empty_text(self):
        self.assertEqual(text_stats.average_word_length(""), 0)
        self.assertEqual(text_stats.reading_time_minutes(""), 0)

    def test_reading_time(self):
        text = " ".join(["слово"] * 400)
        self.assertEqual(text_stats.reading_time_minutes(text), 2.0)
        self.assertEqual(text_stats.reading_time_minutes(text, wpm=400), 1.0)

    def test_bad_wpm(self):
        with self.assertRaises(ValueError):
            text_stats.reading_time_minutes("текст", wpm=0)

    def test_stats_dict_unchanged(self):
        self.assertEqual(set(text_stats.stats("а б")), {"символів", "слів", "речень", "найчастіші"})

    def test_menu_output(self):
        with mock.patch("builtins.input", lambda _="": "кіт і пес"),                 mock.patch("builtins.print") as fake_print:
            text_stats.run()
        lines = [c[0][0] for c in fake_print.call_args_list]
        self.assertIn("середня довжина слова: 2.33", lines)


if __name__ == "__main__":
    unittest.main()

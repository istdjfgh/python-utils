"""Модуль статистики тексту (відповідальний: Учасник 4)."""

import re
from collections import Counter


def word_list(text: str) -> list:
    return re.findall(r"[\w'’-]+", text.lower())


def stats(text: str) -> dict:
    words = word_list(text)
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    return {
        "символів": len(text),
        "слів": len(words),
        "речень": len(sentences),
        "найчастіші": Counter(words).most_common(3),
    }


def run() -> None:
    text = input("Введіть текст: ")
    for key, value in stats(text).items():
        print(f"{key}: {value}")

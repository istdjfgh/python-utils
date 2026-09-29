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


def average_word_length(text: str) -> float:
    """Середня довжина слова (0 для порожнього тексту)."""
    words = word_list(text)
    if not words:
        return 0
    return round(sum(len(w) for w in words) / len(words), 2)


def reading_time_minutes(text: str, wpm: int = 200) -> float:
    """Приблизний час читання у хвилинах за швидкості wpm слів на хвилину."""
    if wpm <= 0:
        raise ValueError("Швидкість читання має бути додатною")
    return round(len(word_list(text)) / wpm, 2)


def run() -> None:
    text = input("Введіть текст: ")
    for key, value in stats(text).items():
        print(f"{key}: {value}")
    print(f"середня довжина слова: {average_word_length(text)}")
    print(f"час читання (хв): {reading_time_minutes(text)}")

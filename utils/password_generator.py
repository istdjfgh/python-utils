"""Модуль генератора паролів (відповідальний: Учасник 3)."""

import secrets
import string

AMBIGUOUS = "0O1lI"  # символи, які легко сплутати


def generate_password(length: int = 12, use_digits: bool = True,
                      use_symbols: bool = True,
                      exclude_ambiguous: bool = False) -> str:
    """Генерує криптографічно стійкий пароль."""
    if length < 4:
        raise ValueError("Мінімальна довжина пароля — 4 символи")
    pools = [string.ascii_lowercase, string.ascii_uppercase]
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+")
    if exclude_ambiguous:
        pools = ["".join(c for c in pool if c not in AMBIGUOUS) for pool in pools]
    # Гарантуємо хоча б один символ з кожної групи
    chars = [secrets.choice(pool) for pool in pools]
    alphabet = "".join(pools)
    chars += [secrets.choice(alphabet) for _ in range(length - len(chars))]
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def password_strength(password: str) -> str:
    score = sum([
        len(password) >= 12,
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password),
    ])
    return {5: "сильний", 4: "добрий", 3: "середній"}.get(score, "слабкий")


def run() -> None:
    try:
        length = int(input("Довжина пароля (за замовчуванням 12): ") or 12)
        exclude = input("Виключити схожі символи? (y/n): ").strip().lower() == "y"
        pwd = generate_password(length, exclude_ambiguous=exclude)
        print(f"Пароль: {pwd} ({password_strength(pwd)})")
    except ValueError as err:
        print(f"Помилка: {err}")

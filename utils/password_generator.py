"""Модуль генератора паролів (відповідальний: Учасник 3)."""

import secrets
import string


def generate_password(length: int = 12, use_digits: bool = True,
                      use_symbols: bool = True) -> str:
    """Генерує криптографічно стійкий пароль."""
    if length < 4:
        raise ValueError("Мінімальна довжина пароля — 4 символи")
    pools = [string.ascii_lowercase, string.ascii_uppercase]
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+")
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
        pwd = generate_password(length)
        print(f"Пароль: {pwd} ({password_strength(pwd)})")
    except ValueError as err:
        print(f"Помилка: {err}")

"""Модуль калькулятора (відповідальний: Учасник 1)."""


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("Ділення на нуль неможливе")
    return a / b


OPERATIONS = {"+": add, "-": subtract, "*": multiply, "/": divide}


def calculate(a: float, op: str, b: float) -> float:
    """Виконує операцію op над числами a та b."""
    if op not in OPERATIONS:
        raise ValueError(f"Невідома операція: {op}")
    return OPERATIONS[op](a, b)


def run() -> None:
    try:
        a = float(input("Перше число: "))
        op = input("Операція (+ - * /): ").strip()
        b = float(input("Друге число: "))
        print(f"Результат: {calculate(a, op, b)}")
    except (ValueError, ZeroDivisionError) as err:
        print(f"Помилка: {err}")

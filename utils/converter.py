"""Модуль конвертера одиниць (відповідальний: Учасник 2)."""

# Коефіцієнти відносно базової одиниці: метр та кілограм
LENGTH = {"mm": 0.001, "cm": 0.01, "m": 1.0, "km": 1000.0,
          "in": 0.0254, "ft": 0.3048, "mi": 1609.344}
MASS = {"g": 0.001, "kg": 1.0, "t": 1000.0, "lb": 0.45359237, "oz": 0.028349523125}
VOLUME = {"ml": 0.001, "l": 1.0, "m3": 1000.0, "gal": 3.785411784}  # база — літр (gal = US gallon)


def convert_length(value: float, src: str, dst: str) -> float:
    return value * LENGTH[src] / LENGTH[dst]


def convert_mass(value: float, src: str, dst: str) -> float:
    return value * MASS[src] / MASS[dst]


def convert_volume(value: float, src: str, dst: str) -> float:
    return value * VOLUME[src] / VOLUME[dst]


def convert_temperature(value: float, src: str, dst: str) -> float:
    """Підтримує C, F, K."""
    to_c = {"C": lambda v: v, "F": lambda v: (v - 32) * 5 / 9, "K": lambda v: v - 273.15}
    from_c = {"C": lambda v: v, "F": lambda v: v * 9 / 5 + 32, "K": lambda v: v + 273.15}
    if src not in to_c or dst not in from_c:
        raise KeyError("Підтримуються лише C, F, K")
    return from_c[dst](to_c[src](value))


def run() -> None:
    kind = input("Тип (length/mass/volume/temp): ").strip()
    try:
        value = float(input("Значення: "))
        src = input("З одиниці: ").strip()
        dst = input("У одиницю: ").strip()
        func = {"length": convert_length, "mass": convert_mass, "volume": convert_volume,
                "temp": convert_temperature}[kind]
        print(f"Результат: {func(value, src, dst):.4f} {dst}")
    except (ValueError, KeyError):
        print("Помилка: некоректне значення або одиниця")

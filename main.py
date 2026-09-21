"""Точка входу: меню вибору утиліти."""

from utils import __version__, calculator, converter, password_generator, text_stats

MENU = {
    "1": ("Калькулятор", calculator.run),
    "2": ("Конвертер одиниць", converter.run),
    "3": ("Генератор паролів", password_generator.run),
    "4": ("Статистика тексту", text_stats.run),
}


def main() -> None:
    print(f"Python Utils v{__version__}")
    while True:
        print()
        for key, (title, _) in MENU.items():
            print(f"{key}. {title}")
        print("0. Вихід")
        choice = input("Ваш вибір: ").strip()
        if choice == "0":
            break
        if choice in MENU:
            MENU[choice][1]()
        else:
            print("Невідомий пункт меню")


if __name__ == "__main__":
    main()

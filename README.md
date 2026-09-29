# Python Utils — навчальний проєкт

Набір невеликих консольних утиліт на Python із текстовим меню (калькулятор, конвертер, генератор паролів, статистика тексту), створений у межах лабораторної роботи №2
«Налаштування середовища розробки та Git workflow».

## Можливості

| Модуль | Файл | Що вміє |
|--------|------|---------|
| Калькулятор | `utils/calculator.py` | `+ − × ÷ ^`, обробка ділення на нуль і комплексних результатів |
| Конвертер одиниць | `utils/converter.py` | довжина, маса, об'єм, температура |
| Генератор паролів | `utils/password_generator.py` | криптостійкі паролі, оцінка надійності, виключення схожих символів |
| Статистика тексту | `utils/text_stats.py` | символи, слова, речення, найчастіші слова, середня довжина слова, час читання |

## Технологічний стек

- Python 3.10+ (лише стандартна бібліотека, зовнішні залежності не потрібні)
- `unittest` для тестів
- Git + GitHub (Feature Branch Workflow / GitHub Flow, Conventional Commits)
- Visual Studio Code

## Встановлення та запуск

```bash
git clone https://github.com/istdjfgh/python-utils.git
cd python-utils
python -m venv .venv                     # необов'язково
python main.py
```

Активація середовища необов'язкова, оскільки зовнішніх залежностей немає.
У PowerShell: `.\.venv\Scripts\Activate.ps1`.
У Linux/macOS: `source .venv/bin/activate`.

## Тести

```bash
python -m unittest discover -v
```

## Структура проєкту

```text
python-utils/
├── main.py                # меню вибору утиліти
├── utils/                 # модулі утиліт
├── tests/                 # модульні тести
├── docs/                  # документація
├── reports/               # звіт про лабораторну
├── .github/               # шаблони Issues та Pull Request
├── .gitignore
├── CHANGELOG.md
└── README.md
```

## Правила роботи з репозиторієм

1. Кожне завдання — окремий Issue.
2. Кожна зміна — окрема гілка `feature/<назва>` від актуальної `main`.
3. Зміни потрапляють у `main` лише через Pull Request.
4. У описі PR вказується `Closes #<номер Issue>`.
5. Повідомлення комітів — за [Conventional Commits](https://www.conventionalcommits.org/uk/v1.0.0/).

## Автор

Власник репозиторію: [@istdjfgh](https://github.com/istdjfgh).
Лабораторну виконано індивідуально.

Звіт: [reports/lab02-report.md](reports/lab02-report.md).
Історія змін: [CHANGELOG.md](CHANGELOG.md).

## Посилання для перевірки

- [Реліз v1.1.0](https://github.com/istdjfgh/python-utils/releases/tag/v1.1.0)
- [Закриті Pull Requests](https://github.com/istdjfgh/python-utils/pulls?q=is%3Apr+is%3Aclosed)
- [Issues](https://github.com/istdjfgh/python-utils/issues?q=is%3Aissue)

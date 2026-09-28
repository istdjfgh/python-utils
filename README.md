# Python Utils — командний навчальний проєкт

Набір невеликих консольних утиліт на Python, створений у межах лабораторної роботи №2
«Налаштування середовища розробки та Git workflow».

## Можливості

| Модуль | Файл | Відповідальний |
|--------|------|----------------|
| Калькулятор (+ − × ÷ ^) | `utils/calculator.py` | @istdjfgh (team lead) |
| Конвертер одиниць (довжина, маса, температура, об'єм) | `utils/converter.py` | @and701 |
| Генератор паролів з оцінкою надійності | `utils/password_generator.py` | @xx1x1x2x |
| Статистика тексту | `utils/text_stats.py` | @логін-4-учасника (QA) |

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
├── reports/               # звіти учасників
├── .github/               # шаблони Issues та Pull Request
├── .gitignore
├── CHANGELOG.md
└── README.md
```

## Правила командної роботи

1. Кожне завдання — окремий Issue.
2. Кожна функція — окрема гілка `feature/<назва>` від актуальної `main`.
3. Зміни потрапляють у `main` лише через Pull Request із принаймні одним схваленням.
4. У описі PR вказується `Closes #<номер Issue>`.
5. Повідомлення комітів — за [Conventional Commits](https://www.conventionalcommits.org/uk/v1.0.0/).

## Команда

| Роль | GitHub | Звіт |
|------|--------|------|
| Team lead, калькулятор, релізи | @istdjfgh | [lab02-report.md](reports/lab02-report.md) |
| Developer, конвертер, review | @and701 | [lab02-report-and701.md](reports/lab02-report-and701.md) |
| Developer, генератор паролів, конфлікт злиття | @xx1x1x2x | [lab02-report-xx1x1x2x.md](reports/lab02-report-xx1x1x2x.md) |
| QA, статистика тексту | @логін-4-учасника | [lab02-report-логін-4-учасника.md](reports/lab02-report-логін-4-учасника.md) |

Базовий код утиліт узято з наданого навчального архіву `python-utils-lab02.zip`.
Частину коду й документації підготовлено з допомогою ШІ.

## Посилання для перевірки

- [Релізи](https://github.com/istdjfgh/python-utils/releases): `v1.0.0`, `v1.1.0`.
- [Завдання команди (Issues)](https://github.com/istdjfgh/python-utils/issues?q=is%3Aissue).
- [Pull Request з review](https://github.com/istdjfgh/python-utils/pulls?q=is%3Apr).
- Навчальний конфлікт злиття: Issue #3 — PR #10 та PR, що закриває #3.

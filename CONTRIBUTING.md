# Участь у розробці

1. Клонувати репозиторій і запустити тести:

   ```powershell
   git clone https://github.com/istdjfgh/python-utils.git
   cd python-utils
   python -m unittest discover -v
   ```

2. Завести Issue з описом та критеріями готовності.
3. Створити гілку `feature/<назва>` від актуальної `main`.
4. Внести зміни разом із тестами; повідомлення комітів — за Conventional Commits
   (`feat:`, `fix:`, `docs:`, `test:`, `chore:`).
5. Відправити гілку та відкрити Pull Request у `main`.
6. В описі вказати `Closes #N`, де N — номер відповідного Issue.
7. Перед злиттям переконатися, що `python -m unittest discover` проходить без помилок.

## Конфлікти злиття

Якщо PR конфліктує з `main`: підтягнути `main` у свою гілку
(`git merge origin/main`), вручну вирішити маркери `<<<<<<<` / `>>>>>>>`,
запустити тести, зробити коміт і відправити гілку.

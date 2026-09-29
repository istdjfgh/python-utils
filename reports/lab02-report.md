# Лабораторна робота №02 — звіт

**Тема:** Налаштування середовища розробки та Git workflow.
**ПІБ:** Пламетюк Ілля Олександрович
**Група:** ІПЗ-22
**Дата:** 29 вересня 2026 року
**Репозиторій:** https://github.com/istdjfgh/python-utils
**Акаунт GitHub:** `istdjfgh`
**Формат виконання:** індивідуально.

## Мета

Опанувати базові операції Git, організацію гілок і Pull Request,
вирішення конфліктів та підготовку релізу.

## Середовище

- Git, Python 3.10+, Visual Studio Code.
- Проєкт: чотири консольні утиліти (`calculator`, `converter`, `password_generator`,
  `text_stats`) із меню в `main.py`; лише стандартна бібліотека, тести на `unittest`.

## Виконана робота

Задачі оформлювались як Issues, кожна зміна — окрема гілка від актуальної `main`
і окремий Pull Request із `Closes #N`. Злиття виконувалось звичайним merge-комітом,
щоб у графі історії були видні гілки.

| PR | Гілка | Що зроблено | Issue |
|----|-------|-------------|-------|
| [#5](https://github.com/istdjfgh/python-utils/pull/5) | `codex/edge-case-tests` | 13 тестів граничних випадків | #1 |
| [#9](https://github.com/istdjfgh/python-utils/pull/9) | `feature/calculator-power` | операція `^` у калькуляторі | #6 |
| [#10](https://github.com/istdjfgh/python-utils/pull/10) | `feature/readme-intro` | перелік утиліт в описі README (перша сторона конфлікту) | #3 |
| [#13](https://github.com/istdjfgh/python-utils/pull/13) | `feature/readme-badge` | згадка текстового меню в тому самому рядку (друга сторона, конфлікт вирішено) | #3 |
| [#14](https://github.com/istdjfgh/python-utils/pull/14) | `feature/converter-volume` | одиниці об'єму в конвертері | #7 |
| [#15](https://github.com/istdjfgh/python-utils/pull/15) | `feature/password-ambiguous` | виключення схожих символів у паролях | #8 |
| [#16](https://github.com/istdjfgh/python-utils/pull/16) | `feature/text-stats-extra` | середня довжина слова та час читання | #12 |

Кількість тестів на `main`: 7 (початкові) → 20 (PR #5) → 22 (#9) → 26 (#14) → 30 (#15) → 36 (#16).

## Навчальний конфлікт

Дві гілки створено від однієї версії `main`; обидві змінюють перший рядок опису в `README.md`
(PR #10 і PR #13). Після злиття PR #10 у PR #13 виник конфлікт злиття.
Вирішення: `git merge origin/main` у гілці `feature/readme-badge`, вручну прибрано маркери
`<<<<<<<` / `=======` / `>>>>>>>`, залишено рядок, що об'єднує обидві правки,
запущено тести, створено merge-коміт `bf7fc48` та відправлено гілку; після цього PR #13 злито.

Скріншоти (додати): <img width="1200" height="900" alt="gh-repo" src="https://github.com/user-attachments/assets/4f3c7ca7-b31d-420d-87c8-c6f357179a42" /> <img width="1200" height="760" alt="gh-issues" src="https://github.com/user-attachments/assets/7eb438ad-8182-4dbf-89b0-7ef781163cc1" /> <img width="1200" height="820" alt="gh-prs" src="https://github.com/user-attachments/assets/7e44df53-e201-41d0-92d2-97c8bb863757" /> <img width="1200" height="900" alt="gh-pr13" src="https://github.com/user-attachments/assets/95cb580d-6395-4f8d-b018-7abc065b037f" /> <img width="1000" height="1018" alt="term-graph" src="https://github.com/user-attachments/assets/b56168b6-c86e-4420-9f12-9709c42d4c67" />
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 1018" width="1000" height="1018" role="img" aria-label="PowerShell — python-utils">
<defs><filter id="sh" x="-5%" y="-5%" width="110%" height="115%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000" flood-opacity=".45"/></filter></defs>
<rect x="8" y="4" width="984" height="1002" rx="14" fill="#0d1117" stroke="#30363d" filter="url(#sh)"/>
<path d="M8 18a14 14 0 0 1 14-14h956a14 14 0 0 1 14 14v22H8z" fill="#161b22"/>
<g transform="translate(8 4)"><circle cx="22" cy="22" r="6.5" fill="#ff5f57"/><circle cx="44" cy="22" r="6.5" fill="#febc2e"/><circle cx="66" cy="22" r="6.5" fill="#28c840"/></g>
<text x="500.0" y="30" fill="#8b949e" font-family="Inter, 'Segoe UI', system-ui, sans-serif" font-size="13" font-weight="500" xml:space="preserve" text-anchor="middle">PowerShell — python-utils</text>
<text x="30.0" y="80" fill="#7ee787" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >PS C:\python-utils&gt; </text><text x="199.0" y="80" fill="#e6edf3" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >git log --graph --oneline --decorate -n 24</text>
<text x="30.0" y="110" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="46.9" y="110" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >9df0c0e</text>
<text x="114.5" y="110" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >(</text>
<text x="123.0" y="110" fill="#39c5cf" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >HEAD -&gt; main</text>
<text x="224.3" y="110" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >, </text>
<text x="241.2" y="110" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >tag: v1.1.0</text>
<text x="334.2" y="110" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >, </text>
<text x="351.1" y="110" fill="#ff7b72" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >origin/main</text>
<text x="444.0" y="110" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >, </text>
<text x="460.9" y="110" fill="#ff7b72" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >origin/HEAD</text>
<text x="553.9" y="110" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >)</text>
<text x="570.8" y="110" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >docs: підготовка релізу 1.1.0 (#17)</text>
<text x="30.0" y="131" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="131" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="30.0" y="152" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="152" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="63.8" y="152" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >f454fef</text>
<text x="131.4" y="152" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >(</text>
<text x="139.8" y="152" fill="#ff7b72" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >origin/docs/release-1.1.0</text>
<text x="351.1" y="152" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >)</text>
<text x="368.0" y="152" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >docs: звіт про лабораторну роботу №02</text>
<text x="30.0" y="173" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="173" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="63.8" y="173" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >8ece4e1</text>
<text x="131.4" y="173" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >docs: оновити README та CONTRIBUTING для релізу 1.1.0</text>
<text x="30.0" y="194" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="194" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="63.8" y="194" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >da05b83</text>
<text x="131.4" y="194" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >chore(release): версія 1.1.0 та запис у CHANGELOG</text>
<text x="30.0" y="215" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="215" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="30.0" y="236" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="46.9" y="236" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >27e1c39</text>
<text x="114.5" y="236" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >feat(text-stats): середня довжина слова та час читання (#16)</text>
<text x="30.0" y="257" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="257" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="30.0" y="278" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="278" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="63.8" y="278" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >917bc64</text>
<text x="131.4" y="278" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >(</text>
<text x="139.8" y="278" fill="#ff7b72" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >origin/feature/text-stats-extra</text>
<text x="401.8" y="278" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >)</text>
<text x="418.7" y="278" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >feat(text-stats): середня довжина слова та час читання</text>
<text x="30.0" y="299" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="299" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="30.0" y="320" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="46.9" y="320" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >3be4931</text>
<text x="114.5" y="320" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >feat(password): виключення схожих символів (#15)</text>
<text x="30.0" y="341" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="341" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="30.0" y="362" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="362" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="63.8" y="362" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >8d437fe</text>
<text x="131.4" y="362" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >(</text>
<text x="139.8" y="362" fill="#ff7b72" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >origin/feature/password-ambiguous</text>
<text x="418.7" y="362" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >)</text>
<text x="435.6" y="362" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >feat(password): параметр exclude_ambiguous для схожих символів</text>
<text x="30.0" y="383" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="383" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="30.0" y="404" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="46.9" y="404" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >4c348d8</text>
<text x="114.5" y="404" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >feat(converter): одиниці об&#x27;єму (#14)</text>
<text x="30.0" y="425" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="425" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="30.0" y="446" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="446" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="63.8" y="446" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >3aaebfd</text>
<text x="131.4" y="446" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >(</text>
<text x="139.8" y="446" fill="#ff7b72" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >origin/feature/converter-volume</text>
<text x="401.8" y="446" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >)</text>
<text x="418.7" y="446" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >feat(converter): додати одиниці об&#x27;єму (ml, l, m3, gal)</text>
<text x="30.0" y="467" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="467" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="30.0" y="488" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="46.9" y="488" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >8a30b73</text>
<text x="114.5" y="488" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >docs: згадати текстове меню в описі проєкту (#13)</text>
<text x="30.0" y="509" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="509" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="30.0" y="530" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="530" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<rect x="57.8" y="515" width="916.2" height="21" rx="5" fill="#f7816622" stroke="#f78166" stroke-dasharray="3 3"/>
<text x="63.8" y="530" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >bf7fc48</text>
<text x="131.4" y="530" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >(</text>
<text x="139.8" y="530" fill="#ff7b72" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >origin/feature/readme-badge</text>
<text x="368.0" y="530" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >)</text>
<text x="384.9" y="530" fill="#f0f6fc" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="600" xml:space="preserve" >Merge branch &#x27;main&#x27; into feature/readme-badge: об&#x27;єднати правки опи…</text>
<text x="30.0" y="551" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="551" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="55.3" y="551" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="30.0" y="572" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="572" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="55.3" y="572" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="30.0" y="593" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="593" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="46.9" y="593" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="30.0" y="614" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="46.9" y="614" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="63.8" y="614" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >b81b74a</text>
<text x="131.4" y="614" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >docs: перелік утиліт в описі проєкту (#10)</text>
<text x="30.0" y="635" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="635" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="55.3" y="635" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="30.0" y="656" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="656" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="63.8" y="656" fill="#d2a8ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="80.7" y="656" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >dacb520</text>
<text x="148.3" y="656" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >(</text>
<text x="156.7" y="656" fill="#ff7b72" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >origin/feature/readme-intro</text>
<text x="384.9" y="656" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >)</text>
<text x="401.8" y="656" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >docs: list utilities in project description</text>
<text x="30.0" y="677" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="46.9" y="677" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="63.8" y="677" fill="#d2a8ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="80.7" y="677" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >af4f852</text>
<text x="148.3" y="677" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >feat(calculator): операція піднесення до степеня (#9)</text>
<text x="30.0" y="698" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="698" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="55.3" y="698" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="72.2" y="698" fill="#d2a8ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="30.0" y="719" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="719" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="63.8" y="719" fill="#d2a8ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="80.7" y="719" fill="#7ee787" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="97.6" y="719" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >42f139e</text>
<text x="165.2" y="719" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >(</text>
<text x="173.6" y="719" fill="#ff7b72" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >origin/feature/calculator-power</text>
<text x="435.6" y="719" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >)</text>
<text x="452.5" y="719" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >feat(calculator): add power operation</text>
<text x="30.0" y="740" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="740" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="55.3" y="740" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="72.2" y="740" fill="#d2a8ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="30.0" y="761" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="46.9" y="761" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="63.8" y="761" fill="#d2a8ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="80.7" y="761" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >2bf9da6</text>
<text x="148.3" y="761" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >test: додаткові тести граничних випадків (#5)</text>
<text x="30.0" y="782" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="782" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="55.3" y="782" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="72.2" y="782" fill="#d2a8ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >\</text>
<text x="30.0" y="803" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="803" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="55.3" y="803" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="72.2" y="803" fill="#d2a8ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="30.0" y="824" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="824" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="46.9" y="824" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="63.8" y="824" fill="#d2a8ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="30.0" y="845" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="845" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="63.8" y="845" fill="#d2a8ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="80.7" y="845" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >81363b1</text>
<text x="148.3" y="845" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >(</text>
<text x="156.7" y="845" fill="#ff7b72" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >origin/codex/edge-case-tests</text>
<text x="393.3" y="845" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >)</text>
<text x="410.2" y="845" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >test: cover utility edge cases and password character groups</text>
<text x="30.0" y="866" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="866" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="63.8" y="866" fill="#d2a8ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="80.7" y="866" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >553af46</text>
<text x="148.3" y="866" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >docs: згадати текстове меню в описі проєкту</text>
<text x="30.0" y="887" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="46.9" y="887" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="55.3" y="887" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="30.0" y="908" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="908" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="46.9" y="908" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="30.0" y="929" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="46.9" y="929" fill="#79c0ff" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="63.8" y="929" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >bb476ec</text>
<text x="131.4" y="929" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >(</text>
<text x="139.8" y="929" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >tag: v1.0.0</text>
<text x="232.8" y="929" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >)</text>
<text x="249.7" y="929" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >docs: record issues review status and verification results</text>
<text x="30.0" y="950" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >|</text>
<text x="38.5" y="950" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >/</text>
<text x="30.0" y="971" fill="#f78166" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >*</text>
<text x="46.9" y="971" fill="#e3b341" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >d278780</text>
<text x="114.5" y="971" fill="#c9d1d9" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >feat: import Python utilities and document verified lab status</text>
</svg>
<img width="960" height="258" alt="term-tests" src="https://github.com/user-attachments/assets/52e99823-d168-4857-bc66-c415177af4b6" />

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 258" width="960" height="258" role="img" aria-label="PowerShell — python-utils">
<defs><filter id="sh" x="-5%" y="-5%" width="110%" height="115%"><feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000" flood-opacity=".45"/></filter></defs>
<rect x="8" y="4" width="944" height="242" rx="14" fill="#0d1117" stroke="#30363d" filter="url(#sh)"/>
<path d="M8 18a14 14 0 0 1 14-14h916a14 14 0 0 1 14 14v22H8z" fill="#161b22"/>
<g transform="translate(8 4)"><circle cx="22" cy="22" r="6.5" fill="#ff5f57"/><circle cx="44" cy="22" r="6.5" fill="#febc2e"/><circle cx="66" cy="22" r="6.5" fill="#28c840"/></g>
<text x="480.0" y="30" fill="#8b949e" font-family="Inter, 'Segoe UI', system-ui, sans-serif" font-size="13" font-weight="500" xml:space="preserve" text-anchor="middle">PowerShell — python-utils</text>
<text x="30.0" y="82" fill="#7ee787" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="700" xml:space="preserve" >PS C:\python-utils&gt; </text><text x="199.0" y="82" fill="#e6edf3" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >python -m unittest discover</text>
<text x="30.0" y="112" fill="#7ee787" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >....................................</text>
<text x="30.0" y="136" fill="#6e7681" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >----------------------------------------------------------------------</text>
<text x="30.0" y="160" fill="#e6edf3" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" >Ran 36 tests in 0.083s</text>
<text x="30.0" y="184" fill="#6e7681" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="14" font-weight="400" xml:space="preserve" ></text>
<text x="30.0" y="208" fill="#3fb950" font-family="Consolas, Cascadia Code, 'Courier New', monospace" font-size="16" font-weight="700" xml:space="preserve" >OK</text><rect x="782" y="64" width="150" height="34" rx="17" fill="#0f2a1a" stroke="#238636"/><text x="857.0" y="86" fill="#3fb950" font-family="Inter, 'Segoe UI', system-ui, sans-serif" font-size="13" font-weight="700" xml:space="preserve" text-anchor="middle">36 тестів · OK</text>
</svg>
<img width="1200" height="760" alt="gh-release" src="https://github.com/user-attachments/assets/042a7ff3-e265-470e-b682-cbc679fa64a5" /> <img width="1000" height="470" alt="vscode-conflict" src="https://github.com/user-attachments/assets/02441773-9578-4cd5-94d3-dae20723a3b4" />


<img width="1680" height="1094" alt="image" src="https://github.com/user-attachments/assets/cadf5d0e-eb19-4b44-b973-f60972139536" />


## Реліз

Версію `1.1.0` описано в [CHANGELOG.md](../CHANGELOG.md); реліз
[v1.1.0](https://github.com/istdjfgh/python-utils/releases/tag/v1.1.0) створено з `main`
після злиття всіх функціональних змін. Попередній реліз — v1.0.0.

## Перевірка

```powershell
git clone https://github.com/istdjfgh/python-utils.git
cd python-utils
python -m unittest discover -v      # 36 тестів, усі проходять
python main.py
```

## Висновки

У ході лабораторної роботи було налаштовано середовище розробки (Git, Python, VS Code) та опрацьовано Feature Branch Workflow: кожне завдання оформлювалося як окремий Issue, окрема гілка та Pull Request із посиланням Closes #N.

Створено 9 Pull Request'ів (8 злито), функціональні зміни покрито 36 модульними тестами. Під час навчального конфлікту дві гілки змінили один і той самий рядок README; після злиття першої з них у другій виник конфлікт, який було вирішено вручну: git merge origin/main, вибір потрібних рядків, запуск тестів. Підготовлено реліз v1.1.0 з описом змін у CHANGELOG.

Найскладнішим було: Зробити це все, підготовити, у мене це зайняло 3 дні з допомогою ШІ.

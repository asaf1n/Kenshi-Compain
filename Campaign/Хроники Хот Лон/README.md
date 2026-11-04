# Хроники Хот Лон

Для этого прохождения в ChatGPT создаются **два проекта**: игровой (`prompts/project-instructions.md`) и летопись (`prompts/project-chronicle.md`). В игровом проекте одна сессия — один чат до `[итог]`; художественное расширение — только в литературном проекте. Межпроектная передача — закрытыми артефактами, не через память.

Документы прохождения по категориям. Какие категории подключает конкретный блокнот и как их обновляет, задаёт инструкция проекта в `prompts/`:

* Блокнот прохождения: **«Kenshi Compain. Hot Lon»** (`prompts/notebook-sessions.md`)

* Блокнот летописи: **«Kenshi Compain. Летопись Hot Lon»** (`prompts/notebook-chronicle.md`)

* База знаний об игре: **«Kenshi. Bible»** (`notebooks/4eade08a-af3f-49b9-9916-496e60a6234b`)

Структура хранения истории:

1. **Хронология** — `Kenshi_Канва.md` (краткий указатель: строка на главу, этап или сессию) и закрытая `archive/Kenshi_Хронология_дни_1-130.md`.

2. **Выгрузки сессий (артефакты хроники сессий)** — `archive/sessions/S-YYYYMMDD-n.md`: готовые артефакты из режима `[итог]`, содержащие дословные художественные вставки сессии и разбор по решениям `D-nnnn`.

3. **Расширенная повесть и произведения** — `archive/povest/`: полнообъёмная художественная книга, создаваемая поэтапно на основе хронологии, выгрузок сессий и Библии (с выгрузкой в Google Drive / внешние хранилища по необходимости).

## Выгрузка игры

Состояние игры от конвертера (`published/`, только чтение):

* Манифест: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/manifest.json

* Сводка: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/brief.md

* Состав отряда: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/squad.md

* Изменения: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/changes.json

* Скриншоты: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/screenshots/index.json — индекс `url_raw`/`sha256`; для визуального анализа открываются сами изображения.

## Рабочие документы

Текущее положение и действующие решения, целевая модель архетипов, билдов и ростеров, методика оценки:

* Текущая арка: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/Campaign/%D0%A5%D1%80%D0%BE%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%A5%D0%BE%D1%82%20%D0%9B%D0%BE%D0%BD/Kenshi_%D0%A2%D0%B5%D0%BA%D1%83%D1%89%D0%B0%D1%8F_%D0%B0%D1%80%D0%BA%D0%B0.md

* Архетипы и билды: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/Campaign/%D0%A5%D1%80%D0%BE%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%A5%D0%BE%D1%82%20%D0%9B%D0%BE%D0%BD/Kenshi_%D0%90%D1%80%D1%85%D0%B5%D1%82%D0%B8%D0%BF%D1%8B_%D0%B8_%D0%B1%D0%B8%D0%BB%D0%B4%D1%8B.md

* Методика: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/Campaign/%D0%A5%D1%80%D0%BE%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%A5%D0%BE%D1%82%20%D0%9B%D0%BE%D0%BD/Kenshi_%D0%9C%D0%B5%D1%82%D0%BE%D0%B4%D0%B8%D0%BA%D0%B0.md

## Хронология

Краткий указатель истории и закрытая хронология дней 1–130:

* Канва: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/Campaign/%D0%A5%D1%80%D0%BE%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%A5%D0%BE%D1%82%20%D0%9B%D0%BE%D0%BD/Kenshi_%D0%9A%D0%B0%D0%BD%D0%B2%D0%B0.md

* Хронология, дни 1–130: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/Campaign/%D0%A5%D1%80%D0%BE%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%A5%D0%BE%D1%82%20%D0%9B%D0%BE%D0%BD/archive/Kenshi_%D0%A5%D1%80%D0%BE%D0%BD%D0%BE%D0%BB%D0%BE%D0%B3%D0%B8%D1%8F_%D0%B4%D0%BD%D0%B8_1-130.md

## Выгрузки сессий

Готовые артефакты хроники каждой сессии (дословные художественные вставки сессии и разбор по решениям `D-nnnn`); файл сессии — `archive/sessions/S-YYYYMMDD-n.md`, список — в `Kenshi_Канва.md`:

* О выгрузках: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/Campaign/%D0%A5%D1%80%D0%BE%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%A5%D0%BE%D1%82%20%D0%9B%D0%BE%D0%BD/archive/sessions/README.md

## Персонажи и мир

Облик, голоса, отношения, фракции и стиль иллюстраций:

* Библия: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/Campaign/%D0%A5%D1%80%D0%BE%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%A5%D0%BE%D1%82%20%D0%9B%D0%BE%D0%BD/archive/Kenshi_%D0%91%D0%B8%D0%B1%D0%BB%D0%B8%D1%8F.md

## Повесть

Расширенная художественная повесть: матрица глав, правила расширения и базовый черновик:

* План и статусы: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/Campaign/%D0%A5%D1%80%D0%BE%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%A5%D0%BE%D1%82%20%D0%9B%D0%BE%D0%BD/archive/povest/README.md

* Черновик, дни 1–130: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/Campaign/%D0%A5%D1%80%D0%BE%D0%BD%D0%B8%D0%BA%D0%B8%20%D0%A5%D0%BE%D1%82%20%D0%9B%D0%BE%D0%BD/archive/povest/Kenshi_%D0%9F%D0%BE%D0%B2%D0%B5%D1%81%D1%82%D1%8C_%D0%B4%D0%BD%D0%B8_1-130.md

## Руководства и шаблоны

* Руководство компаньона: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/docs/companion-guide.md

* Руководство хрониста: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/docs/chronicler-guide.md

* Шаблон `[глава]`: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/templates/template-chapter.md

* Шаблон `[этап]` / `[экспедиция]`: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/templates/template-expedition.md

* Шаблон `[ход]`: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/templates/template-turn.md

* Шаблон `[прогресс]`: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/templates/template-progress.md

* Шаблон `[обсуждение]`: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/templates/template-discussion.md

* Шаблон `[сверка]`: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/templates/template-reconciliation.md

* Шаблон `[итог]`: https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/templates/template-session.md

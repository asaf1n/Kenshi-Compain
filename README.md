# Kenshi Compain — игровой компаньон и хроника кампании

Материалы для LLM: актуальное состояние игры, канон отдельных прохождений, режимы диалога и шаблоны ответов. Репозиторий читается по ссылкам GitHub: [https://github.com/asaf1n/Kenshi-Compain](https://github.com/asaf1n/Kenshi-Compain).

## Состояние игры (обновляется после каждой выгрузки)

| Что | Ссылка | Содержание |
|---|---|---|
| Манифест | [published/manifest.json](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/manifest.json) | игровое время, ветка, время выгрузки |
| Сводка | [published/brief.md](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/brief.md) | краткое положение дел для быстрого старта |
| Состав отряда | [published/squad.md](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/squad.md) | бойцы, снаряжение, характеристики |
| Изменения | [published/changes.json](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/changes.json) | что изменилось с предыдущего сохранения |
| Индекс шардов | [published/current/index.json](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/current/index.json) | бойцы, постройки, обзор мира: по одному файлу на вопрос |
| Расширенный снимок | [published/extended/current.json](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/extended/current.json) | полный очищенный срез; крупный файл, читать только выборочно |
| Локации | [published/locations.json](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/locations.json) | координаты и поселения |
| События | [published/timeline.jsonl](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/timeline.jsonl) | подтверждённые события |
| Справочник мира | [published/world_reference.json](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/world_reference.json) | география, фракции, зоны |

## Прохождения

Каждое прохождение лежит в своей подпапке [Campaign/](https://github.com/asaf1n/Kenshi-Compain/tree/main/Campaign): документы канона, журналы, инструкции блокнотов и ссылка на полную историю сессий описаны в `README.md` подпапки. Общие файлы репозитория от конкретного прохождения не зависят.

## Режимы диалога

Метка в начале запроса включает режим; структура ответа задана шаблоном. Общие правила компаньона: [docs/companion-guide.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/docs/companion-guide.md).

| Метка | Шаблон | Суть |
|---|---|---|
| `[итог]` | [template-session.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/templates/template-session.md) | завершение сессии: журнал, повествование, правки документов |
| `[хроника]` | [template-chronicle.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/templates/template-chronicle.md) | художественные сцены по реальным событиям сессии |
| `[прогресс]` | [template-progress.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/templates/template-progress.md) | боеспособность колонны и билды |
| `[экспедиция]` / `[этап]` | [template-expedition.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/templates/template-expedition.md) | регион, угрозы, логистика, маршруты |
| `[ход]` | [template-turn.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/templates/template-turn.md) | разбор последней сессии и диспозиция |
| `[обсуждение]` | [template-discussion.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/templates/template-discussion.md) | механики, моды, лор, стратегия |
| `[сверка]` | [template-reconciliation.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/templates/template-reconciliation.md) | актуализация документов кампании по новой выгрузке |
| `[глава]` | [template-chapter.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/templates/template-chapter.md) | закрытие сюжетной главы и открытие новой |

## Инструкции для LLM

Для работы достаточно LLM с доступом к этому репозиторию и одной из инструкций:

| Где применяется | Инструкция |
|---|---|
| Проект в чат-интерфейсе (ChatGPT и другие) | [prompts/project-instructions.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/prompts/project-instructions.md) |
| Блокнот (Google Notebook) | [prompts/notebook-instructions.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/prompts/notebook-instructions.md) |

Руководства, на которые ссылаются инструкции: [docs/companion-guide.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/docs/companion-guide.md) (роль, источники, режимы, подача) и [docs/chronicler-guide.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/docs/chronicler-guide.md) (художественные тексты). Блокнот читает только добавленные источники; их список для прохождения указан в `README.md` его подпапки.

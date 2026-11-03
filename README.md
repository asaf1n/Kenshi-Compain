# Kenshi Compain — игровой компаньон и хроника кампании

Материалы для LLM: актуальное состояние игры, канон отдельных прохождений, режимы диалога и шаблоны ответов. Репозиторий читается по ссылкам GitHub: [https://github.com/asaf1n/Kenshi-Compain](https://github.com/asaf1n/Kenshi-Compain).

## Состояние игры (обновляется после каждой выгрузки)

| Что | Ссылка | Содержание |
|---|---|---|
| Манифест | [published/manifest.json](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/manifest.json) | игровое время, ветка, время выгрузки |
| Сводка | [published/brief.md](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/brief.md) | краткое положение дел для быстрого старта |
| Состав отряда | [published/squad.md](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/squad.md) | бойцы, снаряжение, характеристики |
| Изменения | [published/changes.json](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/changes.json) | что изменилось с предыдущего сохранения |
| Полный снимок | [published/current.json](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/current.json) | отряд и мир целиком; крупный файл, читать выборочно |
| Локации | [published/locations.json](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/locations.json) | координаты и поселения |
| События | [published/timeline.jsonl](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/timeline.jsonl) | подтверждённые события |
| Справочник мира | [published/world_reference.json](https://raw.githubusercontent.com/asaf1n/Kenshi-Compain/main/published/world_reference.json) | география, фракции, зоны |

## Прохождения

Каждое прохождение лежит в своей подпапке [Campaign/](https://github.com/asaf1n/Kenshi-Compain/tree/main/Campaign): документы канона, журналы, инструкции блокнотов и ссылка на полную историю сессий описаны в `README.md` подпапки. Общие файлы репозитория от конкретного прохождения не зависят.

## Режимы диалога

Метка в начале запроса включает режим; структура ответа задана шаблоном. Общие правила компаньона: [prompts/01-COMPANION-SYSTEM.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/prompts/01-COMPANION-SYSTEM.md).

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

Для работы достаточно LLM с доступом к этому репозиторию и методологических инструкций:

| Где применяется | Инструкция |
|---|---|
| Профиль или проект | [00-PROFILE-INSTRUCTIONS.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/prompts/00-PROFILE-INSTRUCTIONS.md) |
| Полные правила | [01-COMPANION-SYSTEM.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/prompts/01-COMPANION-SYSTEM.md), [02-CHRONICLER-GUIDE.md](https://github.com/asaf1n/Kenshi-Compain/blob/main/prompts/02-CHRONICLER-GUIDE.md) |
| Блокноты | инструкции в подпапке прохождения |

Документы, на которые ссылаются таблицы, добавляются в блокнот или проект как источники по ссылкам GitHub.

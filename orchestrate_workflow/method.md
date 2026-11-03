# Привязка проекта Kenshi Compain к AI-Orchestrated-Workflow

Используется установленный комплект `asaf1n/AI-Orchestrated-Workflow`: `orchestrate`, `planner`, `implementer`, `reviewer`. Глобальные навыки и формы не копируются в проект. Работа ведётся по циклу: план → независимое ревью → исполнение → верификация.

## Предметные источники (SSOT)

| Назначение | Путь |
|---|---|
| Контракт репозитория | `AGENTS.md` |
| Шаблоны режимов взаимодействия (SSOT структуры) | `templates/` |
| Системное поведение компаньона | `prompts/01-COMPANION-SYSTEM.md` |
| Нормативная хронология и сессионный архив | `docs/CHRONOLOGY.md` |
| Данные снимков игрового мира (СТРОГО READ-ONLY) | `published/` |
| Авторские материалы кампаний | `Campaign/<кампания>/` |

## Пути оркестрации

| Назначение | Путь |
|---|---|
| План и очередь задач | `orchestrate_workflow/plans/<plan>/00_summary.md` |
| Спецификации задач | `orchestrate_workflow/plans/<plan>/<task>.md` |
| Локальная сессия исполнения | `orchestrate_workflow/<plan>/spec.md`, `result.md`, `review.md` |
| Заключение независимого ревью плана | `orchestrate_workflow/<plan>/review_plan.md` |

Каталог `plans/` версионируется в git. Рабочие сессии (`orchestrate_workflow/<plan>/`) исключаются через `.git/info/exclude`.

## Инварианты выполнения
1. `published/` — строго read-only.
2. `Campaign/<кампания>/` — редактирование только после явного согласования diff с игроком.
3. Кода утилит и тестов в `Kenshi Compain` нет; приёмка ведётся верификацией артефактов (`rg`, `wc -m`, чтение, независимое ревью).
4. Коммиты локальные с трейлером соавтора (`Co-Authored-By: <Agent> <email>`); `git push` — строго по прямой команде игрока.

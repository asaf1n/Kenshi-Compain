# Словарь колонок таблицы faction_relations.csv

- Назначение: Отношения фракций
- Ключ сортировки: faction_sid, kind, other_sid
- Ключи соединения: faction_sid, other_sid

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `faction_sid` | sid фракции-источника |
| `faction_name` | Название (ru или en) |
| `kind` | relation - `relations` (отношение к другой фракции); coexistence - `coexistence` (фракции, с которыми стремится сосуществовать); legal_system - `legal system` (чьи законы применяются) |
| `other_sid` | sid другой фракции |
| `other_name` | Название (ru или en) |
| `value` | Только для relation: отношение -100...100 как хранится; не указанные пары равны `default_relation` фракции (faction_hostility.csv); симметрия не предполагается |

[← К оглавлению таблиц](../index.md)

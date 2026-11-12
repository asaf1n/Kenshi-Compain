# Словарь колонок таблицы trade_modifiers.csv

- Назначение: Торговые коэффициенты
- Ключ сортировки: group, record_sid, field, ref_sid
- Ключи соединения: record_sid, ref_sid

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `group` | culture (ITEMS_CULTURE, тип 104), culture_link (TOWN/FACTION: trade culture, trade prices), squad_template (SQUAD_TEMPLATE, тип 52), manufacturer (WEAPON_MANUFACTURER, тип 51), constant (CONSTANTS, тип 27) |
| `record_sid` | sid записи |
| `record_type` | Тип записи |
| `record_name` | Имя записи (en) |
| `record_files` | Файлы, определяющие запись, в порядке загрузки |
| `field` | Поле записи или категория ссылки |
| `value` | Значение скалярного поля |
| `ref_sid` | sid записи, на которую указывает ссылка |
| `ref_name` | Её название (ru или en) |
| `ref_v0` | Значение ссылки `v[0]`: для `trade prices` множитель цены, 100 = 100% |
| `ref_v1` | Значение ссылки `v[1]` (смысл не установлен) |
| `ref_v2` | Значение ссылки `v[2]` (смысл не установлен) |

[← К оглавлению таблиц](../index.md)

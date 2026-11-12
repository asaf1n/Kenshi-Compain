# Словарь колонок таблицы squad_templates.csv

- Назначение: Шаблоны отрядов
- Ключ сортировки: sid
- Ключи соединения: sid

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `sid` | sid шаблона отряда (SQUAD_TEMPLATE, тип 52) |
| `name_en` | Имя записи (en) |
| `name_ru` | Имя записи (ru, gamedata.po) |
| `files` | Файлы, определяющие запись, в порядке загрузки |
| `faction_sids` | sid фракции отряда (`faction`); пусто - не задана |
| `faction_names` | Названия фракций |
| `world_state_sids` | sid World State (`world state`): отряд появляется, только когда условия выполнены (AND) |
| `world_state_required` | Требуемое значение `v[0]` по порядку world_state_sids: 1 - состояние истинно, 0 - ложно |
| `race_override_sids` | sid расы, принудительной для всего отряда (`race override`) |
| `race_override_names` | Названия рас |
| `roaming_military` | Считается бродячими войсками, даже если есть родной город |
| `patrol_approaches_towns` | Патруль заходит в ближние города |
| `dont_multiply` | Размер не зависит от множителя размера отрядов в настройках |
| `regenerates` | Отряд-житель медленно восстанавливает потери |
| `is_trader` | Торговый отряд |
| `num_random_chars` | Минимум персонажей, выбираемых из `choosefrom list` |
| `num_random_chars_max` | Максимум персонажей, выбираемых из `choosefrom list` |

[← К оглавлению таблиц](../index.md)

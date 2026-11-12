# Словарь колонок таблицы squad_spawns.csv

- Назначение: Спавны отрядов
- Ключ сортировки: source, place_sid, squad_sid
- Ключи соединения: place_sid, squad_sid

## Нормативные примечания

- Не публикуется: привязка групп биомов к зонам карты (в записях игры её нет).

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `source` | biome_homeless - `homeless spawns` группы биомов (BIOME_GROUP); town_roaming - `roaming squads` города (TOWN) |
| `place_sid` | sid группы биомов или города |
| `place_name_en` | Название (en) |
| `place_name_ru` | Название (ru, gamedata.po) |
| `place_faction_sid` | sid фракции города (`faction`); для биомов пусто |
| `spawn_amount` | `homeless spawn amount` биома: примерное число бездомных отрядов на зону; для городов пусто |
| `squad_sid` | sid шаблона отряда (squad_templates.csv) |
| `squad_name` | Название отряда (ru или en) |
| `ref_v0` | Значение ссылки `v[0]`: у biome_homeless - относительный шанс появления; у town_roaming смысл не задан |

[← К оглавлению таблиц](../index.md)

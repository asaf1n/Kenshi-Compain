# Словарь колонок таблицы location_garrisons.csv

- Назначение: Гарнизоны и постоянные обитатели объектов мира
- Ключ сортировки: instance_id, squad_name, squad_sid
- Ключи соединения: instance_id, template_sid, squad_sid, faction_sid

## Нормативные примечания

- Гарнизоны и постоянные обитатели фиксированных объектов (лаборатории, арсеналы, базы, башни, города).
- Для объектов без заданных резидентов в данных игры строки не создаются.
- Боевые параметры лидера и рядовых рассчитываются аналогично region_encounters.csv.

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `instance_id` | ID физического объекта на карте мира |
| `location_name_en` | Название объекта (en) |
| `location_name_ru` | Название объекта (ru) |
| `template_sid` | sid шаблона объекта (TOWN) |
| `kind` | Тип объекта |
| `region_name_en` | Регион расположения (en) |
| `region_name_ru` | Регион расположения (ru) |
| `squad_sid` | sid шаблона отряда |
| `squad_name` | Название отряда |
| `faction_sid` | sid фракции отряда |
| `faction_name` | Название фракции |
| `spawn_share` | Доля среди гарнизонов объекта, % |
| `squad_size_min` | Минимальный размер отряда |
| `squad_size_max` | Максимальный размер отряда |
| `members_summary` | Краткий состав отряда |
| `leader_template_name` | Имя шаблона лидера |
| `leader_attack` | Атака лидера |
| `leader_defence` | Защита лидера |
| `leader_strength` | Сила лидера |
| `leader_toughness` | Стойкость лидера |
| `leader_stats_randomise` | Разброс характеристик лидера (+/-) |
| `leader_weapon` | Оружие лидера |
| `leader_armour` | Броня лидера |
| `members_attack_min` | Мин. атака рядовых |
| `members_attack_median` | Медианная атака рядовых |
| `members_attack_max` | Макс. атака рядовых |
| `members_defence_min` | Мин. защита рядовых |
| `members_defence_median` | Медианная защита рядовых |
| `members_defence_max` | Макс. защита рядовых |
| `members_strength_min` | Мин. сила рядовых |
| `members_strength_median` | Медианная сила рядовых |
| `members_strength_max` | Макс. сила рядовых |
| `members_toughness_min` | Мин. стойкость рядовых |
| `members_toughness_median` | Медианная стойкость рядовых |
| `members_toughness_max` | Макс. стойкость рядовых |
| `members_stats_randomise` | Разброс характеристик рядовых (+/-) |
| `weapons_typical` | Типичное оружие рядовых |
| `armour_grade_max` | Макс. грейд брони в отряде |
| `world_state_conditions` | Условия World State |

[← К оглавлению таблиц](../index.md)

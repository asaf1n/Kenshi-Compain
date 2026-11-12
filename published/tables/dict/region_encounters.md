# Словарь колонок таблицы region_encounters.csv

- Назначение: Плоская аналитическая витрина встреч и бродячих отрядов по регионам и городам
- Ключ сортировки: region_name_en, source, squad_name, squad_sid
- Ключи соединения: region_name_en, squad_sid, faction_sid

## Нормативные примечания

- Боевые навыки юнитов вычисляются по stat_attack или combat_stats (для животных — animal_strength).
- Для рядовых участников отряда рассчитываются members_combat_min, members_combat_median и members_combat_max; при их отсутствии значения наследуются от лидера.
- Оружие и броня лидера фиксируют экипировку и грейд шаблона лидера; weapons_typical перечисляет типичное оружие рядовых.
- Ключ соединения region_name_en связывает витрину с локациями справочника мира и просмотрщиком карты.

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `region_name_en` | Регион/биом (en) |
| `region_name_ru` | Регион/биом (ru) |
| `place_sid` | sid биом-группы или города |
| `source` | Источник появления (biome_homeless или town_roaming) |
| `town_name` | Название города (для town_roaming) |
| `squad_sid` | sid шаблона отряда |
| `squad_name` | Название отряда |
| `faction_sid` | sid фракции отряда |
| `faction_name` | Название фракции |
| `spawn_share` | Доля появления в регионе/городе, % |
| `squad_size_min` | Минимальный размер отряда |
| `squad_size_max` | Максимальный размер отряда |
| `members_summary` | Краткий состав отряда |
| `leader_template_name` | Имя шаблона лидера |
| `leader_combat_skill` | Боевой навык лидера |
| `leader_weapon` | Оружие лидера |
| `leader_armour` | Броня лидера |
| `members_combat_min` | Мин. боевой навык рядовых |
| `members_combat_median` | Медианный боевой навык рядовых |
| `members_combat_max` | Макс. боевой навык рядовых |
| `weapons_typical` | Типичное оружие рядовых |
| `armour_grade_max` | Макс. грейд брони в отряде |
| `world_state_conditions` | Условия World State |

[← К оглавлению таблиц](../index.md)

# Словарь колонок таблицы region_encounters.csv

- Назначение: Плоская аналитическая витрина встреч и бродячих отрядов по регионам и городам
- Ключ сортировки: region_name_en, source, squad_name, squad_sid
- Ключи соединения: region_name_en, squad_sid, faction_sid

## Нормативные примечания

- Боевые параметры юнитов (атака, защита, сила, стойкость) вычисляются по stat_*, combat_stats или strength (для животных — animal_strength).
- Для рядовых участников отряда рассчитываются min, median и max по характеристикам и диапазон stats_randomise; при их отсутствии значения наследуются от лидера.
- Оружие и броня лидера фиксируют экипировку и грейд шаблона лидера; weapons_typical перечисляет типичное оружие рядовых с грейдом/производителем.
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

# Табличные выгрузки

- snapshot_id: `sha256-cc78830ed3255c2338228a0e4c3632c15c2a7a87c47f64da56966f126249a324`
- Игровое время: День 136, 20:21
- Формат: CSV, UTF-8, LF, RFC 4180.
- Пустая ячейка — пусто; числа с точкой; булевы `true`/`false`; списки через `; `.
- Справочник игры: base, Newwworld, Dialogue, rebirth, Russian Dark UI simplistic, Martial Arts Fast Dodger, Better Map RUS and Zones

## Таблицы

| Файл | Строк | Ключ сортировки | Ключи соединения | Словарь | Содержание |
|---|---|---|---|---|---|
| `squad.csv` | 30 | character_id | character_id, squad_id | [словарь](dict/squad.md) | Состав отряда, статы, здоровье |
| `equipment.csv` | 252 | location_kind, character_id, kind, slot, sid, level, quality | character_id, sid, building_id | [словарь](dict/equipment.md) | Снаряжение, оружие, броня |
| `inventory.csv` | 456 | character_id, container, slot, base_sid, level, dup_no | character_id, base_sid, item_sid | [словарь](dict/inventory.md) | Инвентарь персонажей |
| `storage.csv` | 224 | location_key, zone, building_id, container, item, item_sid | building_id, item_sid | [словарь](dict/storage.md) | Склады поселений |
| `buildings.csv` | 176 | location_key, zone, parent_instance_id, instance_id | instance_id, parent_instance_id, template_sid | [словарь](dict/buildings.md) | Постройки, крафт, станки |
| `research.csv` | 181 | category, level, sid | sid | [словарь](dict/research.md) | Технологии и рецепты |
| `build_catalog.csv` | 229 | building_category, sid | sid, upgrades_to | [словарь](dict/build_catalog.md) | Каталог построек, сметы |
| `biome_resources.csv` | 74 | biome_sid | biome_sid | [словарь](dict/biome_resources.md) | Ресурсы и климат регионов |
| `item_prices.csv` | 594 | sid | sid | [словарь](dict/item_prices.md) | Базовые цены предметов |
| `trade_modifiers.csv` | 1533 | group, record_sid, field, ref_sid | record_sid, ref_sid | [словарь](dict/trade_modifiers.md) | Торговые коэффициенты |
| `unique_npcs.csv` | 78 | sid | sid | [словарь](dict/unique_npcs.md) | Уникальные NPC |
| `unique_entities.csv` | 262 | sid | sid, primary_location_instance_id, character_id | [словарь](dict/unique_entities.md) | Реестр NPC и Мейто |
| `town_overrides.csv` | 9 | replacement_sid, town | replacement_sid, faction_sid | [словарь](dict/town_overrides.md) | Замены городов |
| `diplomacy.csv` | 103 | faction_sid | faction_sid | [словарь](dict/diplomacy.md) | Отношения фракций |
| `world_reactions.csv` | 310 | town_sid, override_sid, world_state_sid, condition, subject_sid | override_sid, town_sid, world_state_sid, subject_sid, faction_sid | [словарь](dict/world_reactions.md) | Переходы городов |
| `world_reaction_links.csv` | 308 | town_sid, override_sid, world_state_sid, condition, npc_sid | override_sid, town_sid, world_state_sid, npc_sid | [словарь](dict/world_reaction_links.md) | Условия и статус NPC |
| `unit_templates.csv` | 682 | sid | sid | [словарь](dict/unit_templates.md) | Шаблоны персонажей |
| `unit_template_gear.csv` | 5822 | template_sid, category, ref_sid | template_sid, ref_sid | [словарь](dict/unit_template_gear.md) | Экипировка шаблонов |
| `squad_templates.csv` | 959 | sid | sid | [словарь](dict/squad_templates.md) | Шаблоны отрядов |
| `squad_members.csv` | 2131 | squad_sid, role, member_sid | squad_sid, member_sid | [словарь](dict/squad_members.md) | Состав отрядов |
| `squad_spawns.csv` | 713 | source, place_sid, squad_sid | place_sid, squad_sid | [словарь](dict/squad_spawns.md) | Спавны отрядов |
| `faction_relations.csv` | 317 | faction_sid, kind, other_sid | faction_sid, other_sid | [словарь](dict/faction_relations.md) | Отношения фракций |
| `faction_hostility.csv` | 103 | faction_sid | faction_sid | [словарь](dict/faction_hostility.md) | Враждебность фракций |
| `races.csv` | 53 | sid | sid | [словарь](dict/races.md) | Расы, защита от погоды |

## Общие правила и ограничения

- Словари колонок и примечания: `dict/<таблица>.md`.
- Связи между таблицами — по `sid` и `id`.
- Ссылки `world state`/`NPC is`: `v[1]`, `v[2]` публикуются без трактовки.
- Шаблоны юнитов публикуются как в данных модов, без рандомизации.
- Цены в городах не вычисляются (множители не сверены).

## Недоступные и неопубликованные поля


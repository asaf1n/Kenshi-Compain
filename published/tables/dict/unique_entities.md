# Словарь колонок таблицы unique_entities.csv

- Назначение: Реестр NPC и Мейто
- Ключ сортировки: sid
- Ключи соединения: sid, primary_location_instance_id, character_id

## Нормативные примечания

- Коды `state_code`: 0 (мертв), 1 (жив и свободен), 2 (в плену) (fcs.def, WORLD_EVENT_STATE, поле `NPC is`).
- Статус зачистки `location_cleared`: `true`, `false`, пусто (без локации / неоднозначно).
- Статус происхождения `provenance_status`: `confirmed_trophy`, `unconfirmed`, пусто (не определен).
- Статус наблюдения `observation_status`: `observed`, `not_observed`.

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `entity_kind` | Вид сущности: npc, meitou |
| `category` | Категория сущности: recruit, world_leader, boss, significant_npc, unique_npc, meitou |
| `sid` | sid шаблона (npc_sid для персонажей и боссов, base_sid для оружия Мейто) |
| `name_ru` | Имя/название на русском языке |
| `name_en` | Имя/название на английском языке |
| `state_code` | Код состояния: 0 мёртв, 1 жив и свободен, 2 в плену |
| `squad_status` | Статус в отряде игрока: confirmed_in_squad, confirmed_not_in_squad, unresolved |
| `character_id` | Идентификатор персонажа игрока, если принят в отряд |
| `primary_location_instance_id` | Идентификатор основной локации (поселения/города) |
| `location_resolution` | Точность привязки к локации: unique, ambiguous, unresolved |
| `carrier_or_storage` | Носитель или хранилище экземпляра (вид:имя) |
| `observation_status` | Статус наблюдения в сохранении: observed или not_observed |
| `provenance_status` | Статус происхождения: confirmed_trophy или unconfirmed |
| `location_cleared` | Место персонажа отмечено зачищенным: true, false |
| `outcome` | Исход взаимодействия из ручного слоя или персонального свидетельства |
| `evidence` | Текст подтверждения/свидетельства исхода |
| `game_time` | Игровое время подтверждения события |

[← К оглавлению таблиц](../index.md)

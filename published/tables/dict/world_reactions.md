# Словарь колонок таблицы world_reactions.csv

- Назначение: Переходы городов
- Ключ сортировки: town_sid, override_sid, world_state_sid, condition, subject_sid
- Ключи соединения: override_sid, town_sid, world_state_sid, subject_sid, faction_sid

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `override_sid` | sid записи override города |
| `variant` | Название варианта (запись override, en) |
| `town_sid` | sid города-родителя (TOWN с `override town`) |
| `town_name` | Название города (en) |
| `town_name_ru` | Название города (ru) |
| `world_state_sid` | sid записи World State, на которую ссылается override |
| `world_state_name` | Название World State |
| `world_state_v0` | Значение ссылки `world state` у override: по fcs.def 1 - состояние истинно, 0 - ложно; условия через AND |
| `condition` | Вид условия в World State: NPC is, NPC is NOT, player ally, player enemy; пусто - условий нет |
| `subject_sid` | sid NPC или фракции в условии |
| `subject_name` | Название субъекта (ru или en) |
| `subject_v0` | Для `NPC is`/`NPC is NOT` - код состояния NPC (0/1/2, см. unique_npcs.csv) |
| `subject_v1` | `v[1]` ссылки (смысл не установлен) |
| `subject_v2` | `v[2]` ссылки (смысл не установлен) |
| `faction_sid` | sid итоговой фракции override (`faction`) |
| `faction_name` | Название фракции |

[← К оглавлению таблиц](../index.md)

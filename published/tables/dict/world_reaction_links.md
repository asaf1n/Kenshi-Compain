# Словарь колонок таблицы world_reaction_links.csv

- Назначение: Условия и статус NPC
- Ключ сортировки: town_sid, override_sid, world_state_sid, condition, npc_sid
- Ключи соединения: override_sid, town_sid, world_state_sid, npc_sid

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `override_sid` | sid записи override |
| `town_sid` | sid города-родителя |
| `world_state_sid` | sid World State |
| `condition` | NPC is или NPC is NOT |
| `npc_sid` | sid уникального NPC |
| `npc_name` | Название NPC |
| `required_state_code` | Код состояния в условии (`v[0]` ссылки) |
| `npc_in_save` | NPC присутствует среди usedUniques сохранения |
| `current_state_code` | Текущий state_code из сохранения |
| `current_player` | NPC в отряде игрока |
| `current_captured_by` | Кто несёт пленного |

[← К оглавлению таблиц](../index.md)

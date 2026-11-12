# Словарь колонок таблицы unit_templates.csv

- Назначение: Шаблоны персонажей
- Ключ сортировки: sid
- Ключи соединения: sid

## Нормативные примечания

- Не публикуется: имена кодов `NPC class`, `armour grade`, `fundamental type`, `slave` (перечисления не заданы в данных).

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `sid` | sid шаблона (CHARACTER или ANIMAL_CHARACTER) |
| `kind` | character или animal |
| `name_en` | Имя записи (en) |
| `name_ru` | Имя записи (ru, gamedata.po) |
| `files` | Файлы, определяющие запись, в порядке загрузки |
| `faction_sids` | sid фракции шаблона (`faction`); пусто - не задана (фракцию задаёт отряд, см. squad_templates.csv) |
| `faction_names` | Названия фракций |
| `race_sids` | sid рас (`race`), через `; ` |
| `race_names` | Названия рас |
| `race_weights` | Шанс расы `v[0]`, % (по порядку race_sids) |
| `female_chance` | Шанс женского пола, % (0-100) |
| `unique` | Персонаж появляется один раз |
| `named` | Имя выбирается случайно из списка имён |
| `shaved` | Бритая голова (как у рабов) |
| `wears_uniform` | Одежда помечена как форма фракции |
| `is_trader` | Торговец |
| `slave` | Начальное состояние раба, код `slave` как хранится (0 - не раб) |
| `npc_class` | Класс NPC, код `NPC class` как хранится (перечисление CharacterTypeEnum, имена в данных не заданы) |
| `armour_grade` | Качество брони, код `armour grade` как хранится (перечисление ArmourRarity, имена в данных не заданы) |
| `armour_upgrade_chance` | Шанс брони на уровень выше обычного, % (0-100) |
| `stats_randomise` | Случайный разброс характеристик: +/- это число к значениям шаблона |
| `combat_stats` | `combat stats`: боевые навыки, если запись STATS не задана (0 - не задано) |
| `ranged_stats` | `ranged stats`: навыки дальнего боя, если запись STATS не задана |
| `stealth_stats` | `stealth stats`: навыки скрытности, если запись STATS не задана |
| `strength` | `strength`: сила, если запись STATS не задана |
| `unarmed_stats` | `unarmed stats`: боевые искусства и уворот, если запись STATS не задана |
| `animal_strength` | Фиксированная сила животного (`animal strength`) |
| `money_min` | Минимум денег |
| `money_max` | Максимум денег |
| `wages` | Дневное жалованье |
| `bounty_chance` | Шанс награды за голову, % |
| `bounty_amount` | Сумма награды |
| `bounty_amount_fuzz` | Разброс суммы награды +/- |
| `stats_sid` | sid записи STATS шаблона; пусто - не задана; stat_* заполнены, только если ссылка одна |
| `stat_dexterity` | Запись STATS, `dexterity`: Ловкость [0-100] |
| `stat_strength` | Запись STATS, `strength`: Сила [0-100] |
| `stat_toughness2` | Запись STATS, `toughness2`: Крепость [0-100] |
| `stat_perception` | Запись STATS, `perception`: Восприятие [0-100] |
| `stat_attack` | Запись STATS, `attack`: Атака (ближний бой) [0-100] |
| `stat_defence` | Запись STATS, `defence`: Защита (ближний бой) [0-100] |
| `stat_dodge` | Запись STATS, `dodge`: Уворот [0-100] |
| `stat_unarmed` | Запись STATS, `unarmed`: Боевые искусства [0-100] |
| `stat_athletics` | Запись STATS, `athletics`: Атлетика [0-100] |
| `stat_swimming` | Запись STATS, `swimming`: Плавание [0-100] |
| `stat_engineer` | Запись STATS, `engineer`: Инженерия [0-100] |
| `stat_medic` | Запись STATS, `medic`: Полевой медик [0-100] |
| `stat_robotics` | Запись STATS, `robotics`: Роботехника [0-100] |
| `stat_science` | Запись STATS, `science`: Наука [0-100] |
| `stat_assassin` | Запись STATS, `assassin`: Убийство [0-100] |
| `stat_lockpicking` | Запись STATS, `lockpicking`: Взлом [0-100] |
| `stat_stealth` | Запись STATS, `stealth`: Скрытность [0-100] |
| `stat_thievery` | Запись STATS, `thievery`: Воровство [0-100] |
| `stat_armour_smith` | Запись STATS, `armour smith`: Ковка доспехов [0-100] |
| `stat_bow_smith` | Запись STATS, `bow smith`: Ковка арбалетов [0-100] |
| `stat_cooking` | Запись STATS, `cooking`: Готовка [0-100] |
| `stat_farming` | Запись STATS, `farming`: Фермерство [0-100] |
| `stat_labouring` | Запись STATS, `labouring`: Работа [0-100] |
| `stat_weapon_smith` | Запись STATS, `weapon smith`: Ковка оружия [0-100] |
| `stat_blunt` | Запись STATS, `blunt`: Дробящее [0-100] |
| `stat_bow` | Запись STATS, `bow`: Арбалеты [0-100] |
| `stat_ff` | Запись STATS, `ff`: Точная стрельба [0-100] |
| `stat_hackers` | Запись STATS, `hackers`: Рубачи [0-100] |
| `stat_heavy_weapons` | Запись STATS, `heavy weapons`: Тяжелое оружие [0-100] |
| `stat_katana` | Запись STATS, `katana`: Катаны [0-100] |
| `stat_poles` | Запись STATS, `poles`: Древковое [0-100] |
| `stat_sabres` | Запись STATS, `sabres`: Сабли [0-100] |
| `stat_turrets` | Запись STATS, `turrets`: Турели [0-100] |

[← К оглавлению таблиц](../index.md)

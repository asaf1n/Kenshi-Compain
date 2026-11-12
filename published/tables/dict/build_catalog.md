# Словарь колонок таблицы build_catalog.csv

- Назначение: Каталог построек, сметы
- Ключ сортировки: building_category, sid
- Ключи соединения: sid, upgrades_to

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `sid` | sid записи BUILDING (тип 0) |
| `name_en` | Название постройки (en) |
| `name_ru` | Название постройки (ru) |
| `building_category` | Категория в меню строительства (`building category`) |
| `is_interior` | true - устанавливается только внутри зданий (`is interior furniture`); false - наружная постройка |
| `is_node` | true - природный ресурсный узел (`is node`) |
| `unlock_status` | Статус доступности игроку: unlocked (открыта и доступна к постройке), in_queue (технология в очереди), locked (технология не изучена), world_or_town (городское здание или природная жила) |
| `unlocked_by` | Открывающие технологии из RESEARCH (`enable buildings`) |
| `built_complete_count` | Количество уже достроенных экземпляров у игрока в текущем сохранении |
| `built_incomplete_count` | Количество заложенных (недостроенных) экземпляров у игрока |
| `construction_materials` | Точная смета постройки 1 единицы (`refs:construction` либо стандартные Стройматериалы по `build materials`), через `; ` |
| `build_materials_total` | Поле `build materials` шаблона |
| `build_speed_mult` | Множитель времени строительства (`build speed mult`) |
| `build_hours` | Базовое время строительства, ч (`build materials * build speed mult`) |
| `power_output` | Выработка (>0) или потребление (<0) энергии (`power output`) |
| `power_capacity` | Ёмкость хранения энергии в секундах (`power capacity`) |
| `max_operators` | Максимальное число операторов (`max operators`) |
| `output_rate` | Базовая скорость/выход (`output rate`) |
| `production_mult` | Множитель скорости производства или расхода топлива (`production mult` из BUILDING_FUNCTIONALITY) |
| `function_code` | Код функции `function` из BUILDING_FUNCTIONALITY (BuildingFunction) |
| `stat_used_code` | Код используемого навыка `stat used` из BUILDING_FUNCTIONALITY (StatsEnumerated) |
| `world_resource_mining` | Код подземного ресурса `world resource mining` (0 - нет, 1+ - вода/плодородие/руда/камень/топливо) |
| `consumes` | Потребляемое сырьё (`refs:consumes` или расход воды фермы) |
| `produces` | Производимый ресурс для автоматических/добывающих построек (`refs:produces`) |
| `crafts_count` | Число доступных рецептов крафта на станке (`* crafts`) |
| `farm_profile` | Параметры ферм из FARM_DATA: климат (`arid/green/swamp`), `min_fert`, `growth`, `plants` |
| `upgrades_to` | Следующая ступень улучшения (`refs:upgrades to`) |

[← К оглавлению таблиц](../index.md)

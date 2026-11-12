# Словарь колонок таблицы research.csv

- Назначение: Технологии и рецепты
- Ключ сортировки: category, level, sid
- Ключи соединения: sid

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `sid` | sid записи RESEARCH (тип 21) |
| `name_en` | Название технологии (en) |
| `name_ru` | Название технологии (ru) |
| `category` | Технологическая ветка (`category`: Core, Farming, Mining, Power, Defence, Smithing, Robotics...) |
| `status` | Статус у игрока: completed (изучена), in_progress (изучается сейчас), queued (в очереди стенда), available (доступна к изучению), locked_prereq (не выполнены requirements), locked_tech_level (нужен стенд выше текущего tech_level), locked_blueprint (нужен чертёж) |
| `level` | Требуемый уровень научного стенда (`level`) |
| `tech_level_upgrade` | true - повышает технологический уровень (`is level upgrade`) |
| `blueprint_only` | true - открывается только применением чертежа (`blueprint only`) |
| `paid` | true - ресурсы за исследование уже вложены в стенд (`paid#`) |
| `progress_raw` | Сырой прогресс изучения из сохранения (`current_progress`) |
| `completed_level` | Изученный уровень (0 - не изучена; 1..max_repeats для многократных исследований) |
| `max_repeats` | Максимальное число уровней изучения (`repeats`; 1 для однократных) |
| `time_hours` | Базовое время изучения, ч (`time`) |
| `money_cost` | Денежная стоимость, кат. (`money`) |
| `cost_items` | Предметы, расходуемые на изучение (`refs:cost`: `предмет: количество`), через `; ` |
| `requirements` | Предшествующие технологии (`refs:requirements`), через `; ` |
| `missing_requirements` | Неизученные предшествующие технологии из `requirements`, блокирующие запуск |
| `enable_buildings` | Открываемые постройки и станки (`refs:enable buildings`), через `; ` |
| `improve_buildings` | Улучшаемые постройки (`refs:improve buildings`), через `; ` |
| `building_improvements` | Бонусы улучшения построек (`power increase`, `power capacity increase`, `production mult`) |
| `enable_crafts_count` | Число открываемых рецептов крафта предметов, оружия, брони, арбалетов, рюкзаков и протезов |

[← К оглавлению таблиц](../index.md)

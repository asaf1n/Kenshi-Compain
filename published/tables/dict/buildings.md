# Словарь колонок таблицы buildings.csv

- Назначение: Постройки, крафт, станки
- Ключ сортировки: location_key, zone, parent_instance_id, instance_id
- Ключи соединения: instance_id, parent_instance_id, template_sid

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `settlement` | Поселение; пусто, если не определено |
| `location_key` | Ключ места: поселение или «зона N (поселение не определено)» |
| `settlement_status` | Способ привязки: in_location, town, near_location, zone_location, zone |
| `zone` | Зона карты |
| `instance_id` | ID экземпляра постройки или жилы в сохранении |
| `parent_instance_id` | ID родительского здания для интерьерного объекта; пусто у верхнего уровня |
| `parent_name` | Название родительского здания |
| `name` | Название постройки/станка/жилы (ru) |
| `template_sid` | sid шаблона BUILDING в данных игры |
| `category` | Категория постройки (`building category`: Production, Research, Crafting, Power, Storage, Mining, Training, Turret...) |
| `is_interior` | true - объект внутри здания (`interior`); false - верхний уровень |
| `floor` | Этаж внутри здания (`floornum`) |
| `complete` | true - постройка завершена; false - недострой |
| `destroyed` | true - разрушена |
| `broken` | true - сломана (`broken`) |
| `construction_progress_raw` | Сырой прогресс постройки из сохранения |
| `construction_materials` | Смета и фактически вложенные материалы по слотам (`Материал: вложено/требуется`), через `; ` |
| `power_on` | Питание включено (`power on`) |
| `gets_battery` | Подключено к сети/аккумуляторам (`gets battery`) |
| `battery_charge` | Текущий заряд аккумулятора в сейве (`batterycharge`) |
| `tpl_power_output` | Паспортная выработка (>0) или потребление (<0) энергии из шаблона BUILDING (`power output`) |
| `tpl_power_capacity` | Паспортная ёмкость аккумулятора из шаблона BUILDING (`power capacity`) |
| `is_paused` | Работа приостановлена (`pause`) |
| `is_repeat` | Включён повтор очереди крафта (`repeat`) |
| `production_progress` | Сырой прогресс цикла производства (`production amount`) |
| `resource_mult` | Качество ресурсной жилы (`resource mult`, 0..1 для MINING) |
| `mining_resource_level` | Уровень ресурса разработки (`mining resource level`) |
| `active_craft` | Активная очередь крафта станка `предмет (прогресс%)` из `current0..N`, через `; ` |
| `partial_ingredients` | Вложенные в станок незавершённые ингредиенты `предмет: количество` из `craft partial item`, через `; ` |
| `stored_items_count` | Суммарное количество предметов во внутреннем контейнере объекта; подробно - storage.csv |
| `assigned_workers` | Назначенные на этот объект работники отряда `Имя (ЗАДАЧА)` по совпадению target_handle |
| `upgrades_to` | Следующая ступень улучшения постройки из шаблона BUILDING (`upgrades to`) |

[← К оглавлению таблиц](../index.md)

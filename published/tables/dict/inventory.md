# Словарь колонок таблицы inventory.csv

- Назначение: Инвентарь персонажей
- Ключ сортировки: character_id, container, slot, base_sid, level, dup_no
- Ключи соединения: character_id, base_sid, item_sid

## Нормативные примечания

- Предметы персонажей поэкземплярно (контейнеры body, belt, backpack, inventory; ключ сравнения снимков (character_id, base_sid, level, slot, dup_no), `item_sid` действует внутри снимка).
- Вес экземпляров и параметры рюкзаков в таблицы не входят.

## Колонки

| Колонка | Описание / Тип |
|---|---|
| `character_id` | ID персонажа |
| `character_name` | Имя персонажа |
| `container` | body - надето (оружие, броня, надетый рюкзак); belt - пояс; backpack - внутри рюкзака; inventory - основной инвентарь; unknown - раздел не распознан (значение в `slot`) |
| `slot` | weapon_back, weapon_hip, head, shirt, body, legs, boots, backpack (надетый рюкзак), belt; main - основной инвентарь; backpack_content - содержимое рюкзака |
| `backpack_name` | Для container = backpack: название рюкзака, в котором лежит предмет |
| `backpack_sid` | Для container = backpack: base_sid рюкзака |
| `item_name` | Название предмета (игра, ru); пусто, если sid нет в данных игры |
| `item_type` | Тип записи: ITEM, WEAPON, CROSSBOW, ARMOUR, CONTAINER, LIMB_REPLACEMENT... |
| `base_sid` | sid записи предмета в данных игры; стабилен между сейвами |
| `item_sid` | sid экземпляра в сейве; уникален только внутри снимка, между сейвами меняется - для сравнения снимков не использовать |
| `level` | Уровень экземпляра как в сейве (у расходников 0) |
| `quality` | quality экземпляра как в сейве (у брони и оружия 100, у прочих 1; смысл у расходников не установлен) |
| `grade` | Грейд: оружие - запись material, броня и арбалет - по уровню, протез - по уровню; пусто - не определён |
| `quantity` | Количество в стопке |
| `stolen` | true - предмет краденый; пусто - нет |
| `charges` | charges как в сейве (для еды - питательность на единицу) |
| `unique` | Признак unique из сейва |
| `unresolved` | true - base_sid не найден в данных игры |
| `dup_no` | Порядковый номер среди экземпляров с одинаковым (character_id, base_sid, level, slot): ключ сравнения снимков - (character_id, base_sid, level, slot, dup_no) |

[← К оглавлению таблиц](../index.md)

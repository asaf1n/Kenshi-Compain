# Табличные выгрузки

- snapshot_id: `sha256-487bd5b4d5f7853272408524e5158bc529891aba81299445ead568d09f8ed121`
- Игровое время: День 134, 20:46
- Формат: CSV, UTF-8 без BOM, LF, RFC 4180, разделитель - запятая; первая строка - заголовок.
- Пустая ячейка - значение отсутствует или не применимо; числа с точкой без разделителей разрядов, булевы `true`/`false`; списки в ячейке разделены `; `.
- Строки отсортированы по ключу; меток времени в таблицах нет; связи между таблицами - по идентификаторам (sid, id), не по именам.
- Справочник игры (шаблоны, цены, торговля, реакции): base, Newwworld, Dialogue, rebirth, Russian Dark UI simplistic, Martial Arts Fast Dodger, Better Map RUS and Zones

## Таблицы

| Файл | Строк | Ключ сортировки | Содержание |
|---|---|---|---|
| `squad.csv` | 30 | character_id | Один персонаж отряда игрока в строке |
| `equipment.csv` | 170 | character_id, kind, slot, sid | Оружие, броня и протезы персонажей: значения шаблона, множители и итоговые `calc_*` |
| `storage.csv` | 249 | location_key, zone, building_id, container, item, item_sid | Предметы в хранилищах зданий игрока |
| `item_prices.csv` | 594 | sid | Базовые цены записей игры без торговых коэффициентов |
| `trade_modifiers.csv` | 1533 | group, record_sid, field, ref_sid | Сырые торговые записи игры без вычисленных цен продажи и покупки |
| `unique_npcs.csv` | 79 | sid | Уникальные NPC мира и их состояние |
| `town_overrides.csv` | 9 | replacement_sid, town | Города, заменённые записями override |
| `diplomacy.csv` | 103 | faction_sid | Отношения фракций с игроком без классификации |
| `world_reactions.csv` | 310 | town_sid, override_sid, world_state_sid, condition, subject_sid | Условия вариантов городов: одна строка на условие World State |
| `world_reaction_links.csv` | 308 | town_sid, override_sid, world_state_sid, condition, npc_sid | Условия `NPC is`/`NPC is NOT` с текущим state_code NPC; соответствие условия не вычисляется |

## Недоступные и неопубликованные поля

Колонки `calc_*` в `equipment.csv` - значения по формулам конвертера (itemstats.py, prosthetics.py). `calc_status` = verified означает, что в строке сверены с карточкой игры все публикуемые `calc_*`; при остальных статусах все `calc_*` пусты, а `calc_status` объясняет причину. Значения публикуются без округления; совпадение с карточкой - равенство после округления до точности интерфейса (усечение целой части для сопротивлений, веса и нижней границы урона арбалета; округление для верхней границы урона и скорости выстрела); в CSV числа записываются с точностью до 6 знаков без хвостовых нулей (это не округление интерфейса); шаблоны берутся после применения модов снимка. verified только для сверенных сочетаний: броня - лёгкий и средний класс x кожа, кольчуга; средний x латы; тяжёлый x латы; оружие ближнего боя - катаны (Идущие по Клинку, Скелеты-кузнецы), сабли (Идущие по Клинку, Крест, Скелеты-кузнецы), древковое (Идущие по Клинку, Крест), тяжёлое (Катунский Кулибин), рубачи (Идущие по Клинку, Крест); арбалеты; протезы ног. Прочие сочетания получают `unverified_class`: в частности вес не сошёлся у тяжёлого оружия Скелетов-кузнецов (Падающее солнце: карточка 23, расчёт 24.0), рубачей Древних (карточка 5, расчёт 6) и катан Катунского Кулибина (карточка 9, расчёт 8.0). Колонок цены в `calc_*` нет: базовые цены - в `item_prices.csv`. Не подтверждено: порог скрытия атлетики на карточке; граница 59.x у брони Высокого уровня (подбор level; blunt и гарпун карточки на 1 ниже расчёта при level 60); грейды брони 5 «Прото» и 20 «Низкий»; множители протезов публикуются только для атлетики, плавания и скрытности. Значения шаблона (`tpl_*`), множители производителя и поправки грейда даны отдельными колонками.
- Содержимое инвентаря и рюкзаков персонажей, сведения о построенных зданиях и исследованиях в таблицы не входят.
- Смысл `v[1]`, `v[2]` у ссылок `world state`/`NPC is` в документах игры не описан; значения публикуются без трактовки.
- Итоговые цены продажи и покупки в городах не вычисляются: связь город - культура задана записями, но остальные множители (отряд-торговец, константы, разброс) не сверены с игрой.
- Для зданий без поселения в `storage.csv` колонка `settlement` пуста, а `location_key` содержит «зона N (поселение не определено)».

## Коды state_code уникальных NPC

Факт игры (fcs.def, WORLD_EVENT_STATE, поле `NPC is`): 0 - мёртв, 1 - жив и свободен, 2 - в плену.

## Словарь колонок

### squad.csv

| Колонка | Значение |
|---|---|
| `character_id` | Стабильный ID персонажа (`ps:` + portrait_serial, при отсутствии `h:`) |
| `name` | Имя |
| `race` | Раса |
| `is_animal` | Животное |
| `is_leader` | Лидер отряда |
| `female` | Пол женский |
| `squad_id` | ID отряда |
| `squad_name` | Название отряда |
| `zone` | Зона карты `x.y` из locations.json |
| `resolution_status` | Способ определения места: in_location, near_location, in_region, unknown |
| `region` | Регион карты |
| `settlement` | Поселение, в границах которого находится персонаж |
| `nearby_settlement` | Ближайшее поселение при near_location |
| `status_active` | Активные статусы (coma, dead, incapacitated, unconscious), через `; ` |
| `combat_modes_active` | Включённые боевые режимы, через `; ` |
| `blood` | Кровь |
| `hunger_raw` | Сытость, сырое значение сохранения |
| `bleeding` | Кровотечение |
| `ko` | Нокаут (KO) |
| `lost_limbs` | Потерянные конечности; пусто - поле в снимке отсутствует (нет потерянных) |
| `prosthetics` | Протезы: `слот: имя (level N, grade)`, через `; `; подробности - equipment.csv |
| `jobs_enabled` | Работы включены |
| `jobs_primary` | Основные работы `TASK [цель]` по порядку слотов, через `; ` |
| `jobs_temporary` | Временные работы, через `; ` |
| `carrying_target` | Кого несёт персонаж |
| `carried_by` | Кто несёт персонажа |
| `bounty_total` | Сумма наград за голову |
| `Dexterity` | Атрибут «Ловкость», базовое значение |
| `Perception` | Атрибут «Восприятие», базовое значение |
| `Strength` | Атрибут «Сила», базовое значение |
| `Toughness` | Атрибут «Крепость», базовое значение |
| `Armour Smithing` | Навык «Ковка доспехов», базовое значение |
| `Assassination` | Навык «Убийство», базовое значение |
| `Athletics` | Навык «Атлетика», базовое значение |
| `Blunt` | Навык «Дробящее», базовое значение |
| `Cooking` | Навык «Готовка», базовое значение |
| `Crossbow Smithing` | Навык «Ковка арбалетов», базовое значение |
| `Crossbows` | Навык «Арбалеты», базовое значение |
| `Dodge` | Навык «Уворот», базовое значение |
| `Engineering` | Навык «Инженерия», базовое значение |
| `Farming` | Навык «Фермерство», базовое значение |
| `Field Medic` | Навык «Полевой медик», базовое значение |
| `Hackers` | Навык «Рубачи», базовое значение |
| `Heavy Weapons` | Навык «Тяжелое оружие», базовое значение |
| `Katanas` | Навык «Катаны», базовое значение |
| `Labouring` | Навык «Работа», базовое значение |
| `Lockpicking` | Навык «Взлом», базовое значение |
| `Martial Arts` | Навык «Боевые искусства», базовое значение |
| `Melee Attack` | Навык «Атака (ближний бой)», базовое значение |
| `Melee Defence` | Навык «Защита (ближний бой)», базовое значение |
| `Polearms` | Навык «Древковое», базовое значение |
| `Precision Shooting` | Навык «Точная стрельба», базовое значение |
| `Robotics` | Навык «Роботехника», базовое значение |
| `Sabres` | Навык «Сабли», базовое значение |
| `Science` | Навык «Наука», базовое значение |
| `Stealth` | Навык «Скрытность», базовое значение |
| `Swimming` | Навык «Плавание», базовое значение |
| `Thievery` | Навык «Воровство», базовое значение |
| `Turrets` | Навык «Турели», базовое значение |
| `Weapon Smithing` | Навык «Ковка оружия», базовое значение |

### equipment.csv

| Колонка | Значение |
|---|---|
| `character_id` | ID персонажа |
| `character_name` | Имя персонажа |
| `kind` | weapon, armour или prosthetic |
| `slot` | weapon_back/weapon_hip, head/shirt/body/legs/boots или конечность протеза (left_leg...) |
| `item_name` | Название (ru) |
| `item_name_en` | Название (en), если отличается |
| `sid` | sid записи предмета в данных игры |
| `item_type` | melee или crossbow для оружия |
| `level` | Уровень экземпляра |
| `quality` | quality экземпляра из items[] (оружие и броня) |
| `grade` | Грейд: у оружия - запись material (Мейто, Катун No.N...), у брони и протезов - по уровню |
| `stolen` | Предмет помечен как краденый |
| `grade_sid` | sid записи грейда оружия |
| `manufacturer` | Производитель оружия (запись company) |
| `manufacturer_sid` | sid производителя |
| `armour_class` | Класс брони (cloth, light, medium, heavy) |
| `armour_material` | Материал брони (cloth, leather, chain, plate) |
| `coverage` | Покрытие частей тела `часть=доля`, через `; ` |
| `template_unshown` | Поля шаблона брони, не показываемые игрой, `поле=значение` |
| `manufacturer_cut_damage_mod` | Множитель/поправка производителя `cut damage mod` |
| `manufacturer_blunt_damage_mod` | Множитель/поправка производителя `blunt damage mod` |
| `manufacturer_weight_mod` | Множитель/поправка производителя `weight mod` |
| `grade_attack_mod` | Поправка грейда (запись material) `attack mod` |
| `grade_defence_mod` | Поправка грейда (запись material) `defence mod` |
| `tpl_cut_damage_multiplier` | Поле шаблона игры `cut damage multiplier`; пусто - не применимо к виду предмета |
| `tpl_blunt_damage_multiplier` | Поле шаблона игры `blunt damage multiplier`; пусто - не применимо к виду предмета |
| `tpl_weight_kg` | Поле шаблона игры `weight kg`; пусто - не применимо к виду предмета |
| `tpl_weight_mult` | Поле шаблона игры `weight mult`; пусто - не применимо к виду предмета |
| `tpl_armour_penetration` | Поле шаблона игры `armour penetration`; пусто - не применимо к виду предмета |
| `tpl_attack_mod` | Поле шаблона игры `attack mod`; пусто - не применимо к виду предмета |
| `tpl_defence_mod` | Поле шаблона игры `defence mod`; пусто - не применимо к виду предмета |
| `tpl_indoors_mod` | Поле шаблона игры `indoors mod`; пусто - не применимо к виду предмета |
| `tpl_bleed_mult` | Поле шаблона игры `bleed mult`; пусто - не применимо к виду предмета |
| `tpl_animal_damage_mult` | Поле шаблона игры `animal damage mult`; пусто - не применимо к виду предмета |
| `tpl_human_damage_mult` | Поле шаблона игры `human damage mult`; пусто - не применимо к виду предмета |
| `tpl_robot_damage_mult` | Поле шаблона игры `robot damage mult`; пусто - не применимо к виду предмета |
| `tpl_skill_category` | Поле шаблона игры `skill category`; пусто - не применимо к виду предмета |
| `tpl_pierce_damage_min_0` | Поле шаблона игры `pierce damage min 0`; пусто - не применимо к виду предмета |
| `tpl_pierce_damage_min_1` | Поле шаблона игры `pierce damage min 1`; пусто - не применимо к виду предмета |
| `tpl_pierce_damage_max_0` | Поле шаблона игры `pierce damage max 0`; пусто - не применимо к виду предмета |
| `tpl_pierce_damage_max_1` | Поле шаблона игры `pierce damage max 1`; пусто - не применимо к виду предмета |
| `tpl_reload_time_min` | Поле шаблона игры `reload time min`; пусто - не применимо к виду предмета |
| `tpl_reload_time_min_1` | Поле шаблона игры `reload time min 1`; пусто - не применимо к виду предмета |
| `tpl_reload_time_max` | Поле шаблона игры `reload time max`; пусто - не применимо к виду предмета |
| `tpl_reload_time_max_1` | Поле шаблона игры `reload time max 1`; пусто - не применимо к виду предмета |
| `tpl_accuracy_deviation_at_0_skill` | Поле шаблона игры `accuracy deviation at 0 skill`; пусто - не применимо к виду предмета |
| `tpl_accuracy_deviation_at_0_skill_1` | Поле шаблона игры `accuracy deviation at 0 skill 1`; пусто - не применимо к виду предмета |
| `tpl_range` | Поле шаблона игры `range`; пусто - не применимо к виду предмета |
| `tpl_range_1` | Поле шаблона игры `range 1`; пусто - не применимо к виду предмета |
| `tpl_shot_speed` | Поле шаблона игры `shot speed`; пусто - не применимо к виду предмета |
| `tpl_shot_speed_1` | Поле шаблона игры `shot speed 1`; пусто - не применимо к виду предмета |
| `tpl_accuracy_perfect_skill` | Поле шаблона игры `accuracy perfect skill`; пусто - не применимо к виду предмета |
| `tpl_class` | Поле шаблона игры `class`; пусто - не применимо к виду предмета |
| `tpl_material_type` | Поле шаблона игры `material type`; пусто - не применимо к виду предмета |
| `tpl_slot` | Поле шаблона игры `slot`; пусто - не применимо к виду предмета |
| `tpl_cut_into_stun` | Поле шаблона игры `cut into stun`; пусто - не применимо к виду предмета |
| `tpl_level_bonus` | Поле шаблона игры `level bonus`; пусто - не применимо к виду предмета |
| `tpl_blunt_def_bonus` | Поле шаблона игры `blunt def bonus`; пусто - не применимо к виду предмета |
| `tpl_cut_def_bonus` | Поле шаблона игры `cut def bonus`; пусто - не применимо к виду предмета |
| `tpl_pierce_def_mult` | Поле шаблона игры `pierce def mult`; пусто - не применимо к виду предмета |
| `tpl_weather_protection_amount` | Поле шаблона игры `weather protection amount`; пусто - не применимо к виду предмета |
| `tpl_weather_protection0` | Поле шаблона игры `weather protection0`; пусто - не применимо к виду предмета |
| `tpl_stealth_mult` | Поле шаблона игры `stealth mult`; пусто - не применимо к виду предмета |
| `tpl_ranged_skill_mult` | Поле шаблона игры `ranged skill mult`; пусто - не применимо к виду предмета |
| `tpl_dodge_mult` | Поле шаблона игры `dodge mult`; пусто - не применимо к виду предмета |
| `tpl_dexterity_mult` | Поле шаблона игры `dexterity mult`; пусто - не применимо к виду предмета |
| `tpl_asassination_mult` | Поле шаблона игры `asassination mult`; пусто - не применимо к виду предмета |
| `tpl_athletics_mult` | Поле шаблона игры `athletics mult`; пусто - не применимо к виду предмета |
| `tpl_combat_speed_mult` | Поле шаблона игры `combat speed mult`; пусто - не применимо к виду предмета |
| `tpl_damage_output_mult` | Поле шаблона игры `damage output mult`; пусто - не применимо к виду предмета |
| `tpl_fist_injury_mult` | Поле шаблона игры `fist injury mult`; пусто - не применимо к виду предмета |
| `tpl_unarmed_bonus` | Поле шаблона игры `unarmed bonus`; пусто - не применимо к виду предмета |
| `tpl_perception_bonus` | Поле шаблона игры `perception bonus`; пусто - не применимо к виду предмета |
| `tpl_combat_attk_bonus` | Поле шаблона игры `combat attk bonus`; пусто - не применимо к виду предмета |
| `tpl_combat_def_bonus` | Поле шаблона игры `combat def bonus`; пусто - не применимо к виду предмета |
| `tpl_combat_skill_bonus` | Поле шаблона игры `combat skill bonus`; пусто - не применимо к виду предмета |
| `tpl_ranged_bonus` | Поле шаблона игры `ranged bonus`; пусто - не применимо к виду предмета |
| `tpl_HP` | Поле шаблона игры `HP`; пусто - не применимо к виду предмета |
| `tpl_HP_1` | Поле шаблона игры `HP 1`; пусто - не применимо к виду предмета |
| `tpl_strength_mult` | Поле шаблона игры `strength mult`; пусто - не применимо к виду предмета |
| `tpl_strength_mult_1` | Поле шаблона игры `strength mult 1`; пусто - не применимо к виду предмета |
| `tpl_dexterity_mult_1` | Поле шаблона игры `dexterity mult 1`; пусто - не применимо к виду предмета |
| `tpl_athletics_mult_1` | Поле шаблона игры `athletics mult 1`; пусто - не применимо к виду предмета |
| `tpl_swimming_mult` | Поле шаблона игры `swimming mult`; пусто - не применимо к виду предмета |
| `tpl_swimming_mult_1` | Поле шаблона игры `swimming mult 1`; пусто - не применимо к виду предмета |
| `tpl_stealth_mult_1` | Поле шаблона игры `stealth mult 1`; пусто - не применимо к виду предмета |
| `tpl_thievery_mult` | Поле шаблона игры `thievery mult`; пусто - не применимо к виду предмета |
| `tpl_thievery_mult_1` | Поле шаблона игры `thievery mult 1`; пусто - не применимо к виду предмета |
| `tpl_ranged_mult` | Поле шаблона игры `ranged mult`; пусто - не применимо к виду предмета |
| `tpl_ranged_mult_1` | Поле шаблона игры `ranged mult 1`; пусто - не применимо к виду предмета |
| `tpl_unarmed_damage_bonus` | Поле шаблона игры `unarmed damage bonus`; пусто - не применимо к виду предмета |
| `tpl_unarmed_damage_bonus_1` | Поле шаблона игры `unarmed damage bonus 1`; пусто - не применимо к виду предмета |
| `tpl_encumbrance_mult` | Поле шаблона игры `encumbrance mult`; пусто - не применимо к виду предмета |
| `tpl_overall_mult` | Поле шаблона игры `overall mult`; пусто - не применимо к виду предмета |
| `calc_status` | Причина пустых calc_*: verified - рассчитано (сочетание сверено с карточками игры); unknown_level - level не определён; unknown_template - шаблон (или константы игры) не найден в справочнике; unverified_class - сочетание без карточки игры (броня: класс x материал; оружие: класс x производитель; протез не на ноге) |
| `calc_level` | level, использованный для расчёта calc_*; пусто - level неизвестен, все calc_* пусты |
| `calc_cut_damage` | Оружие ближнего боя: режущий урон (`cut damage multiplier` x `cut damage mod` x (0.3 + 0.017 x level)) |
| `calc_blunt_damage` | Оружие ближнего боя: дробящий урон (`blunt damage multiplier` x `blunt damage mod` x level / 50) |
| `calc_damage_min` | Арбалет: нижняя граница урона, без округления (карточка усекает до целого) |
| `calc_damage_max` | Арбалет: верхняя граница урона, без округления (карточка округляет до целого: 100.62 -> 101) |
| `calc_reload_min_s` | Арбалет: перезарядка, нижняя граница, с |
| `calc_reload_max_s` | Арбалет: перезарядка, верхняя граница, с |
| `calc_spread_deg` | Арбалет: разброс, градусы |
| `calc_range_m` | Арбалет: дальность, м |
| `calc_shot_speed_ms` | Арбалет: скорость выстрела, м/с, без округления (lerp(`shot speed`, `shot speed 1`, level/100) x 0.23; карточка округляет) |
| `calc_weight_kg` | Вес предмета, кг (оружие ближнего боя, броня); у арбалета и протеза - `tpl_weight_kg` |
| `calc_cut_resist_pct` | Броня: сопротивление разрезу, % |
| `calc_blunt_resist_pct` | Броня: сопротивление дробящему, % |
| `calc_harpoon_resist` | Броня: сопротивление гарпунам |
| `calc_cut_efficiency` | Броня: эффективность сопротивления разрезу (1 - `cut into stun`) |
| `calc_stealth_mult` | Броня и протез: множитель скрытности; 1 - нейтрально |
| `calc_ranged_mult` | Броня: множитель дальнего боя (арбалеты); 1 - нейтрально |
| `calc_dodge_mult` | Броня: множитель уворота; 1 - нейтрально |
| `calc_dexterity_mult` | Броня: множитель ловкости; 1 - нейтрально |
| `calc_combat_speed_mult` | Броня: множитель скорости боя; 1 - нейтрально |
| `calc_athletics_mult` | Броня и протез: множитель атлетики; 1 - нейтрально, у брони считается для ног и обуви |
| `calc_martial_arts_add` | Броня: поправка боевых искусств; 0 - нейтрально |
| `calc_swimming_mult` | Протез: множитель плавания; не округлён, UI показывает целые проценты усечением |
| `calc_hp_max` | Протез: ОЗ макс (округление до 5) |

### storage.csv

| Колонка | Значение |
|---|---|
| `settlement` | Поселение; пусто, если не определено |
| `location_key` | Ключ места: поселение или «зона N (поселение не определено)» |
| `settlement_status` | Способ привязки: in_location, town, near_location, zone_location (единственное поселение зоны по locations и справочнику мира), zone |
| `zone` | Зона карты |
| `building_id` | ID здания в сохранении |
| `building` | Название здания |
| `container` | Контейнер внутри здания; пусто - без контейнера |
| `item` | Название предмета (игра, ru) |
| `item_sid` | sid предмета |
| `quantity` | Количество |
| `base_price` | Базовая цена `value` (последний файл в порядке загрузки модов) |
| `base_price_source` | Файл, задающий цену |
| `unresolved` | Предмет не найден в данных игры |

### item_prices.csv

| Колонка | Значение |
|---|---|
| `sid` | sid записи |
| `name_en` | Название (en) |
| `name_ru` | Название (ru) |
| `type` | Тип записи (ITEM, ARMOUR, WEAPON, CROSSBOW, CONTAINER, LIMB_REPLACEMENT...) |
| `value` | Базовая цена `value`: последнее определение в порядке загрузки |
| `value_1` | `value 1` - цена высшего качества (протезы, арбалеты) |
| `value_source` | Файл последнего определения цены |
| `value_history` | Определения по файлам в порядке загрузки `файл=значение`, если их несколько |

### trade_modifiers.csv

| Колонка | Значение |
|---|---|
| `group` | culture (ITEMS_CULTURE, тип 104), culture_link (TOWN/FACTION: trade culture, trade prices), squad_template (SQUAD_TEMPLATE, тип 52), manufacturer (WEAPON_MANUFACTURER, тип 51), constant (CONSTANTS, тип 27) |
| `record_sid` | sid записи |
| `record_type` | Тип записи |
| `record_name` | Имя записи (en) |
| `record_files` | Файлы, определяющие запись, в порядке загрузки |
| `field` | Поле записи или категория ссылки |
| `value` | Значение скалярного поля |
| `ref_sid` | sid записи, на которую указывает ссылка |
| `ref_name` | Её название (ru или en) |
| `ref_v0` | Значение ссылки `v[0]`: для `trade prices` множитель цены, 100 = 100% |
| `ref_v1` | Значение ссылки `v[1]` (смысл не установлен) |
| `ref_v2` | Значение ссылки `v[2]` (смысл не установлен) |

### unique_npcs.csv

| Колонка | Значение |
|---|---|
| `sid` | sid уникального NPC (usedUniques) |
| `name_en` | Имя (en) |
| `name_ru` | Имя (ru) |
| `state_code` | Код состояния из сохранения: 0 - мёртв, 1 - жив и свободен, 2 - в плену |
| `player` | NPC входит в отряд игрока |
| `captured_by` | Персонаж отряда, который несёт пленного |

### town_overrides.csv

| Колонка | Значение |
|---|---|
| `replacement_sid` | sid записи-замены города (override) |
| `town` | Название города в сохранении |
| `raw_name` | Исходное имя записи состояния города |
| `replacement_name` | Название записи-замены (en), в нём вариант: destroyed, half destroyed... |
| `replacement_name_ru` | Название записи-замены (ru) |
| `faction_sid` | sid фракции города после замены |
| `faction_name` | Название фракции из данных игры |
| `factions_here` | sid фракций, присутствующих в городе, через `; ` |

### diplomacy.csv

| Колонка | Значение |
|---|---|
| `faction_sid` | sid фракции |
| `faction_name` | Название фракции |
| `relation` | Отношение фракции к игроку, сырое значение (-100...100) |
| `trust` | trust, сырое значение |
| `trust_neg` | trust_neg, сырое значение |

### world_reactions.csv

| Колонка | Значение |
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

### world_reaction_links.csv

| Колонка | Значение |
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

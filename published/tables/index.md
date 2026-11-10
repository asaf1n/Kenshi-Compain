# Табличные выгрузки

- snapshot_id: `sha256-9f47dae6fafa887c4e11f5456905e491aac3a3ee596128c352a5e716676a505f`
- Игровое время: День 136, 17:23
- Формат: CSV, UTF-8 без BOM, LF, RFC 4180, разделитель - запятая; первая строка - заголовок.
- Пустая ячейка - значение отсутствует или не применимо; числа с точкой без разделителей разрядов, булевы `true`/`false`; списки в ячейке разделены `; `.
- Строки отсортированы по ключу; меток времени в таблицах нет; связи между таблицами - по идентификаторам (sid, id), не по именам.
- Справочник игры (шаблоны, цены, торговля, реакции): base, Newwworld, Dialogue, rebirth, Russian Dark UI simplistic, Martial Arts Fast Dodger, Better Map RUS and Zones

## Таблицы

| Файл | Строк | Ключ сортировки | Содержание |
|---|---|---|---|
| `squad.csv` | 30 | character_id | Один персонаж отряда игрока в строке |
| `equipment.csv` | 252 | location_kind, character_id / здание, kind, slot, sid, level, quality | Все экземпляры оружия, брони и протезов (надетые, запасные у персонажей, на складах): значения шаблона, множители и итоговые `calc_*` |
| `inventory.csv` | 448 | character_id, container, slot, base_sid, level, dup_no | Все предметы персонажей отряда поэкземплярно: надетое, пояс, рюкзаки, инвентарь |
| `storage.csv` | 224 | location_key, zone, building_id, container, item, item_sid | Предметы в хранилищах зданий игрока: строка на запись сейва (стопка), экземпляры разного уровня раздельно |
| `buildings.csv` | 176 | location_key, zone, parent_instance_id, instance_id | Все постройки, интерьерные станки, турели, генераторы, контейнеры и разрабатываемые рудные жилы игрока |
| `research.csv` | 181 | category, level, sid | Полное дерево технологий игры (RESEARCH) со статусом изучения в кампании, стоимостью, предпосылками и открываемыми объектами |
| `build_catalog.csv` | 229 | building_category, sid | Каталог и смета всех строящихся объектов игры (BUILDING): статус открытия, стройматериалы, энергобаланс, входы/выходы и апгрейды |
| `biome_resources.csv` | 74 | biome_sid | Ресурсный, климатический и ветровой профиль регионов (BIOME_GROUP + ENVIRONMENT_RESOURCES + SEASON/WEATHER) для оценки площадок под форпост |
| `item_prices.csv` | 594 | sid | Базовые цены записей игры без торговых коэффициентов |
| `trade_modifiers.csv` | 1533 | group, record_sid, field, ref_sid | Сырые торговые записи игры без вычисленных цен продажи и покупки |
| `unique_npcs.csv` | 79 | sid | Уникальные NPC мира и их состояние |
| `town_overrides.csv` | 9 | replacement_sid, town | Города, заменённые записями override |
| `diplomacy.csv` | 103 | faction_sid | Отношения фракций с игроком без классификации |
| `world_reactions.csv` | 310 | town_sid, override_sid, world_state_sid, condition, subject_sid | Условия вариантов городов: одна строка на условие World State |
| `world_reaction_links.csv` | 308 | town_sid, override_sid, world_state_sid, condition, npc_sid | Условия `NPC is`/`NPC is NOT` с текущим state_code NPC; соответствие условия не вычисляется |
| `unit_templates.csv` | 682 | sid | Шаблоны персонажей и животных: раса, уровни и навыки как хранятся |
| `unit_template_gear.csv` | 5822 | template_sid, category, ref_sid | Оружие, арбалеты, уровень оружия, одежда и рюкзаки шаблонов персонажей |
| `squad_templates.csv` | 959 | sid | Шаблоны отрядов и патрулей: фракция, условия появления, флаги |
| `squad_members.csv` | 2131 | squad_sid, role, member_sid | Состав шаблонов отрядов по ролям |
| `squad_spawns.csv` | 713 | source, place_sid, squad_sid | Где появляются отряды: бездомные отряды групп биомов и бродячие отряды городов; привязки группы биомов к зонам карты в данных нет |
| `faction_relations.csv` | 317 | faction_sid, kind, other_sid | Заданные в данных отношения фракций между собой без классификации |
| `faction_hostility.csv` | 103 | faction_sid | Настройки фракций (враждебность, доверие, бегство) и расовый состав; враждебности по расе, полу и протезам в данных нет |
| `races.csv` | 53 | sid | Расы игры (RACE) с учётом порядка загрузки модов: иммунитет к погоде, естественная броня, скорости, множители, анатомия |

## Недоступные и неопубликованные поля

Колонки `calc_*` в `equipment.csv` - значения по формулам конвертера (itemstats.py, prosthetics.py). `calc_status` = verified означает, что в строке сверены с карточкой игры все публикуемые `calc_*`; при остальных статусах все `calc_*` пусты, а `calc_status` объясняет причину. Значения публикуются без округления; совпадение с карточкой - равенство после округления до точности интерфейса (усечение целой части для сопротивлений, веса и нижней границы урона арбалета; округление для верхней границы урона и скорости выстрела); в CSV числа записываются с точностью до 6 знаков без хвостовых нулей (это не округление интерфейса); шаблоны берутся после применения модов снимка. verified только для сверенных сочетаний: броня - лёгкий и средний класс x кожа, кольчуга; средний x латы; тяжёлый x латы; оружие ближнего боя - катаны (Идущие по Клинку, Скелеты-кузнецы), сабли (Идущие по Клинку, Крест, Скелеты-кузнецы), древковое (Идущие по Клинку, Крест), тяжёлое (Катунский Кулибин), рубачи (Идущие по Клинку, Крест); арбалеты; протезы ног. Прочие сочетания получают `unverified_class`: в частности вес не сошёлся у тяжёлого оружия Скелетов-кузнецов (Падающее солнце: карточка 23, расчёт 24.0), рубачей Древних (карточка 5, расчёт 6) и катан Катунского Кулибина (карточка 9, расчёт 8.0). Колонок цены в `calc_*` нет: базовые цены - в `item_prices.csv`. Не подтверждено: порог скрытия атлетики на карточке; граница 59.x у брони Высокого уровня (подбор level; blunt и гарпун карточки на 1 ниже расчёта при level 60); грейды брони 5 «Прото» и 20 «Низкий»; множители протезов публикуются только для атлетики, плавания и скрытности. Значения шаблона (`tpl_*`), множители производителя и поправки грейда даны отдельными колонками.
- Предметы персонажей поэкземплярно - `inventory.csv` (контейнеры body, belt, backpack, inventory; ключ сравнения снимков (character_id, base_sid, level, slot, dup_no), `item_sid` действует внутри снимка). Оружие, броня и протезы независимо от места - `equipment.csv` (`location_kind`). Вес экземпляров и параметры рюкзаков, здоровье по частям тела в таблицы не входят. Построенные здания, интерьерные станки, очереди крафта и разрабатываемые жилы - `buildings.csv`; полное дерево технологий со статусом изучения - `research.csv`; смета стройматериалов и ТТХ всех построек меню строительства - `build_catalog.csv`; ресурсно-климатический профиль регионов (плодородие, вода, руды, ветер, кислотность) - `biome_resources.csv` (локальные пятна кнопки «Разведка» в рантайме вычисляются процедурным шумом и в сохранение не записываются).
- `races.csv`: поля записей RACE после слияния файлов в порядке загрузки; пустая ячейка - поле не хранится (действует значение по умолчанию fcs.def). Расшифровка кодов погоды 1-4 сверена с карточками брони, прочие не расшифрованы.
- Смысл `v[1]`, `v[2]` у ссылок `world state`/`NPC is` в документах игры не описан; значения публикуются без трактовки.
- Справочник юнитов (`unit_templates.csv`, `unit_template_gear.csv`, `squad_templates.csv`, `squad_members.csv`, `squad_spawns.csv`, `faction_relations.csv`, `faction_hostility.csv`): значения шаблонов как хранятся в данных набора модов снимка, без вычисленных оценок; итоговые навыки персонажа игра получает с разбросом `stats_randomise`. Не публикуется: враждебность по расе, полу и протезам (в данных такого поля нет), привязка групп биомов к зонам карты (в записях её нет), имена кодов `NPC class`, `armour grade`, `fundamental type`, `slave` (перечисления не заданы в данных).
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
| `character_id` | ID персонажа; пусто у складских предметов |
| `character_name` | Имя персонажа |
| `kind` | weapon, armour или prosthetic |
| `slot` | weapon_back/weapon_hip, head/shirt/body/legs/boots или конечность протеза (left_leg...); у запасных и складских - слот или конечность по шаблону предмета, у оружия пусто |
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
| `location_kind` | Где экземпляр: worn - надето (строки прежнего вида; протез установлен), inventory - основной инвентарь персонажа, backpack - внутри рюкзака, belt - пояс, storage - склад здания, other_slot - второй предмет в слоте надетого (не показан в weapons/armour) |
| `quantity` | Количество в стопке; у надетого - из items[], у протезов пусто |
| `container` | backpack: название рюкзака; storage: контейнер внутри здания (как в storage.csv); иначе пусто |
| `building_id` | storage: ID здания в сохранении |
| `building` | storage: название здания |
| `settlement` | storage: поселение; пусто, если не определено |
| `zone` | storage: зона карты |
| `tpl_races` | Брони: расы, только которым разрешено её надевать (`races`); пусто - ограничения нет |
| `tpl_races_exclude` | Брони: расы, которым запрещено её надевать (`races exclude`) |

### inventory.csv

| Колонка | Значение |
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
| `level` | Уровень экземпляра как в сейве (у расходников 0) |
| `quality` | quality экземпляра как в сейве (у брони и оружия 100, у прочих 1; смысл у расходников не установлен) |
| `grade` | Грейд: оружие - запись material, броня и арбалет - по уровню, протез - по уровню; пусто - не определён |
| `charges` | charges как в сейве (для еды - питательность на единицу) |
| `stolen` | true - краденый; пусто - нет |
| `unique` | Признак unique из сейва |

### buildings.csv

| Колонка | Значение |
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

### research.csv

| Колонка | Значение |
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

### build_catalog.csv

| Колонка | Значение |
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

### biome_resources.csv

| Колонка | Значение |
|---|---|
| `biome_sid` | sid записи BIOME_GROUP (тип 95) |
| `name_en` | Название региона (en) |
| `name_ru` | Название региона (ru) |
| `color_index` | Цветовой код региона на карте (`index`) |
| `locations_total` | Всего стационарных локаций в регионе по справочнику мира (`world_reference.json`) |
| `locations_discovered` | Открыто локаций игроком (`discovered = true` в `quick.save`) |
| `player_buildings_count` | Число верхнеуровневых построек и рудных точек игрока в регионе |
| `player_mining_nodes` | Уже разрабатываемые игроком рудные точки (`MINING`) в регионе с их `resource_mult` |
| `climate_arid` | Доля засушливого климата (`arid` из ENVIRONMENT_RESOURCES) |
| `climate_green` | Доля зелёного климата (`green` из ENVIRONMENT_RESOURCES) |
| `climate_swamp` | Доля болотного климата (`swamp` из ENVIRONMENT_RESOURCES) |
| `farming_min` | Минимальное плодородие почвы в регионе (`farming min`) |
| `farming_mult` | Максимальный множитель плодородия почвы (`farming mult`) |
| `farming_altitude_min` | Нижняя граница высоты плодородия (`farming altitude min`) |
| `farming_altitude_max` | Верхняя граница высоты плодородия (`farming altitude max`) |
| `water_min` | Минимальный уровень грунтовых вод (`water min`) |
| `water_mult` | Максимальный множитель грунтовых вод (`water mult`) |
| `water_altitude_min` | Нижняя граница высоты грунтовых вод (`water altitude min`) |
| `water_altitude_max` | Верхняя граница высоты грунтовых вод (`water altitude max`) |
| `farm_water_usage` | Множитель расхода воды фермами в регионе (`farm water usage`) |
| `iron_mult` | Множитель железной руды в регионе (`iron mult`) |
| `copper_mult` | Множитель медной руды в регионе (`copper mult`) |
| `stone_mult` | Множитель камня в регионе (`stone mult`) |
| `stone_noise_cutoff` | Порог Perlin-шума пятен камня (`stone noise cutoff`; меньше — крупнее пятна) |
| `carbon_mult` | Множитель углерода/топлива (`carbon mult`) |
| `wind_speed_min` | Минимальная скорость ветра по сезонам региона (`wind speed min` из WEATHER) |
| `wind_speed_max` | Максимальная скорость ветра по сезонам региона (`wind speed max` из WEATHER) |
| `wind_speed_weighted_avg` | Средневзвешенная скорость ветра по длительности сезонов и вероятностям погоды |
| `acidic_ground` | Кислотность почвы (`acidic ground`, 0..1: обжигает ноги без обуви) |
| `acidic_water` | Кислотность воды (`acidic water`, 0..1) |
| `weather_affect_codes` | Коды погодных угроз в сезонах региона (`affect type` из WEATHER и WEATHER_EFFECT) |
| `weather_hazards` | Расшифровка погодных угроз (1 песчаная буря, 2 кислотный дождь, 3 жара/лучи, 4 газ; сопоставимо с `races.csv`) |

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

### unit_templates.csv

| Колонка | Значение |
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

### unit_template_gear.csv

| Колонка | Значение |
|---|---|
| `template_sid` | sid шаблона (unit_templates.csv) |
| `template_name` | Название шаблона (ru или en) |
| `category` | Категория ссылки: weapons - v0 количество, v1 слот (0 пояс, 1 спина), v2 абсолютный шанс, % (сумма < 100 - шанс остаться без оружия); crossbows - v0 количество, v1 шанс, % (шансы не относительные); weapon level - v0 относительный шанс; запись - производитель оружия (уровень оружия); clothing - v0 количество, v1 шанс, % (нормируется среди предметов одного типа); backpack - v1 абсолютный шанс, %; robot limbs - v0 качество, v1 относительный шанс; отрицательное качество - оставить настоящую конечность; weapon - встроенное оружие животного |
| `ref_sid` | sid предмета или производителя |
| `ref_name` | Название (ru или en) |
| `ref_type` | Тип записи (WEAPON, CROSSBOW, ARMOUR, WEAPON_MANUFACTURER, CONTAINER, LIMB_REPLACEMENT) |
| `v0` | Значение ссылки `v[0]` |
| `v1` | Значение ссылки `v[1]` |
| `v2` | Значение ссылки `v[2]` |

### squad_templates.csv

| Колонка | Значение |
|---|---|
| `sid` | sid шаблона отряда (SQUAD_TEMPLATE, тип 52) |
| `name_en` | Имя записи (en) |
| `name_ru` | Имя записи (ru, gamedata.po) |
| `files` | Файлы, определяющие запись, в порядке загрузки |
| `faction_sids` | sid фракции отряда (`faction`); пусто - не задана |
| `faction_names` | Названия фракций |
| `world_state_sids` | sid World State (`world state`): отряд появляется, только когда условия выполнены (AND) |
| `world_state_required` | Требуемое значение `v[0]` по порядку world_state_sids: 1 - состояние истинно, 0 - ложно |
| `race_override_sids` | sid расы, принудительной для всего отряда (`race override`) |
| `race_override_names` | Названия рас |
| `roaming_military` | Считается бродячими войсками, даже если есть родной город |
| `patrol_approaches_towns` | Патруль заходит в ближние города |
| `dont_multiply` | Размер не зависит от множителя размера отрядов в настройках |
| `regenerates` | Отряд-житель медленно восстанавливает потери |
| `is_trader` | Торговый отряд |
| `num_random_chars` | Минимум персонажей, выбираемых из `choosefrom list` |
| `num_random_chars_max` | Максимум персонажей, выбираемых из `choosefrom list` |

### squad_members.csv

| Колонка | Значение |
|---|---|
| `squad_sid` | sid шаблона отряда (squad_templates.csv) |
| `squad_name` | Название отряда (ru или en) |
| `role` | Роль ссылки: leader - v0 число лидеров; squad - v0 минимум, v1 максимум (0 - не случайно); squad2 - v0 минимум, v1 максимум (0 - не случайно); вторая половина отряда; animals - v0 минимум, v1 максимум, v2 возраст (100 взрослый, 0 детёныш); animals2 - v0 минимум, v1 максимум, v2 возраст (100 взрослый, 0 детёныш); choosefrom list - v0 шанс; число выбираемых - num_random_chars и num_random_chars_max в squad_templates.csv; prisoners - шаблоны отрядов-заключённых; slaves - шаблоны отрядов-рабов; housemates - v0 минимум, v1 максимум дополнительных отрядов в том же здании |
| `member_sid` | sid шаблона персонажа (CHARACTER), животного (ANIMAL_CHARACTER) или отряда (SQUAD_TEMPLATE) |
| `member_name` | Название (ru или en) |
| `member_type` | Тип записи |
| `v0` | Значение ссылки `v[0]` (смысл зависит от роли) |
| `v1` | Значение ссылки `v[1]` |
| `v2` | Значение ссылки `v[2]` |

### squad_spawns.csv

| Колонка | Значение |
|---|---|
| `source` | biome_homeless - `homeless spawns` группы биомов (BIOME_GROUP); town_roaming - `roaming squads` города (TOWN) |
| `place_sid` | sid группы биомов или города |
| `place_name_en` | Название (en) |
| `place_name_ru` | Название (ru, gamedata.po) |
| `place_faction_sid` | sid фракции города (`faction`); для биомов пусто |
| `spawn_amount` | `homeless spawn amount` биома: примерное число бездомных отрядов на зону; для городов пусто |
| `squad_sid` | sid шаблона отряда (squad_templates.csv) |
| `squad_name` | Название отряда (ru или en) |
| `ref_v0` | Значение ссылки `v[0]`: у biome_homeless - относительный шанс появления; у town_roaming смысл не задан |

### faction_relations.csv

| Колонка | Значение |
|---|---|
| `faction_sid` | sid фракции-источника |
| `faction_name` | Название (ru или en) |
| `kind` | relation - `relations` (отношение к другой фракции); coexistence - `coexistence` (фракции, с которыми стремится сосуществовать); legal_system - `legal system` (чьи законы применяются) |
| `other_sid` | sid другой фракции |
| `other_name` | Название (ru или en) |
| `value` | Только для relation: отношение -100...100 как хранится; не указанные пары равны `default_relation` фракции (faction_hostility.csv); симметрия не предполагается |

### faction_hostility.csv

| Колонка | Значение |
|---|---|
| `faction_sid` | sid фракции |
| `faction_name_en` | Имя записи (en) |
| `faction_name_ru` | Имя записи (ru) |
| `files` | Файлы, определяющие запись, в порядке загрузки |
| `default_relation` | Отношение к фракциям, не перечисленным в `relations`, -100...100 |
| `enemy_classification` | Максимальное отношение, при котором фракция считает другую врагом (нападает при виде) |
| `business_relations` | Минимальное отношение для торговли |
| `trustworthy` | Надёжность фракции -100...100 |
| `effect_of_anger` | Влияние гнева на реальные отношения (множитель) |
| `effect_of_happy` | Влияние довольства на реальные отношения (множитель) |
| `emotion_fade_rate` | Скорость возврата эмоций к нулю (множитель) |
| `run_away_ratio_of_squad_size` | Доля потерь отряда, после которой он бежит (0-1) |
| `run_away_ratio_relative_to_enemy` | Соотношение сил с врагом, при котором отряд бежит |
| `not_real` | Не человеческая фракция: действия против неё не считаются преступлением |
| `anti_slavery` | Против рабства |
| `heals_strangers` | Помогает раненым чужакам |
| `offers_bounties` | Может назначать награду за голову |
| `allow_slaves_weapons` | Рабам разрешено оружие |
| `fundamental_type` | Базовая классификация, код `fundamental type` (CharacterTypeEnum, имена в данных не заданы) |
| `squad_formation` | Построение отрядов, код `squad formation` (0 RANDOM, 1 CARAVAN, 2 MILITARY: fcs_enums.def) |
| `race_sids` | sid рас фракции (`races`), через `; ` |
| `race_names` | Названия рас |
| `race_weights` | Доля расы `v[0]` (относительная) по порядку race_sids |

### races.csv

| Колонка | Значение |
|---|---|
| `sid` | sid записи RACE (тип 7) |
| `name_en` | Имя записи (en) |
| `name_ru` | Имя записи (ru, gamedata.po) |
| `files` | Файлы, определяющие запись, в порядке загрузки: поле последнего файла заменяет предыдущие (rebirth после базы) |
| `weather_immunity_codes` | Коды `weather immunity0..N` как хранятся, через `; `; 0 - WA_NONE (иммунитета нет); пусто - полей нет |
| `weather_immunity` | Расшифровка: 1 песчаная буря, 2 кислотный дождь, 3 жара, 4 газ (перечисление WeatherAffecting в fcs.def не задано, коды сверены с карточками брони); прочие коды помечены «не установлен» |
| `weather_immunity_source` | Файл последнего определения кодов |
| `weather_immunity_by_file` | Коды по файлам `файл=коды`, если запись определена в нескольких файлах; слияние идёт по ключам weather immunityN, удаление кода перекрывающим файлом не распознаётся |
| `natural_armour_sids` | sid ARMOUR естественной брони (`natural armour`): добавляется к надетой; уровень в записи расы не задан |
| `natural_armour_names` | Название |
| `natural_armour_template` | Поля шаблона этой брони `поле=значение` как хранятся |
| `combat_anatomy` | Части тела `часть=доля попадания/здоровье` как хранятся (val0/val1 ссылки LOCATIONAL_DAMAGE) |
| `armour_only_for_race` | Броня, у которой в `races` указана эта раса. Броня с непустым `races`, где расы нет, для неё недоступна (таких записей брони в данных: 8) |
| `armour_excluded_for_race` | Броня, у которой эта раса указана в `races exclude` |
| `playable` | `playable`: Игрок может выбрать расу; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `is_robot` | `is robot`: Робот: атрибуты фиксированы и растут только протезами; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `single_gender` | `single gender`: Один пол; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `no_hats` | `no hats`: Нет слота шлема: шлемы не надеваются; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `no_shirts` | `no shirts`: Нет слота рубахи: рубахи не надеваются; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `no_shoes` | `no shoes`: Нет слота обуви: обувь не надевается; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `speed_min_skill` | `speed min skill`: Скорость бега при минимальной Атлетике; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `speed_max_skill` | `speed max skill`: Скорость бега при максимальной Атлетике; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `walk_speed` | `walk speed`: Скорость шага; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `combat_move_speed_mult` | `combat move speed mult`: Множитель боевой скорости (fcs.def: 1.0 - человек); пусто - поле не хранится (значение по умолчанию fcs.def) |
| `swim_speed_mult` | `swim speed mult`: Множитель скорости плавания; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `swim_speed` | `swim speed`: Скорость плавания, целое как хранится; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `strength_mult` | `strength`: Множитель атрибута Сила; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `dexterity_mult` | `dexterity`: Множитель атрибута Ловкость; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `bleed_rate` | `bleed rate`: Множитель кровотечения (0 - без крови); пусто - поле не хранится (значение по умолчанию fcs.def) |
| `heal_rate` | `heal rate`: Множитель лечения; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `hunger_rate` | `hunger rate`: Скорость голода (множитель); пусто - поле не хранится (значение по умолчанию fcs.def) |
| `min_blood` | `min blood`: Кровь при минимальной силе/возрасте; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `max_blood` | `max blood`: Кровь при максимальной силе/возрасте; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `extra_attack_slots` | `extra attack slots`: Добавка к числу атакующих слотов; пусто - поле не хранится (значение по умолчанию fcs.def) |
| `overridden_fields` | Поля, чьё значение задано не первым файлом записи: `поле=файл последнего определения` |

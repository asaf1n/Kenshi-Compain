# Атлас регионов Kenshi (Vanilla)

Полный справочник по всем регионам из docs/reference/regions-index.md. Русские названия — приоритетно из индекса и docs/Kenshi_RU_EN.md; уникальные NPC — по `published/tables/unique_npcs.csv``. Английские термины в скобках при первом упоминании. Источники: kenshi.zone (environment-hazards, world-map, locations), Kenshi Wiki (Zones, individual region pages), regions-index.md. Vanilla only. Связь с World States — ссылками на world-states.md.

Кто появляется в каждом регионе и городе, состав отрядов и отношения фракций между собой — `docs/reference/encounters.md`.

Соседство — общая граница в растре регионов игры `data/newland/land/areasmap.tga` (256 × 256, пиксель 1152 ед.; соседи перечислены по длине общей границы), извлечённом конвертером в `data/world/<world_ref_id>.json` (`regions_map`). Положение — по игровой карте и координатам локаций `published/world_reference.json`. Соседство не означает проходимости: граница может идти по горам или воде. Контурная карта регионов — `docs/reference/regions_map.svg`.

Карта — единый континент ~870 км² без загрузочных экранов. Зоны определяют спавны врагов, сезоны и модификаторы среды. Слои (зоны, биом, ресурсы) не совпадают. Безопасность зависит от расы сильнее координат: Святая Нация (Holy Nation) убивает нелюдей и скелетов/протезы на месте.

## Авантюра Стоба (Stobe's Gamble)
Положение: юго-восток. Соседи: Ровная лагуна (Flats Lagoon), Мщение (Venge), Серый шельф (Greyshelf), Долина снайперов (Sniper Valley), Утёсы (The Crags), Сад Стоба (Stobe's Garden), Ненужная зона (The Unwanted Zone), Звонкий мрак (Sonorous Dark).
Среда: вулканический климат, коренная порода, пепел. Кислотный дождь в части зон. Источник: https://kenshi.zone/en/environment-hazards, https://kenshi.zone/en/world-map.
Локации (из индекса):
- Затерянный склад доспехов (Lost Armour Store) — ruins
- Осыпающиеся лабы (Crumbling Labs) — ruins · секретная
- Свободное селение (Free Settlement) — ruins
- Скачок (Spring) — town · секретная
- Тайная наркоферма (Secret Drug Farm) — outpost
- Форпост снабжения старой империи (Old Empire Supply Outpost) — ruins · секретная
- Экспедиция 5 (Expedition 5) — ruins
Постоянные NPC / вербуемые: в проверенных источниках нет данных по уникальным постоянным.
Противники: высокие уровни, кислотные угрозы. Связь с WS: см. world-states.md.
Источники: regions-index.md, https://kenshi.zone/en/locations, https://kenshi.zone/en/environment-hazards.

## Арах (Arach)
Положение: юго-запад. Соседи: Дозорный рубеж (Watcher's Rim), Шан (Shun), Паучьи равнины (Spider Plains).
Среда: высокая опасность, пауки. Источник: community maps / kenshi.zone locations.
Локации:
- Трон Хозяина Жуков (Throne of the Bugmaster) — poi
- Упавшая башня (Fallen Tower) — ruins
Постоянные NPC: Хозяин Жуков (Bugmaster). Вербуемые: нет. Связь с WS: сдача награды для Сэто (см. recruits.md, world-states.md).
Источники: regions-index.md, https://kenshi.fandom.com/wiki/Bugmaster, https://kenshi.zone/en/locations.

## Берег грозового ущелья (Stormgap Coast)
Положение: восток. Соседи: Дальние земли (The Outlands), Мщение (Venge), Кишка (Gut), Запретный остров (Forbidden Isle), Глаз (The Eye), Ненужная зона (The Unwanted Zone).
Среда: кислотные дожди в прибрежных зонах (спорадически). Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Глазница (Eyesocket) — slave_camp
- Грань (Brink) — town
- Деревня культистов (Cult Village) — village
- Рыбацкая деревня (Fishing Village) — village
Вербуемые: Хоббс (Hobbs) в Рыбацкой деревне. Связь с WS: см. world-states.md.
Источники: regions-index.md, https://kenshi.zone/en/environment-hazards, recruits.md.

## Берег левиафанов (Leviathan Coast)
Положение: северо-запад. Соседи: Равнины людоедов (Cannibal Plains), Железный шлейф (The Iron Trail).
Среда: северный край. Угрозы: левиафаны, людоеды (вынос раненых). Источник: https://kenshi.zone/en/locations.
Локации:
- Затерянная библиотека (Lost Library) — ruins
- Затерянный арсенал (Lost Armoury) — ruins · секретная (×3)
- Старая имперская башня (Old Empire Watchtower) — ruins (×2)
- Упавшая башня (Fallen Tower) — ruins
Вербуемые: Зелёный палец (Green Finger) в Рыбацкой деревне (Deadcat). Источники: recruits.md.

## Болото (The Swamp)
Положение: юго-запад. Соседи: Южные болота (South Wetlands), Пограничная зона (Border Zone), Паучьи равнины (Spider Plains), Горящий лес (Burning Forest), Сим (Shem), Верхние поля костей (High Bonefields), Сетка (The Grid).
Среда: избыток воды (200 %), высокая fertility. Кислотные дожди: в проверенных источниках нет данных. Источник: https://kenshi.zone/en/world-map.
Локации:
- Акула (Shark) — town
- Гниль (Rot) — village
- Город из грязи (Mud Town) — village
- Деревня Каменных Крыс (Stone Rat Village) — village
- Деревня Серодёров (Grayflayer Village) — village
- Деревня на болоте (Swamp Village) — village (×2)
- Заболоченная лаба (Swamped Lab) — ruins
- Заражённая лаба (Infested Lab) — ruins
- Логово Красных сабель (Red Sabre Hideout) — poi · секретная
- Пустые развалины (Empty Ruin) — poi
- Форпост затерянной библиотеки (Lost Library Outpost) — ruins
Вербуемые: Доктор Чон (Doctor Chung), Зелёный (Green), Хамут (Hamut), Мью (Miu), Стабс момусо (Stubs Momuso). Связь с WS: Акула, Гниль, Деревня Серодёров (см. world-states.md).
Источники: regions-index.md, https://kenshi.zone/en/world-map, recruits.md.

## Великая пустыня (The Great Desert)
Положение: северо-восток, ядро Союзных Городов (United Cities). Соседи: Хэн (Heng), Мочалка (Bast), Хребтовый каньон (Spine Canyon), Синкаан (Sinkuun), Рвущие пески (Skimsands).
Среда: water 20 %, fertility 75 %, ample ore. Песчаные бури. Источник: https://kenshi.zone/en/world-map, https://kenshi.zone/en/environment-hazards.
Локации:
- Барк (Bark) — town
- Груз (Heft) — town
- Каменный лагерь (Stone Camp) — slave_camp
- Отдалённый улей (Distant Hive Village) — village
- Порт Юг (Port South) — slave_camp
- Старая деревня (Old Village) — ruins
- Стоат (Stoat) — town
- Форт Мираж (Fort Mirage) — outpost
- Шо-Баттаи (Sho-Battai) — town
NPC: Император Тэнгу (в Грузе). Вербуемые: Эллс (Ells) в Шо-Баттаи, Ред (Red) в Барке. Связь с WS: см. world-states.md.
Источники: regions-index.md, https://kenshi.zone/en/locations.

## Возрождение (Rebirth)
Положение: северо-запад, территория Святой Нации. Соседи: Окранов залив (Okran's Gulf), Путь (Wend), Окранова гордость (Okran's Pride), Пойма (Floodlands).
Среда: рабский лагерь. Источник: regions-index.md.
Локации:
- Возрождение (Rebirth) — slave_camp
- Убежище Отщепенцев (Flotsam Safehouse) — poi
Связь с WS: Молл может захватить при выбытии лидеров СН (см. world-states.md).
Источники: regions-index.md, world-states.md.

## Восточные каньоны (The Pits East)
Положение: юго-восток. Соседи: Каньоны (The Pits), Зелёный пляж (Greenbeach), Сад Стоба (Stobe's Garden).
Среда: кислотные угрозы, песчаные бури. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Город крабов (Crab Town) — outpost · секретная
- Старая мастерская (Dead Workshop) — ruins
- Форпост снабжения старой империи (Old Empire Supply Outpost) — ruins · секретная
Вербуемые: Луми (Lumi) в Городе крабов. Источники: recruits.md.

## Гиблые земли (Deadlands)
Положение: центр. Соседи: Скорняков край (Skinner's Roam), Железные долины (Iron Valleys), Серая пустыня (Grey Desert), Сим (Shem), Чёрная пустыня (The Black Desert), Мщение (Venge).
Среда: постоянный кислотный дождь, кислотная земля и озёра, нет ветра. Иммунитет: скелеты, улей, рыболюды, людоеды, животные. Источник: https://kenshi.zone/en/deadlands, https://kenshi.zone/en/environment-hazards.
Локации:
- Затерянный арсенал (Lost Armoury) — ruins · секретная (×2)
- Мастерская в пустоши (Deadland Workshop) — ruins (×3)
- Мастерская перепрошивки (Reprogramming Workshop) — ruins
- Развалины арсенала (Armoury Ruin) — ruins
- Хламилище (Scraphouse) — poi
- Чёрная Пустыня (Black Desert City) — town
NPC: Мрачный Нил (Sadneil) в Чёрной Пустыне. Источники: recruits.md, https://kenshi.zone/en/deadlands.

## Горящий лес (Burning Forest)
Положение: юг, восточнее Болота. Соседи: Болото (The Swamp), Сим (Shem), Поля костей (Bonefields), Верхние поля костей (High Bonefields).
Среда: кислотный дождь в сезоне Acid Forest; Blood Spiders. Источник: https://kenshi.fandom.com/wiki/Burning_Forest, https://kenshi.zone/en/environment-hazards.
Локации:
- Древние лабы (Ancient Labs) — ruins
- Развалины фермы (Farm Ruin) — ruins
Источники: regions-index.md, https://kenshi.fandom.com/wiki/Burning_Forest.

## Дальние земли (The Outlands)
Положение: восток. Соседи: Берег грозового ущелья (Stormgap Coast), Ненужная зона (The Unwanted Zone), Сад Стоба (Stobe's Garden), Зелёный пляж (Greenbeach).
Среда: бандиты. Источник: https://kenshi.zone/en/locations.
Локации:
- Лагерь Разбойников (Reaver Camp) — outpost
- Фермерская деревня (Farming Village) — village
- Чёрная Ссадина (Black Scratch) — town
- Штаб Чёрных Псов (Black Dog HQ) — poi
Вербуемые: Бо (Bo) в Чёрной Ссадине (должен присоединиться к Anti-Slavers). Источники: recruits.md.

## Долина снайперов (Sniper Valley)
Положение: юго-восток. Соседи: Авантюра Стоба (Stobe's Gamble), Звонкий мрак (Sonorous Dark), Каньоны (The Pits), Утёсы (The Crags).
Среда: вулканический пояс. Источник: https://kenshi.zone/en/world-map.
Локации:
- Полицейские бараки (Police Barracks) — ruins · секретная
- Форпост снабжения старой империи (Old Empire Supply Outpost) — ruins · секретная
Источники: regions-index.md.

## Железные долины (Iron Valleys)
Положение: центр. Соседи: Скорняков край (Skinner's Roam), Гиблые земли (Deadlands), Чёрная пустыня (The Black Desert).
Среда: постоянный кислотный дождь и земля. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Затерянный арсенал (Lost Armoury) — ruins · секретная
- Ловушка Нарко (Narko's Trap) — military
Источники: regions-index.md, https://kenshi.zone/en/environment-hazards.

## Железный шлейф (The Iron Trail)
Положение: северо-запад. Соседи: Берег левиафанов (Leviathan Coast), Пурпурные пески (Purple Sands), Равнины людоедов (Cannibal Plains).
Среда: Iron Spiders, людоеды, кислотные дожди. Источник: https://kenshi.zone/en/locations.
Локации:
- Древняя техно лаба (Ancient Tech Lab) — ruins
Источники: regions-index.md.

## Запретный остров (Forbidden Isle)
Положение: восток. Соседи: Берег грозового ущелья (Stormgap Coast).
Среда: кислотный дождь ~50 % времени. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Древние лабы (Ancient Labs) — ruins
- Завод пауков (Spider Factory) — ruins · секретная
Источники: regions-index.md, https://kenshi.zone/en/environment-hazards.

## Звонкий мрак (Sonorous Dark)
Положение: юго-восток. Соседи: Пепельные земли (Ashlands), Долина снайперов (Sniper Valley), Серый шельф (Greyshelf), Царская долина (Royal Valley), Каньоны (The Pits), Авантюра Стоба (Stobe's Gamble).
Среда: кислотный дождь ~50 % времени. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Барьерная башня (Barrier Tower) — military
- Дом Кожи - Штаб (Skinhouse HQ) — outpost · секретная
- Дом кожи (Skinhouse) — outpost · секретная (×2)
Источники: regions-index.md, https://kenshi.zone/en/environment-hazards.

## Зелёный пляж (Greenbeach)
Положение: восток. Соседи: Сад Стоба (Stobe's Garden), Восточные каньоны (The Pits East), Дальние земли (The Outlands).
Среда: кислотные дожди спорадически. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Деревня крабов (Crab Village) — outpost · секретная
Источники: regions-index.md.

## Каньоны (The Pits)
Положение: юго-восток. Соседи: Утёсы (The Crags), Восточные каньоны (The Pits East), Сад Стоба (Stobe's Garden), Звонкий мрак (Sonorous Dark), Пепельные земли (Ashlands), Долина снайперов (Sniper Valley).
Среда: кислотные угрозы, песчаные бури. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Башня снайперов (Sniper Tower) — poi
- Затерянный арсенал (Lost Armoury) — ruins · секретная
- Полицейские бараки (Police Barracks) — ruins · секретная
Источники: regions-index.md.

## Кишка (Gut)
Положение: восток. Соседи: Берег грозового ущелья (Stormgap Coast), Хэн (Heng), Глаз (The Eye), Ревущий лабиринт (Howler Maze).
Среда: Gutters, высокие уровни. Источник: https://kenshi.zone/en/locations.
Локации:
- Странный лагерь (Strange Camp) — poi
Источники: regions-index.md.

## Кратер (The Crater)
Положение: юго-запад. Соседи: Шан (Shun), Крюк (The Hook), Сетка (The Grid), Южные болота (South Wetlands), Паучьи равнины (Spider Plains).
Среда: высокие уровни. Источник: community maps.
Локации:
- Древние лабы (Ancient Labs) — ruins
- Пустая лаба (Empty Lab) — ruins (×3)
- Руины лабы (Lab Ruin) — ruins
Источники: regions-index.md.

## Крюк (The Hook)
Положение: юг. Соседи: Южные болота (South Wetlands), Шан (Shun), Кратер (The Crater), Поля костей (Bonefields).
Среда: песчаные бури. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- База Охотников на людей (Manhunter Base) — outpost
- Брошенный посёлок (Abandoned Town) — ruins
- Выдержка Скитальца (Drifter's Last) — town
- Клаунстэди (Clownsteady) — town
- Путевая станция (Waystation) — outpost
- Руины библиотеки (Library Ruins) — ruins
- Южная рабская ферма (Slave Farm South) — slave_camp
Источники: regions-index.md.

## Мочалка (Bast)
Положение: север, между Святой Нацией и Союзными Городами. Соседи: Великая пустыня (The Great Desert), Синкаан (Sinkuun), Окранова долина (Okran's Valley), Северный берег (Northern Coast), Рвущие пески (Skimsands), Рука Окрана (Arm of Okran).
Среда: поля сражений. Источник: https://kenshi.zone/en/locations.
Локации:
- Дрин (Drin) — ruins
- Застава стражников (Guard Outpost) — poi (×2)
- Мочалка (Bast) — ruins
- Разорённая деревня (Ravaged Hamlet) — poi (×9)
- Эндин (Endin) — ruins
Связь с WS: Дрин разрушается при выбытии Валтэны (см. world-states.md).
Источники: regions-index.md, world-states.md.

## Мщение (Venge)
Положение: центр. Соседи: Сим (Shem), Авантюра Стоба (Stobe's Gamble), Берег грозового ущелья (Stormgap Coast), Ненужная зона (The Unwanted Zone), Серая пустыня (Grey Desert), Ровная лагуна (Flats Lagoon), Глаз (The Eye), Гиблые земли (Deadlands).
Среда: орбитальные лучи (burns) днём, скелеты, Thrall Masters. Источник: https://kenshi.zone/en/environment-hazards, https://kenshi.zone/en/locations.
Локации:
- Башня Жестокости (Tower of Abuse) — ruins
- Развалины путевой станции (Waystation Ruins) — ruins · секретная
- Разрушенная диспетчерская (Ruined Control Tower) — ruins · секретная
- Старая диспетчерская (Old Control Tower) — ruins · секретная
Вербуемые: Ану (Agnu) в Башне Жестокости (клетка + Meitou + враждебные рядом). Источники: recruits.md, https://kenshi.fandom.com/wiki/Agnu.

## Обломки (Dreg)
Положение: запад. Соседи: Острова тумана (Fog Islands), Тщета (Vain), Окранов залив (Okran's Gulf), Верещащий лес (The Shrieking Forest).
Среда: кислота, улей, бандиты. Источник: https://kenshi.zone/en/locations.
Локации:
- Деревня Оседлых Кочевников (Settled Nomad Village) — village
- Деревня собирателей (Gatherer Village) — village (×2)
- Улей (Hive Village) — village (×3)
Вербуемые: Корнелиус (Cornelius) в Деревне Оседлых Кочевников. Источники: recruits.md.

## Окранов залив (Okran's Gulf)
Положение: запад, западнее Окрановой гордости. Соседи: Окранова гордость (Okran's Pride), Острова тумана (Fog Islands), Пограничная зона (Border Zone), Возрождение (Rebirth), Пойма (Floodlands), Тщета (Vain), Обломки (Dreg).
Среда: плоские аридные земли. Источник: https://kenshi.fandom.com/wiki/Okran%27s_Gulf.
Локации:
- Мёртвый улей (Deadhive Overrun) — ruins · секретная
- Святая военная база (Holy Military Base) — military (×2)
- Святые шахты (Holy Mines) — village (×2)
- Стопка (Stack) — town
NPC: Инквизитор Сэта (High Inquisitor Seta) в Стопке. Связь с WS: Стопка, Святые военные базы → Deadhive при выбытии Феникса (см. world-states.md).
Источники: regions-index.md, https://kenshi.fandom.com/wiki/Okran%27s_Gulf, world-states.md.

## Окранова гордость (Okran's Pride)
Положение: центр-запад, плодородная. Соседи: Окранов залив (Okran's Gulf), Скорняков край (Skinner's Roam), Путь (Wend), Возрождение (Rebirth), Окранова долина (Okran's Valley), Пограничная зона (Border Zone), Рука Окрана (Arm of Okran).
Среда: плодородные луга, река, River Raptors. Самый населённый регион. Источник: https://kenshi.fandom.com/wiki/Okran%27s_Pride, https://kenshi.zone/en/locations.
Локации:
- Бугристый Холм (Blister Hill) — town
- Плохие Зубы (Bad Teeth) — town
- Святая ферма (Holy Farm) — village (×4)
NPC: Святой Лорд Феникс (Holy Lord Phoenix) в Бугристом Холме. Вербуемые: Бард (Bard), Гриффин (Griffin). Связь с WS: Бугристый Холм, Плохие Зубы, фермы (см. world-states.md).
Источники: regions-index.md, https://kenshi.fandom.com/wiki/Okran%27s_Pride, world-states.md.

## Окранова долина (Okran's Valley)
Положение: север, Святая Нация. Соседи: Рука Окрана (Arm of Okran), Мочалка (Bast), Окранова гордость (Okran's Pride), Северный берег (Northern Coast), Путь (Wend).
Среда: фермы. Источник: https://kenshi.fandom.com/wiki/Holy_Farms.
Локации:
- Развалины фермы (Farm Ruins) — ruins
- Святая ферма (Holy Farm) — village (×2)
Связь с WS: см. world-states.md.
Источники: regions-index.md.

## Остров Ящера (Raptor Island)
Положение: запад. Соседей нет: остров, отделён морем.
Среда: ящеры. Источник: https://kenshi.zone/en/locations.
Локации:
- Остров Ящера (Raptor Island) — poi
Источники: regions-index.md.

## Остров рыболюдов (Fishman Island)
Положение: юго-восток. Соседи: Поля костей (Bonefields).
Среда: рыболюды, кислотные дожди спорадически. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Островная лаба (Island Lab) — ruins · секретная
- Рыбный остров (Fish Isle) — town · секретная
NPC: Король Гурглер (King Gurgler). Источники: https://kenshi.fandom.com/wiki/King_Gurgler.

## Острова тумана (Fog Islands)
Положение: запад. Соседи: Обломки (Dreg), Окранов залив (Okran's Gulf), Верещащий лес (The Shrieking Forest).
Среда: туманники (carry/eat). Источник: https://kenshi.fandom.com/wiki/Fogmen, https://kenshi.zone/en/locations.
Локации:
- Безродный (Mongrel) — town
Вербуемые: Бип (Beep), Крошка Джон (Crumblejon), Вечный Суньвынь (Infinite Wingwang), Шрайк (Shryke). Связь с WS: вторжение туманников в Залив при выбытии Феникса (см. world-states.md).
Источники: regions-index.md, recruits.md, https://kenshi.fandom.com/wiki/Fogmen.

## Паучьи равнины (Spider Plains)
Положение: юг Шек. Соседи: Пустыня Стэнн (Stenn Desert), Болото (The Swamp), Дозорный рубеж (Watcher's Rim), Сетка (The Grid), Шан (Shun), Арах (Arach), Тщета (Vain), Пограничная зона (Border Zone), Кратер (The Crater).
Среда: Skin Spiders, шеки. Источник: https://kenshi.zone/en/locations.
Локации:
- Деревня Берсерков (Berserker Village) — outpost
- Последний Бой (Last Stand) — military
- Старая линия фронта (Old Frontlines) — ruins
NPC: Призрак (Ghost) в Деревне Берсерков. Вербуемые: Кан (Kang), Орон (Oron), Гигант Ранэ (Rane the Giant), Рука (Ruka) в Последнем Бою / Адмаге / Скуине. Источники: recruits.md, world-states.md.

## Пепельные земли (Ashlands)
Положение: юго-восток, конец карты. Соседи: Звонкий мрак (Sonorous Dark), Каньоны (The Pits).
Среда: water 0 %, fertility 0 %, iron/copper 300 %. Газ, Stormthralls, Behemoths. Источник: https://kenshi.zone/en/world-map, https://kenshi.zone/en/environment-hazards.
Локации:
- Пепельный купол I–IV (Ashland Dome I–IV) — ruins
- Руины пепельного купола (Ashland Dome Ruin) — ruins (×2)
- Ссылка Кат-Лона (Cat-Lon's Exile) — town
NPC: Кат-Лон (Cat-Lon). Источники: https://kenshi.fandom.com/wiki/Cat-Lon, lore.md.

## Пограничная зона (Border Zone)
Положение: центр-запад. Соседи: Болото (The Swamp), Скорняков край (Skinner's Roam), Окранов залив (Okran's Gulf), Тщета (Vain), Пустыня Стэнн (Stenn Desert), Окранова гордость (Okran's Pride), Паучьи равнины (Spider Plains), Сим (Shem).
Среда: пыльные бури. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- База Мятежников (Rebel Base) — poi
- Башня Ниндзя (Tower Of Ninjas) — poi
- Башня Пыльного Короля (Dust King Tower) — poi
- Маленькое селение (Tiny Settlement) — ruins
- Путевая станция (Waystation) — outpost
- Руины святой заставы (Ruined Holy Outpost) — ruins
- Скуин (Squin) — town
- Хаб (The Hub) — town
Вербуемые: Кот (Cat) в Башне Пыльного Короля, Хоббс (Hobbs) в Хабе. NPC: Король (Dust King). Связь с WS: Скуин (см. world-states.md).
Источники: regions-index.md, recruits.md.

## Пойма (Floodlands)
Положение: северо-запад. Соседи: Равнины людоедов (Cannibal Plains), Скрытый лес (Hidden Forest), Верещащий лес (The Shrieking Forest), Окранов залив (Okran's Gulf), Возрождение (Rebirth), Пурпурные пески (Purple Sands), Путь (Wend).
Среда: дождь, Iron Spiders, древние сооружения Первой империи. Источник: https://kenshi.zone/en/locations.
Локации:
- Башня Ожога (Burn's Tower) — ruins
- Древние лабы (Ancient Labs) — ruins
- Клонящаяся башня (Leaning Tower) — ruins
- Подозрительная лаба (Suspicious Lab) — ruins · секретная
- Пустые развалины (Empty Ruins) — ruins (×2)
- Руины башни (Ruined Tower) — ruins
- Упавшая башня (Fallen Tower) — ruins
Вербуемые: Ожог (Burn) в Башне Ожога. Источники: recruits.md.

## Поля костей (Bonefields)
Положение: юг. Соседи: Царская долина (Royal Valley), Верхние поля костей (High Bonefields), Ровная лагуна (Flats Lagoon), Горящий лес (Burning Forest), Серый шельф (Greyshelf), Остров рыболюдов (Fishman Island), Сим (Shem), Крюк (The Hook), Южные болота (South Wetlands).
Среда: песчаные бури. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Катун (Catun) — town
- Пустые развалины (Empty Ruin) — poi
- Старая тюрьма (The Old Prison) — ruins
- Траур (Mourn) — town · секретная
Источники: regions-index.md.

## Пурпурные пески (Purple Sands)
Положение: северо-запад. Соседи: Железный шлейф (The Iron Trail), Верещащий лес (The Shrieking Forest), Страна Берсерков (Berserker Country), Равнины людоедов (Cannibal Plains), Пойма (Floodlands).
Среда: песчаные бури. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Не-древняя мастерская (Post-Ancient Workshop) — ruins
Источники: regions-index.md.

## Пустыня Стэнн (Stenn Desert)
Положение: запад, ядро Королевства шеков (Shek Kingdom). Соседи: Тщета (Vain), Паучьи равнины (Spider Plains), Пограничная зона (Border Zone).
Среда: песчаные бури ~15 %. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Адмаг (Admag) — town
- Великая крепость (The Great Fortress) — military
- Лагерь изгнанников (Exile Camp) — poi
- Новая Кралия (New Kralia) — outpost
- Пустые развалины (Empty Ruins) — ruins
- Путевая станция (Waystation) — outpost
- Упавшая башня (Fallen Tower) — ruins
- Шекские руины (Shek Ruins) — ruins
NPC: Каменный Голем Эсата (Esata the Stone Golem) в Адмаге, Летящий Бык (Flying Bull) в Новой Кралии, Бесстрашная Тора (Tora the Fearless) в Лагере изгнанников. Вербуемые: Сэто (Seto) в Адмаге, Кан, Орон, Гигант Ранэ, Рука. Связь с WS: см. world-states.md.
Источники: regions-index.md, world-states.md, recruits.md.

## Путь (Wend)
Положение: север, Святая Нация. Соседи: Окранова гордость (Okran's Pride), Рука Окрана (Arm of Okran), Возрождение (Rebirth), Скрытый лес (Hidden Forest), Пойма (Floodlands), Окранова долина (Okran's Valley).
Среда: патрули СН, туманники. Источник: https://kenshi.zone/en/locations.
Локации:
- Затерянная библиотека (Lost Library) — ruins
- Затопленные руины (Drowned Ruins) — ruins
Источники: regions-index.md.

## Равнины людоедов (Cannibal Plains)
Положение: северо-запад. Соседи: Берег левиафанов (Leviathan Coast), Пойма (Floodlands), Скрытый лес (Hidden Forest), Железный шлейф (The Iron Trail), Северный берег (Northern Coast), Пурпурные пески (Purple Sands).
Среда: людоеды (большие группы, carry/eat). Источник: https://kenshi.zone/en/locations.
Локации:
- Деревня людоедов (Cannibal Village) — village (×3)
- Развалины арсенала (Armoury Ruin) — ruins
- Разведпост (Scout Post) — poi (×2)
- Старая деревня (Old Village) — ruins
- Столица людоедов (Cannibal Capital) — town · секретная
NPC: Великий шаман (Cannibal Grand Wizard). Источники: `published/tables/unique_npcs.csv`.

## Рвущие пески (Skimsands)
Положение: север, юго-западнее Великой пустыни. Соседи: Хребтовый каньон (Spine Canyon), Рука Окрана (Arm of Okran), Чёрная пустыня (The Black Desert), Хэн (Heng), Великая пустыня (The Great Desert), Глаз (The Eye), Мочалка (Bast).
Среда: песчаные бури. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Логово Кактуса (Cactus Den) — poi
- Хранилище Теньгу (Tengu's Vault) — prison
Вербуемые: Эсфер (Espher), Лукин (Luquin), Синклайд (Sinklyde) в Хранилище Теньгу (клетка + стражи СГ рядом). Источники: recruits.md.

## Ревущий лабиринт (Howler Maze)
Положение: восток. Соседи: Хэн (Heng), Кишка (Gut).
Среда: Howlers, кислотный дождь ~1/3 времени. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Город-архив (Archive Town) — ruins · секретная
- Затерянный город (Lost Town) — ruins · секретная
- Разграбленные руины (Looted Ruins) — ruins · секретная
Источники: regions-index.md, https://kenshi.zone/en/environment-hazards.

## Ровная лагуна (Flats Lagoon)
Положение: юго-восток. Соседи: Авантюра Стоба (Stobe's Gamble), Поля костей (Bonefields), Серый шельф (Greyshelf), Мщение (Venge), Сим (Shem).
Среда: Tech Hunters. Источник: https://kenshi.zone/en/locations.
Локации:
- Ровная лагуна (Flats Lagoon) — town
Вербуемые: Чад (Chad), Седая тень (Silvershade). Источники: recruits.md.

## Рука Окрана (Arm of Okran)
Положение: север, Святая Нация. Соседи: Окранова долина (Okran's Valley), Рвущие пески (Skimsands), Скрытый лес (Hidden Forest), Путь (Wend), Северный берег (Northern Coast), Окранова гордость (Okran's Pride), Скорняков край (Skinner's Roam), Мочалка (Bast).
Среда: военный пост. Источник: https://kenshi.zone/en/locations.
Локации:
- Дозорная башня (Watchtower) — poi
- Край Мира (World's End) — town
- Кулак Окрана (Okran's Fist) — military
NPC: Tech Hunters в Крае Мира. Связь с WS: Кулак Окрана (см. world-states.md).
Источники: regions-index.md, world-states.md.

## Сад Стоба (Stobe's Garden)
Положение: юго-восток. Соседи: Зелёный пляж (Greenbeach), Дальние земли (The Outlands), Утёсы (The Crags), Авантюра Стоба (Stobe's Gamble), Каньоны (The Pits), Ненужная зона (The Unwanted Zone), Восточные каньоны (The Pits East).
Среда: кислотные угрозы. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Башня пауков (Tower of Spiders) — poi · секретная
- Деревня крабов (Crab Village) — outpost · секретная
- Ковчег (Ark) — outpost · секретная
- Лагерь Разбойников (Reaver Camp) — outpost (×2)
- Развалины путевой станции (Waystation Ruins) — ruins · секретная
- Экспедиция 4 (Expedition 4) — ruins
Источники: regions-index.md.

## Северный берег (Northern Coast)
Положение: север. Соседи: Скрытый лес (Hidden Forest), Равнины людоедов (Cannibal Plains), Синкаан (Sinkuun), Рука Окрана (Arm of Okran), Тёмный палец (Darkfinger), Мочалка (Bast), Окранова долина (Okran's Valley).
Среда: людоеды. Источник: https://kenshi.zone/en/locations.
Локации:
- Деревня-призрак (Ghost Village) — village
- Рыбацкая деревня (Fishing Village) — village
Источники: regions-index.md.

## Серая пустыня (Grey Desert)
Положение: центр. Соседи: Глаз (The Eye), Гиблые земли (Deadlands), Мщение (Venge), Чёрная пустыня (The Black Desert).
Среда: песчаные бури. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Путевая станция (Waystation) — outpost
Источники: regions-index.md.

## Серый шельф (Greyshelf)
Положение: юго-восток. Соседи: Царская долина (Royal Valley), Авантюра Стоба (Stobe's Gamble), Ровная лагуна (Flats Lagoon), Звонкий мрак (Sonorous Dark), Поля костей (Bonefields).
Среда: кислота. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Занятый роями арсенал (Hiver-Claimed Armoury) — ruins · секретная (×2)
- Развалины арсенала (Armoury Ruin) — ruins (×2)
- Улей (Southern Hive Village) — village · секретная
Источники: regions-index.md.

## Сетка (The Grid)
Положение: юго-запад. Соседи: Кратер (The Crater), Паучьи равнины (Spider Plains), Южные болота (South Wetlands), Болото (The Swamp).
Среда: высокие уровни. Источник: community maps.
Локации:
- Цеховый комплекс (Workshop Complex) — ruins
Источники: regions-index.md.

## Сим (Shem)
Положение: центр. Соседи: Мщение (Venge), Скорняков край (Skinner's Roam), Болото (The Swamp), Горящий лес (Burning Forest), Гиблые земли (Deadlands), Ровная лагуна (Flats Lagoon), Поля костей (Bonefields), Пограничная зона (Border Zone).
Среда: бандиты. Источник: https://kenshi.zone/en/locations.
Локации:
- Бар контрабандистов (Smugglers Bar) — poi
- Оседлые кочевники (Settled Nomads) — village
Источники: regions-index.md.

## Синкаан (Sinkuun)
Положение: север. Соседи: Великая пустыня (The Great Desert), Мочалка (Bast), Тёмный палец (Darkfinger), Северный берег (Northern Coast).
Среда: людоеды. Источник: https://kenshi.zone/en/locations.
Локации:
- Бастион (The Bastion) — military
- Башня Козлов (Tower Of Goats) — poi · секретная
- Отдалённый улей (Distant Hive Village) — village
- Форт Симион (Fort Simion) — outpost · секретная
Источники: regions-index.md.

## Скорняков край (Skinner's Roam)
Положение: центр. Соседи: Окранова гордость (Okran's Pride), Гиблые земли (Deadlands), Пограничная зона (Border Zone), Сим (Shem), Железные долины (Iron Valleys), Рука Окрана (Arm of Okran).
Среда: 3 сезона, песчаные бури. Источник: https://kenshi.zone/en/world-map, https://kenshi.zone/en/environment-hazards.
Локации:
- Развалины святой шахты (Holy Mine Ruin) — ruins (×2)
- Святые шахты (Holy Mines) — village (×3)
Источники: regions-index.md.

## Скрытый лес (Hidden Forest)
Положение: север. Соседи: Рука Окрана (Arm of Okran), Пойма (Floodlands), Равнины людоедов (Cannibal Plains), Северный берег (Northern Coast), Путь (Wend).
Среда: людоеды. Источник: https://kenshi.zone/en/locations.
Локации:
- Деревня Отщепенцев (Flotsam Village) — village
Вербуемые: Дина (Digna), Нож (Knife), Пиа (Pia), Рева (Reva). Источники: recruits.md.

## Тропа хитрецов (Cheaters Run)
Положение: юго-восток. Соседи: Царская долина (Royal Valley).
Среда: кислотный дождь ~50 %. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Жуткие руины (Horrible Ruin) — ruins · секретная
- Полицейские бараки (Police Barracks) — ruins · секретная
- Рыбацкая деревня-призрак (Dead Fishing Village) — village · секретная
Источники: regions-index.md, https://kenshi.zone/en/environment-hazards.

## Тщета (Vain)
Положение: запад. Соседи: Обломки (Dreg), Пустыня Стэнн (Stenn Desert), Пограничная зона (Border Zone), Окранов залив (Okran's Gulf), Паучьи равнины (Spider Plains).
Среда: Beak Things, кислотная вода. Источник: https://kenshi.zone/en/locations.
Локации:
- Башня Тумана (Tower of Fog) — poi · секретная
- Западный Улей (Western Hive) — village
- Затерянная библиотека (Lost Library) — ruins
- Не-древняя мастерская (Post-Ancient Workshop) — ruins
- Улей (Hive Village) — village (×5)
Связь с WS: Queen gone → Deadhive (см. world-states.md).
Источники: regions-index.md, world-states.md.

## Тёмный палец (Darkfinger)
Положение: север. Соседи: Синкаан (Sinkuun), Северный берег (Northern Coast).
Среда: людоеды. Источник: https://kenshi.zone/en/locations.
Локации:
- Деревня людоедов (Cannibal Village) — village (×2)
- Затерянная библиотека (Lost Library) — ruins
Источники: regions-index.md.

## Утёсы (The Crags)
Положение: юго-восток. Соседи: Каньоны (The Pits), Сад Стоба (Stobe's Garden), Авантюра Стоба (Stobe's Gamble), Долина снайперов (Sniper Valley).
Среда: кислота, песчаные бури. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Железный штаб (Iron HQ) — outpost · секретная
- Форпост снабжения старой империи (Old Empire Supply Outpost) — ruins · секретная
Источники: regions-index.md.

## Хэн (Heng)
Положение: юг Великой пустыни. Соседи: Великая пустыня (The Great Desert), Ревущий лабиринт (Howler Maze), Глаз (The Eye), Кишка (Gut), Рвущие пески (Skimsands).
Среда: песчаные бури ~68 %. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Край Торговца (Trader's Edge) — outpost
- Рабская ферма (Slave Farm) — slave_camp
- Хэн (Heng) — town
- Южный каменный лагерь (South Stone Camp) — slave_camp
Вербуемые: Ямду (Yamdu) в Крае Торговца (WS: сдача Тинфиста). Источники: recruits.md.

## Царская долина (Royal Valley)
Положение: юго-восток. Соседи: Поля костей (Bonefields), Тропа хитрецов (Cheaters Run), Серый шельф (Greyshelf), Звонкий мрак (Sonorous Dark).
Среда: кислотный дождь ~10 %. Источник: https://kenshi.zone/en/environment-hazards.
Локации:
- Занятый роями арсенал (Hiver-Claimed Armoury) — ruins · секретная
- Улей (Southern Hive Village) — village · секретная
- Южный улей (Southern Hive) — town · секретная
Источники: regions-index.md, https://kenshi.zone/en/environment-hazards.

## Шан (Shun)
Положение: юго-запад. Соседи: Кратер (The Crater), Крюк (The Hook), Арах (Arach), Дозорный рубеж (Watcher's Rim), Паучьи равнины (Spider Plains).
Среда: высокие уровни. Источник: community maps.
Локации:
- Брошенный посёлок (Abandoned Town) — ruins
- Древняя техно лаба (Ancient Tech Lab) — ruins
- Затерянная библиотека (Lost Library) — ruins (×6)
- Затерянный арсенал (Lost Armoury) — ruins · секретная
- Развалины арсенала (Armoury Ruin) — ruins
Источники: regions-index.md.

## Южные болота (South Wetlands)
Положение: юг. Соседи: Болото (The Swamp), Крюк (The Hook), Сетка (The Grid), Верхние поля костей (High Bonefields), Кратер (The Crater), Поля костей (Bonefields).
Среда: кислота, пауки. Источник: https://kenshi.zone/en/locations.
Локации:
- База Болотных Ниндзя (Swamp Ninja Base) — poi · секретная
- Пустые развалины (Empty Ruin) — poi
- Рабские рынки (Slave Markets) — outpost
Вербуемые: Вынос мозга (Headshot), Рэй (Ray) на Рабских рынках. Источники: recruits.md.

## Регионы без локаций в индексе
- Страна Берсерков (Berserker Country): северо-запад, побережье западнее Пурпурных песков. Соседи: Пурпурные пески, Верещащий лес. Деревня Берсерков и Призрак находятся в Паучьих равнинах.
- Смирение (Obedience): северо-запад, белая пустыня севернее Островов тумана; на карте — Древние лабы. В растре регионов игры занимает 30 пикселей внутри участка без региона, общей границы с другими регионами нет; на игровой карте окружено Верещащим лесом, Поймой, Островами тумана, Окрановым заливом и Обломками. Скелеты, древние машины.
- Верещащий лес (The Shrieking Forest): северо-запад, южнее Пурпурных песков. Соседи: Пурпурные пески, Пойма, Страна Берсерков, Острова тумана, Обломки.
- Верхние поля костей (High Bonefields): юг. Соседи: Поля костей, Болото, Южные болота, Горящий лес. Высокие уровни.
- Чёрная пустыня (The Black Desert): центр, полоса между Железными долинами и Серой пустыней. Соседи: Рвущие пески, Гиблые земли, Железные долины, Серая пустыня, Глаз. Ядовитый газ.
- Глаз (The Eye): центр-восток, между Серой пустыней и Кишкой. Соседи: Хэн, Серая пустыня, Кишка, Берег грозового ущелья, Рвущие пески, Мщение, Чёрная пустыня. Орбитальные лучи.
- Дозорный рубеж (Watcher's Rim): юго-запад, горное кольцо вокруг Араха. Соседи: Арах, Паучьи равнины, Шан. Высокие уровни.
- Ненужная зона (The Unwanted Zone): восток, южнее Дальних земель. Соседи: Дальние земли, Мщение, Авантюра Стоба, Сад Стоба, Берег грозового ущелья. Высокие уровни.
- Хребтовый каньон (Spine Canyon): восток. Соседи: Рвущие пески, Великая пустыня. Песчаные бури.
- Центр (Central), Пустыня (Desert), Империя (Empire), The Desert: служебные / без данных в индексе.

Источники раздела: docs/reference/regions-index.md, https://kenshi.zone/en/environment-hazards, https://kenshi.zone/en/world-map, https://kenshi.zone/en/locations, https://kenshi.zone/en/deadlands, Kenshi Wiki (Zones, Okran's Pride, Okran's Gulf, Burning Forest, Fogmen, Bugmaster, Agnu, Cat-Lon, King Gurgler), published/tables/unique_npcs.csv, world-states.md, recruits.md. Vanilla only.

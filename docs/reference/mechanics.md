# Боевые и экономические механики Kenshi (Vanilla)

Справочник по ключевым боевым и экономическим системам Kenshi 1 (Vanilla). Источники: FCS / Web FCS, Kenshi Wiki (kenshi.fandom.com), kenshi.zone. Русские названия — приоритетно из docs/Kenshi_RU_EN.md. Английские термины в скобках при первом упоминании.

## Грейды оружия и производители

Грейды (model value 1–100) и производители определяют финальные статы. Homemade — базовая линия без бонусов.

| Грейд (RU/EN) | Level | Производитель | Cut mod | Blunt mod | Weight mod | Price mod |
|---------------|-------|---------------|---------|-----------|------------|-----------|
| Ржавый хлам / Rusted Junk | 5 | Unknown | 1.0 | 1.0 | 1.0 | 0.3 |
| Ржавеющий клинок / Rusting Blade | 10 | Unknown | 1.0 | 1.0 | 1.0 | 0.3 |
| Средний salvage / Mid-Grade Salvage | 15 | Ancient | 0.9 | 1.0 | 0.7 | 0.8 |
| Старый перекованный клинок / Old Refitted Blade | 20 | Ancient | 0.9 | 1.0 | 0.7 | 0.8 |
| Перекованный клинок / Refitted Blade | 25 | Ancient | 0.9 | 1.0 | 0.7 | 0.8 |
| Катун №1 / Catun No.1 | 30 | Catun Scrapmaster | 1.0 | 1.2 | 1.2 | 1.2 |
| Катун №2 / Catun No.2 | 35 | Catun Scrapmaster | 1.0 | 1.2 | 1.2 | 1.2 |
| Катун №3 / Catun No.3 | 40 | Catun Scrapmaster | 1.0 | 1.2 | 1.2 | 1.2 |
| Mk I | 50 | Skeleton Smiths | 1.0 | 1.0 | 1.0 | 1.2 |
| Mk II | 55 | Skeleton Smiths | 1.0 | 1.0 | 1.0 | 1.2 |
| Mk III | 60 | Skeleton Smiths | 1.0 | 1.0 | 1.0 | 1.2 |
| Edge Type 1 | 70 | Edgewalkers | 1.1 | 1.0 | 1.0 | 1.4 |
| Edge Type 2 | 75 | Edgewalkers | 1.1 | 1.0 | 1.0 | 1.4 |
| Edge Type 3 | 80 | Edgewalkers | 1.1 | 1.0 | 1.0 | 1.4 |
| Meitou | 100 | Cross | 1.1 | 1.0 | 1.0 | 2.0 |
| Homemade (игрок) | 5–80 | Homemade | 1.0 | 1.0 | 1.0 | 1.0 |

**Формулы (упрощённо):**
- Cut = cut_mult × (0.3 + 0.017 × model_value) × manuf_cut
- Blunt = blunt_mult × model_value / 50 × manuf_blunt
- Meitou ~5.2× лучше Rusted Junk по базовому cut (с бонусом Cross ~5.7×).

Ковка: качество зависит от навыка «Ковка оружия» (Weapon Smithing), освещения и состояния персонажа. Edge Type 3 и Meitou в ванилле не крафтятся. Сила (Strength) для тяжёлого оружия: примерно max(weight×2, blunt×40).

Источники: https://kenshi.fandom.com/wiki/Weapons_(FCS), https://kenshi.zone/en/weapons, Steam/Shidan.

## Классы оружия

Cut (режущий) vs Blunt (дробящий). Разные множители против людей / животных / роботов (в FCS). Штрафы в помещениях (reach). Тяжёлое оружие требует высокой силы. Примеры из локализации: Катана, Сабля, Рубач, Тяжёлое оружие, Дробящее, Древковое.

## Броня

Покрытие зон (coverage %), сопротивления (cut / blunt / pierce), штрафы (athletics, combat speed, stealth, dodge). Сопротивления нескольких предметов складываются мультипликативно.

**Тяжёлая броня (стандартный грейд, примеры):**

| Предмет (RU/EN) | Coverage (основные) | Cut | Blunt | Pierce | Вес | Штрафы |
|-----------------|---------------------|-----|-------|--------|-----|--------|
| Святая нагрудная пластина / Holy Chest Plate | Грудь 100%, живот 100%, руки 25%, ноги 40% | 40% | 22% | 36 | 19 кг | Dodge 50%, Dex 70% |
| Доспех самурая / Samurai Armour | Грудь 100%, живот/руки 85% | 40% | 26% | 36 | 20.25 кг | Dodge 60%, Dex 100% |
| Доспех наёмника / Mercenary Plate | — | 33% | 21% | 27 | 20 кг | — |

Грейды брони: Prototype (5) → Shoddy (20) → Standard (40) → High (60) → Specialist (80) → Masterwork (95). Святая Нация: паладины в Holy Chest Plate. Союзные Города: самурайские комплекты. Полные сеты сильно снижают скорость и скрытность.

Источники: https://kenshi.zone/en/item-holy-chest-plate, https://kenshi.zone/en/item-samurai-armour, https://kenshi.zone/en/item-heavy-armour, https://kenshi.fandom.com/wiki/Armor_Stats.

## Протезы

Модели: Economy, Skeleton, Stealth, Scout, KLR Series, Industrial Lifter, Steady/Thief (последние два не крафтятся).

**Цепочка исследований (Crafting Tech):**
1. Robotics (Tech Level 3, 1 Ancient Science Book)
2. Hiver Skeleton Legs (Tech) и Hiver Skeleton Arms (Tech) (Level 4)
3. Skeleton Legs / Arms (Level 5, AI Cores)
4. Специализированные (Scout, Stealth, KLR, Industrial — Level 6)

**Проверка: Hiver Skeleton Legs/Arms (Tech)** — Vanilla. Описание: «копия технологии Economy Legs улья, первый шаг к производству заменяемых конечностей». Применимы ко всем гуманоидным расам (включая Hivers и Skeletons после потери конечности). Крафт на Skeleton Limb Bench. Качество зависит от навыка «Роботехника» (Robotics).

Множители (примерно, Masterwork): Scout Legs +athletics, Stealth Legs +stealth, Skeleton Arms +dexterity, Industrial +strength, KLR — баланс.

Источники: https://kenshi.zone/en/robotic-limbs, https://kenshi.zone/en/item-skeleton-legs-tech, https://kenshi.fandom.com/wiki/Hiver_Skeleton_Legs_(Tech), https://kenshi.fandom.com/wiki/Robot_Limbs.

## Экономика и торговля

Базовая цена × культура-множитель × случайный ±30% × наличность торговца. Гашиш (Hashish): база ~144 ката. Пенька → гашиш (Hemp Processor).

| Культура / фракция | Множитель гашиша | Контрабанда |
|--------------------|------------------|-------------|
| Союзные Города (Empire) | 1200% | Да |
| Работорговцы | 600% | Да |
| Святая Нация | 400% | Да |
| Королевство Шек | 350% | Да |
| Болотники (Swampers) | 100% | Нет |
| Ровная лагуна / Flats Lagoon, Траур / Mourn | ~400% | Нет (легально) |

Воры шиноби покупают за половину цены. Награды за головы (bounties): от ~10k до 100k+ катов (Феникс, Хозяин Жуков и др.).

Источники: https://kenshi.zone/en/economy, https://kenshi.zone/en/item-hashish, https://kenshi.fandom.com/wiki/Hashish.

## Прочее

- Массовый бой: численный перевес, окружение, knockout (KO), вынос раненых (туманники, людоеды, рыболюди).
- Скрытые операции: knockout, carry, похищение спящих. Условия тревоги (свидетели, шум).
- Развитие: sparring, toughness от урона, athletics от бега, stealth от скрытности. Ориентиры высоких уровней 70–80+.

Источники раздела: FCS, Kenshi Wiki (Weapons, Armor, Limbs, Hashish), kenshi.zone (weapons, armour, robotic-limbs, economy, item-*). Vanilla only.

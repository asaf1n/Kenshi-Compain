# Справочник NPC и типов юнитов Kenshi (Vanilla) — предварительный план и структура

Источники: Kenshi Wiki (Factions, Races, individual unit pages), kenshi.zone (factions, races, unit notes). Vanilla only.

## Предлагаемая структура справочника

1. **Введение**: Расы (Greenlander, Scorchlander, Shek, Hive variants, Skeleton, Soldierbot, animals), общие характеристики (HP limbs, speed, hunger, healing, racial bonuses/penalties).
2. **Основные фракции** (по порядку важности):
   - Святая Нация (Holy Nation)
   - Союзные Города (United Cities) + Traders Guild + Slave Traders
   - Королевство Шеков (Shek Kingdom) + Kral's Chosen + Berserkers
   - Улей (Western/Southern Hive) + Fogmen/Deadhive
   - Tech Hunters, Anti-Slavers, Flotsam Ninjas
   - Hostile factions (Cannibals, Skin Bandits, Reavers, Crab Raiders, etc.)
   - Wildlife / Ancient machines
3. **Для каждой фракции**:
   - Общее описание и базовая враждебность (attacks on sight? conditions: race, relations ≤ -30, world states).
   - Типы юнитов (иерархия: leaders, elites, regulars, civilians, slaves).
   - Характеристики: типичные stats ranges (combat skills, toughness, athletics), weapons, armour, special abilities.
   - Поведение: patrols, raids, carry/eat (Fogmen/Cannibals), KO, dialogue.
   - Связь с World States.
4. **Сводная таблица базовой враждебности** (attacks on sight по расе/условиям).
5. **Animals и machines**.

## Черновик ключевых данных

### Расы (кратко)
- **Greenlander**: стандарт humans, balanced.
- **Scorchlander**: higher athletics/stealth, lower strength.
- **Shek**: high strength/toughness, natural armour, slow heal, high hunger.
- **Hive Worker Drone**: low combat, high labouring/farming.
- **Hive Soldier Drone**: higher combat, lower labour.
- **Hive Prince**: leaders, higher stats.
- **Skeleton**: no hunger, high robotics, vulnerable to anti-skeleton.
- **Soldierbot**: high strength, rare.

### Святая Нация (Holy Nation)
- Базовая враждебность: attacks on sight Shek, Hivers, Skeletons, anyone with prosthetics, non-humans. Neutral to humans if not criminal.
- Типы: Holy Lord Phoenix (elite, Meitou), High Inquisitors (Seta, Valtena), High Paladins, Paladins, Holy Sentinels, Chosen, Holy Nation Servants (slaves as troops), Priests.
- Характеристики: Paladins ~40-60 combat, heavy armour (Holy Chest Plate), Cross weapons. High Inquisitors higher.
- Поведение: patrols, Wrath of God raids (при Phoenix gone), searches for "skeleton in disguise".

### Союзные Города (United Cities)
- Базовая враждебность: neutral to most; hostile if criminal or relations low. Slave Hunters/Manhunters aggressive.
- Типы: Emperor Tengu, nobles (Lady Sanda etc.), Samurai, Samurai Rogues, Empire Peasants, Slave Masters.
- Характеристики: Samurai medium-heavy armour, better arm coverage. Stats vary by rank.

### Королевство Шеков (Shek Kingdom)
- Базовая враждебность: neutral/aggressive warrior culture; hostile to HN. Kamikaze if low morale.
- Типы: Esata (Stone Golem, Meitou Fragment Axe), Hundred Guardians, Shek Warriors, Shek Scouts, Kamikaze.
- Характеристики: high strength/toughness, medium/heavy mixes, high combat skills (40+).

### Улей и Fogmen
- Western Hive: mostly neutral, villages in Vain/Dreg. Queen gone → Deadhive.
- Fogmen (Deadhive): attacks on sight, carry/eat, acid. Fog Princes higher stats.
- Southern Hive: more hostile.

### Hostile factions (attacks on sight)
- Cannibals: high numbers, carry/eat, poles. Chiefs with bounties.
- Berserkers: high-level Shek, maroon robes.
- Skin Bandits: high-level, skinning.
- Fogmen: as above.
- Reavers, Crab Raiders, Swamp Ninjas, Dust Bandits, Sand Ninjas, Shrieking Bandits: vary by strength.

### Wildlife
- Beak Things, Leviathans, Iron Spiders, Blood Spiders, Skin Spiders, Bonedogs, Goats, Crabs, Fishmen, Howlers, Gutters, Stormthralls, Behemoths.
- Many carry/eat or environmental threats.

Полный справочник будет расширен по конкретным unit templates из FCS/вики. Связь с world-states.md и regions_atlas.md.
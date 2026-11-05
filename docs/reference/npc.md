# Справочник NPC и типов юнитов Kenshi (Vanilla)

Справочник по расам, фракциям и типам юнитов Kenshi 1 (Vanilla). Источники: Kenshi Wiki (Factions, Races, individual unit pages), kenshi.zone (factions, races). Русские названия — приоритетно из docs/Kenshi_RU_EN.md и поля `name_ru` из published/current/world_state.json. Связь с world-states.md и regions_atlas.md. Vanilla only.

## Расы (кратко)

| Раса | Особенности | Бонусы / штрафы |
|------|-------------|-----------------|
| Greenlander | Стандартные люди | Сбалансированы |
| Scorchlander | Пустынные люди | Выше athletics/stealth, ниже strength |
| Shek | Воины с рогами | Высокая strength/toughness, natural armour, медленное заживление, высокий голод |
| Hive Worker Drone | Рабочие улья | Низкий бой, высокая labouring/farming |
| Hive Soldier Drone | Солдаты улья | Выше бой, ниже labour |
| Hive Prince | Лидеры улья | Выше статы |
| Skeleton | Скелеты | Нет голода, высокая robotics, уязвимы к anti-skeleton |
| Soldierbot | Редкие солдатские скелеты | Высокая strength |

## Основные фракции

### Святая Нация (Holy Nation)
- **Базовая враждебность:** attacks on sight Shek, Hivers, Skeletons, anyone with prosthetics, non-humans. Neutral to humans if not criminal / low relations.
- **Типы юнитов:** Святой Лорд Феникс (Holy Lord Phoenix, elite, Meitou), Инквизитор Сэта / Инквизитор Валтэна (High Inquisitor), High Paladins, Paladins, Holy Sentinels, Chosen, Holy Nation Servants, Priests.
- **Характеристики:** Paladins ~40–60 combat skills, Holy Chest Plate, Cross weapons. High Inquisitors выше.
- **Поведение:** патрули, Wrath of God raids (при выбытии Феникса), обыски на «skeleton in disguise».
- **World States:** см. world-states.md (Феникс, Сэта, Валтэна).

### Союзные Города (United Cities) + Traders Guild + Slave Traders
- **Базовая враждебность:** neutral к большинству; hostile при low relations или преступлении. Slave Hunters / Manhunters агрессивны.
- **Типы:** Император Тенгу, дворяне, Samurai, Samurai Rogues, Empire Peasants, Slave Masters.
- **Характеристики:** Samurai medium-heavy armour (лучше покрытие рук). Статы по рангу.

### Королевство Шек (Shek Kingdom) + Kral's Chosen + Berserkers
- **Базовая враждебность:** warrior culture; hostile к Святой Нации. Kamikaze при low morale.
- **Типы:** Каменный Голем Эсата (Meitou Fragment Axe), Hundred Guardians, Shek Warriors, Shek Scouts, Kamikaze, Летящий Бык, Призрак (Ghost).
- **Характеристики:** высокая strength/toughness, medium/heavy mixes, combat 40+.

### Улей (Western / Southern Hive) + Fogmen / Deadhive
- Western Hive: mostly neutral, деревни в Vain / Dreg. Queen gone → Deadhive.
- Fogmen (Deadhive): attacks on sight, carry/eat. Fog Princes выше статы.
- Southern Hive: более hostile.

### Другие
- Tech Hunters, Anti-Slavers, Flotsam Ninjas (Молл): mostly neutral / conditional.
- Hostile (attacks on sight): Cannibals (carry/eat, poles), Berserkers, Skin Bandits, Reavers, Crab Raiders, Swamp Ninjas, Dust Bandits, Sand Ninjas, Shrieking Bandits.

## Сводная таблица базовой враждебности (attacks on sight)

| Фракция / тип | Условие |
|---------------|---------|
| Святая Нация | Shek, Hiver, Skeleton, prosthetic, non-human |
| Fogmen / Cannibals | Всегда (organics) |
| Skin Bandits / Reavers / Crab Raiders | Всегда |
| Союзные Города | Low relations / criminal |
| Шек | Low relations / HN |
| Western Hive | Usually neutral |
| Wildlife (Beak Things, Leviathans, Iron Spiders и др.) | Обычно всегда |

## Wildlife и machines

Beak Things, Leviathans, Iron Spiders, Blood Spiders, Skin Spiders, Bonedogs, Goats, Crabs, Fishmen, Howlers, Gutters, Stormthralls, Behemoths. Многие carry/eat или environmental threats.

Полный справочник расширяется по конкретным unit templates из FCS / вики.  

Источники: Kenshi Wiki (Factions, Races), kenshi.zone, published/current/world_state.json (name_ru). Vanilla only.

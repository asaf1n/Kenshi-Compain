# Боевые и экономические механики Kenshi (Vanilla)

Источники: FCS/Web FCS, Kenshi Wiki, kenshi.zone, Steam. Русские названия по Kenshi_RU_EN.md.

## Лестница грейдов оружия

Грейды: Prototype/Rusted Junk (5) → ... → Meitou (100). Производители влияют на множители.

| Manufacturer | Cut mod | Blunt mod | Weight mod | Notes |
|--------------|---------|-----------|------------|-------|
| Unknown | 1 | 1 | 1 | Price 0.3 |
| Ancient | 0.9 | 1 | 0.7 | Lighter |
| Catun Scrapmaster | 1 | 1.2 | 1.2 | Blunt bonus |
| Skeleton Smiths | 1 | 1 | 1 | - |
| Edgewalkers | 1.1 | 1 | 1 | Cut bonus |
| Cross (Meitou) | 1.1 | 1 | 1 | Price 2 |
| Homemade | 1 | 1 | 1 | Baseline |

Формулы (упрощённо): Cut = mult * (0.3 + 0.017 * model_value); Blunt = mult * model_value / 50 * manuf. Meitou ~5x+ лучше Rusted. Strength req ≈ max(weight*2, blunt*40). [Kenshi Wiki Weapons FCS; kenshi.zone weapons; Shidan Steam]

## Классы оружия

Cut (режущий) vs Blunt (дробящий). Бронепробитие, множители против robots/animals/humans (в FCS). Штрафы в помещениях (reach). Сила для тяжёлых. [Wiki]

## Броня

Покрытие зон (coverage %), сопротивления (cut/blunt/pierce), штрафы (athletics, combat speed, stealth, dodge).

Тяжёлая: Holy Chest Plate (HN паладины: chest 100%, arms 25%, legs 40%; cut ~40% standard), Samurai Armour (UC: better arm coverage), Shek warriors часто medium/heavy mixes. Full sets stack multiplicatively. [kenshi.zone heavy armour, holy chest plate; Wiki Armor Stats]

## Развитие персонажа

Тренировка: sparring, toughness (damage), athletics (run), stealth (sneak). Ориентиры 70-80+: use prepared fighter. Skills soft-cap effectively. [Community/guides]

## Массовый бой

Численный перевес, окружение, knockout (KO), вынос раненых (Fogmen, Cannibals, Fishmen carry to poles). [Wiki]

## Скрытые операции

Knockout, carry, kidnap sleeping NPC. Alert conditions (witness, noise). [Mechanics knowledge]

## Протезы

Модели: Economy, Skeleton, Stealth, Scout, KLR, Industrial, Steady/Thief (some non-craftable).

Грейды Prototype–Masterwork. Множители: Scout Legs +38% athletics, Stealth Legs +25% stealth, Skeleton Arms +25% dexterity.

Изготовление: Skeleton Limb Bench, research chain (Robotics → Hiver Skeleton Legs/Arms → Skeleton Legs → specialists). AI Cores required.

**Проверка: Hiver Skeleton Legs/Arms (Tech)** — Vanilla. Stepping stone to replacement limbs. Применимы ко всем расам (включая Hivers, Skeletons после потери limb). [kenshi.zone robotic-limbs, skeleton-legs-tech; Wiki Hiver Skeleton Legs (Tech); Reddit confirmation]

Расовые: все humanoids; Skeletons native limbs vs prosthetic.

## Экономика

Базовые цены, торговые коэффициенты (города/культуры), наценки (гашиш в Ровная лагуна / Flats Lagoon). Наличность торговцев. Цепочки: пенька (hemp) → гашиш. Награды за головы (bounties 10k–100k+). [Wiki Bounty; zone]

Источники: Kenshi Wiki (Weapons, Armor, Limbs), kenshi.zone (weapons, armour, robotic-limbs, item-*), Steam/Shidan notes. Vanilla only.